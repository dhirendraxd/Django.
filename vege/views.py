from django.shortcuts import render, redirect
from .models import Receipe

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('recipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
        )
        
       
