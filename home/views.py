from django.shortcuts import render

# Create your views here.
from django.shortcut import HttpResponse

def home (request):

#  return  HttpResponse("""<h1>hey i am a django server,<h1> 
#                       <p> hey this is comming form form django server </p> 
#                       <hr>hey </hr>
#                       <h3 >hope your good </h3>   
    
#    """)
    
    peoples ={
        {'name':'ram','age':26},
        {'name':'shyam','age':16},
        {'name':'hari','age':6},
        {'name':'ritesh' , 'age':2}

    }

for people in peoples :
    if people ['age']:
        print("yes")


    vegetables={'pumkins','potato','tomato'}

text="""lorem leroem erl erejr e"""
for peoples in peoples:
    print(peoples)

 return render(request, "home/index.html", context={'page': 'django tuts', 'peoples': peoples, 'vegetables': vegetables})


def about(request):
     context ={'page':'about'}
    return render(request,"home/about.html",context)

def contact (request):
    context ={'page':'contact'}
return render(request,"home/contact.html",context)

def sucess_page (request):
    print("*" *10)
    return HttpResponse("<h1>hey this is a sucess page </h1>")