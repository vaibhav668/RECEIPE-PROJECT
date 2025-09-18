from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request): 
    peoples=[
        {"name":"sachin","age":24}, 
        {"name":"rahul","age":13},  
        {"name":"rohit","age":26}
    ]
    vegies=['potato','tomato','onion','carrot']
    return render(request,"index.html",context={'page':'Django 2025 tut','peoples':peoples,'vegies':vegies})
def about(request):
    context={'page':'About'}
    return render(request,"about.html",context)
def contact(request):
    context={'page':'Contact'}
    return render(request,"contact.html",context)

def success_page(request):
    return HttpResponse("<h1>hey i am success page </h1>")