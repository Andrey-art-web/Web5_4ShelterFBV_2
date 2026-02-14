from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from dogs.forms import DogForm
from dogs.models import Breed, Dog


def index(request):
    context = {
        'objects_list': Breed.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)


def breeds_list_view(request):
    context = {
        'objects_list': Breed.objects.all(),
        'title': 'Питомник - Все наши породы'
    }
    return render(request, 'dogs/breeds.html', context)


def breeds_dogs_list_view(request, pk: int):
    breed_item = Breed.objects.get(pk=pk)
    context = {
        'objects_list': Dog.objects.filter(breed_id=pk),
        'title': f'Собаки породы - {breed_item}',
        'breed_pk': breed_item.pk,
    }
    return render(request, 'dogs/dogs.html', context)


def dogs_list_view(request):
    context = {
        'object': Dog.objects.all(),
        'title': 'Питомник все наши собаки'
    }
    return render(request, 'dogs/dogs.html', context)


# def dog_create_view(request):
#     if request.method == 'POST':
#         form = DogForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('dogs:dogs_list'))
#         context = {
#             'title': 'Добавить собаку',
#             'form': DogForm()
#         }
#         return render(request, 'dogs/create.html', {})
def dog_create_view(request):
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dogs:dogs_list'))
    context = {
        'title': 'Добавить собаку',
        'form': DogForm()  # Используем form, а не DogForm() для сохранения данных при ошибках
    }
    return render(request, 'dogs/create.html', {})
