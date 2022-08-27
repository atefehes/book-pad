from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, StatusForm

from .models import Book, Note

# Create your views here.


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('library')

    return render(request, 'notes/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('library')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('library')

    context = {'form': form, 'page': page}
    return render(request, 'notes/login_register.html', context)


def library(request):
    books = Book.objects.all()
    return render(request, 'notes/library.html', {'books':books})


def bookDetail(request, slug):
    book = Book.objects.get(slug=slug)
    context = {'book':book}
    if request.user.is_active:

        notes = Note.objects.filter(book=book, user=request.user)
        context['notes'] = notes
        context['form'] = StatusForm
        if request.method == 'POST':
            data = request.POST
            if data['status'] != 'none':
                book.status = data['status']
                book.save()
            return redirect('book', slug=book.slug)

    return render(request, 'notes/book.html', context)


@login_required
def addNote(request, slug):
    user = request.user
    book = Book.objects.get(slug=slug)

    if request.method == 'POST':
        data = request.POST
        Note.objects.create(
                user=user,
                text=data['text'],
                book=book,
            )

        return redirect('book', slug=book.slug)

    return render(request, 'notes/add_note.html')

@login_required
def myNotes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/my_notes.html', {'notes':notes})

@login_required
def myBooks(request):
    books = Book.objects.filter(status='1')
    return render(request, 'notes/my_books.html', {'books':books})