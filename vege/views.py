from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def receipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            )

    # return redirect('/receipe/')
    queryset = Receipe.objects.all()
    context = {'receipe':queryset}

    return render(request, 'receipe.html', context)

def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipe/')
        
    context = {'receipe':queryset}
    return render(request, 'update_receipe.html', context)

def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipe/')


