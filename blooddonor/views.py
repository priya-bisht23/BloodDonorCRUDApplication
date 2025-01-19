# blooddonor/views.py
from django.contrib.auth.models import User  # Add this import


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Add this import for login_required

#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import login, logout
from .forms import DonorForm, UserRegistrationForm
from .models import Donor
from django.shortcuts import render, get_object_or_404, redirect

# blooddonor/views.py

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import DonorForm
from .models import Donor

# ... other views ...

def register_user(request):
    if request.method == 'POST':
        # Handle user registration logic
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if the username is unique
        if User.objects.filter(username=username).exists():
            # Handle case where the username already exists
            # You might want to redirect back to the registration form with an error message
            return render(request, 'registration/register.html', {'error': 'Username already exists'})

        if password1 == password2:
            # Create user
            user = User.objects.create_user(username, email, password1)
            login(request, user)
            return redirect('login')
        else:
            # Handle password mismatch (you might want to add error messages)
            return render(request, 'registration/register.html', {'error': 'Passwords do not match'})

    return render(request, 'registration/register.html')
    if request.method == 'POST':
        # Handle user registration logic
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            # Create user
            user = User.objects.create_user(username, email, password1)
            login(request, user)
            return redirect('login')
        else:
            # Handle password mismatch (you might want to add error messages)
            pass

    return render(request, 'registration/register.html')

def login_user(request):
    if request.method == 'POST':
        # Handle user login logic
        username = request.POST['username']
        password = request.POST['password']

        print(f"Attempting login with username: {username}, password: {password}")
        user = authenticate(request, username=username, password=password)
        print(f"Authenticated user: {user}")


        if user is not None:
            login(request, user)
            return redirect('donor_list')
        else:
            # Handle unsuccessful login (you might want to add error messages)
            pass

    return render(request, 'registration/login.html')

def logout_user(request):
    logout(request)
    return redirect('donor_list')

    # Handle user logout logic
    return redirect('login')

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'blooddonor/donor_list.html', {'donors': donors})

def donor_detail(request, donor_id):
    donor = Donor.objects.get(pk=donor_id)
    return render(request, 'blooddonor/donor_detail.html', {'donor': donor})

def create_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm()
    
    return render(request, 'blooddonor/donor_form.html', {'form': form})

# ... (other views)

def edit_donor(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)

    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm(instance=donor)

    return render(request, 'blooddonor/donor_form.html', {'form': form})

def delete_donor(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)

    if request.method == 'POST':
        donor.delete()
        return redirect('donor_list')

    return render(request, 'blooddonor/donor_confirm_delete.html', {'donor': donor})

