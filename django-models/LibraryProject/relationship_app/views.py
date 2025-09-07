from django.shortcuts import render
from .models import Book
from .models import Library    
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

# Create your views here.
def list_books(request):
    """This view should render a simple text list of book titles and their authors."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

    
class LibraryDetailView(DetailView):
    """A class-based view rendering a template named 'hello.html'."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    


class register(CreateView):
    _ = UserCreationForm()
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'
    

