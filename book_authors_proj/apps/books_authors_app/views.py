from django.shortcuts import render,HttpResponse,redirect
from apps.books_authors_app.models import *
from django.contrib import messages


def books(request):
    context={
        'books': Books.objects.all()
    }
    
    return render(request,"books_authors_app/books.html",context)

def newbook(request):
    context={
        "book": request.POST
    }

    errors = Books.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for error in errors:

            messages.error(request,errors[error])
        return(redirect('/'))

    Books.objects.create(title=context['book']['title'],desc=context['book']['description'])
    # print (context['book'])
    return redirect('/')

def book(request,id):
    
    book = Books.objects.get(id=id)
    authors = Authors.objects.exclude(id__in=book.authors.all())
    # print (authors)
    # for author in book.authors.all():
    #     authors = authors.exclude(id = author.id)
    
    # print(authors)
    context ={
        'book': book,
        'authors': authors
    }
    return render(request,'books_authors_app/book.html',context)

def addauthor(request):
    print(request.POST)
    context = {
        'book':Books.objects.get(id=request.POST['bookid']),
        'author':Authors.objects.get(id=request.POST['authorid']),
    }
    context['book'].authors.add(context['author'])
    return redirect('/book/'+str(context['book'].id))

def authors(request):
    context = {
        'authors': Authors.objects.all()
    }
    return render(request,'books_authors_app/authors.html',context)

def newauthor(request):
    context = {
        'fname': request.POST['first_name'],
        'lname': request.POST['last_name'],
        'notes': request.POST['notes'],

    }
    Authors.objects.create(first_name=context['fname'], last_name =context['lname'],notes=context['notes'])
    return redirect('/authors')

def author(request,id):
    context = {
        'author': Authors.objects.get(id=id),
        'books': Books.objects.all()
    }
    return render(request,'books_authors_app/author.html',context)

def addbook(request):
    context = {
        'book':Books.objects.get(id=request.POST['bookid']),
        'author':Authors.objects.get(id=request.POST['authorid']),
    }
    print(context['book'])
    print(context['author'])
    context['author'].books.add(context['book'])
    return redirect('/author/'+str(context['author'].id))