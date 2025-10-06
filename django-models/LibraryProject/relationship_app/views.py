from django.shortcuts import render
from .models import Book
from .models import Library    
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator



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
    

#Helper function
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')