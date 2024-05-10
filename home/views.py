from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name':'Amit', 'Age':24}, {'name':'Raj', 'Age':18}, {'name':'Siya', 'Age':16}, {'name':'Riya', 'Age':19}, {'name':'Akshay', 'Age':25}
    ]

    text="""
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo maiores dignissimos odio, repudiandae, dolor temporibus amet ut, corporis laborum neque similique animi provident! Beatae et minima architecto neque accusantium perferendis aliquam unde magnam harum facilis libero tenetur nobis, tempora quod voluptas quos nesciunt esse, possimus id veniam quas! Ducimus, assumenda quas nihil distinctio ratione suscipit minus earum libero, enim eum dolorum tempora nostrum laborum doloribus numquam fugit nisi non, minima recusandae placeat officiis. A adipisci perferendis necessitatibus eligendi, id autem consectetur architecto fuga similique et rem, voluptate nemo earum, itaque delectus omnis quaerat quisquam fugit. Veniam quia quam iure iste.
    """

    vegetables = ['Pumpkin', 'Tomato', 'Potato']
    return render(request, "home/index.html", context={'page':'Django Tutorial 2024', 'peoples':peoples, 'text':text, 'vegetables':vegetables})

def about(request):
    context = {'page':'About'}
    return render(request, "home/about.html", context)

def contact(request):
    context = {'page':'Contact'}
    return render(request, "home/contact.html", context)

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a Success Page</h1>")
