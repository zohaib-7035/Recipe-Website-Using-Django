from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Vege


@login_required(login_url='/login/')
def recipe(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')
        Vege.objects.create(name=name, description=description, image=image)
        return redirect('/recipe/')

    query = request.GET.get('search')
    if query:
        queryset = Vege.objects.filter(name__icontains=query)
    else:
        queryset = Vege.objects.all()

    context = {
        'queryset': queryset
    }
    return render(request, 'recipe.html', context)


def delete_recipe(request, id):
    recipe = get_object_or_404(Vege, id=id)
    recipe.delete()
    return redirect('/recipe/')

def update_recipe(request, id):
    recipe = Vege.objects.get(id=id)

    if request.method == "POST":
        recipe.name = request.POST.get('name')
        recipe.description = request.POST.get('description')
        if request.FILES.get('image'):
            recipe.image = request.FILES.get('image')
        recipe.save()
        return redirect('recipe')  # go back to list page

    return render(request, 'update.html', {'recipe': recipe})


def login_page(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/recipe/')  # Change 'home' to your desired route name
        else:
            error = 'Invalid username or password'

    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')  # Redirect to login page after logout


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Passwords must match
        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})


        # Username must be unique
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        # Optional: Email check
        if email and User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email is already in use'})

        # All good - create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        return redirect('/login/')  # Or wherever your login page is named in urls.py

    return render(request, 'register.html')
