from django.shortcuts import render,redirect
from .models import Receipe

# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')  # Corrected the syntax here
        receipe_name = data.get('recipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
        )
        
        
        return redirect('/receipe')
    
    
    
    queryset=Receipe.object.all()
    context = {'receipes': queryset}

        
    return render(request, 'receipes.html' ,context)
