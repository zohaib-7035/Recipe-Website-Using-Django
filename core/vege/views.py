from django.shortcuts import render,redirect,get_object_or_404
from .models import Vege
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