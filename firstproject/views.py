from django.shortcuts import render, HttpResponse

def home(request):
    peoples = [
        {'name': 'ram', 'age': 26},
        {'name': 'shyam', 'age': 16},
        {'name': 'hari', 'age': 6},
        {'name': 'ritesh', 'age': 2}
    ]

    for people in peoples:
        if people['age'] > 0:  # Checking if age is greater than 0
            print("yes")

    vegetables = ['pumkins', 'potato', 'tomato']

    text = """lorem leroem erl erejr e"""
    for people in peoples:
        print(people)

    return render(request, "home/index.html", context={'page': 'django tuts', 'peoples': peoples, 'vegetables': vegetables})

def about(request):
    context = {'page': 'about'}
    return render(request, "home/about.html", context)

def contact(request):
    context = {'page': 'contact'}
    return render(request, "home/contact.html", context)

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>hey this is a success page </h1>")

