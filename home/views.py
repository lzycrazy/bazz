from django.shortcuts import render
from .models import Post,Table,Contact,Singup,Record,blog
from django.contrib import messages


# Create your views here.



def home(request):
    sager = Post.objects.all()
    tab = Table.objects.all()
    sonu = Record.objects.all()
    deep = blog.objects.all()

    if request.method =="POST":
        email = request.POST['email']
        new_singup = Singup()
        new_singup.email = email
        new_singup.save()

    context = {
        'sug': sager,
        'read':tab,
        'pol' :sonu,
        'sag':deep,

    }
    return render(request,'index.html',context)




def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, f'Your Message has been sand.')
    context = {'contact':'active'}    

    return render(request,'contact.html', context)
    
   

        

    



def about(request):
    return render(request,'about.html')


def terms(request):
    return render(request,'terms.html')


def police(request):
    return render(request,'privic.html')


def desclimer(request):
    return render(request,'desclimer.html')    