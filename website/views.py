from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from .forms import SignUpForm ,AddRecordForm
from django.contrib import messages
from .models import records


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully registered! Welcome!")
                return redirect('home')
            else:
                pass
                messages.error(request, "Error occurred during registration. Please try again.")
        else:
            pass
            messages.error(request, "Invalid form data. Please correct the errors.")
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})


def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('user')  # Redirect to the home page
        else:
            messages.error(request, "Incorrect username or password")
    return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

# @login_required
# def user_view(request):
#     record = records.object.all()
#     return render(request, 'user.html', {'records':record})

@login_required
def user_view(request):
    records_list = records.objects.all()
    return render(request, 'user.html', {'records': records_list})

def user_details(request , pk):
        if request.user.is_authenticated:
            user_details = records.objects.get(id=pk)
            return render(request, 'user_details.html', {'user_details':user_details})
        else:
            messages.success(request, "You Must Be Logged In To View That Page...")
            return redirect('home')


def user_delete(request, pk):
	if request.user.is_authenticated:
		delete_it = records.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('user')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')
     
def add_user(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_user = form.save()
				messages.success(request, "Record Added...")
				return redirect('user')
		return render(request, 'add_user.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
    
def update_user(request, pk):
    if request.user.is_authenticated:
        current_user = records.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_user)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record has been updated successfully!")
                return redirect('user')
            else:
                messages.error(request, "Invalid form data. Please correct the errors.")
        return render(request, 'update_user.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to update user records.")
        return redirect('home')

      
      