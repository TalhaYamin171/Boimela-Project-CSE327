from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Stall, Book
# Create your views here.


def home(request):
    return render(request, 'boimelawebApp/index.html')


def latest(request):
    book = Book.objects.all()
    return render(request, 'boimelawebApp/latestbook.html', {'books': book})


def navigation(request):
    return render(request, 'boimelawebApp/navigation.html')


class StallListView(LoginRequiredMixin, ListView):
    model = Stall
    template_name = 'boimelawebApp/dash.html'
    context_object_name = 'stalls'

    def get_queryset(self):
        return Stall.objects.filter(owner=self.request.user)


class StallDetailView(LoginRequiredMixin, DetailView):
    model = Stall


class StallCreateView(LoginRequiredMixin, CreateView):
    model = Stall
    fields = ['stall_name', 'stall_type']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class StallUpdateView(LoginRequiredMixin, UpdateView):
    model = Stall
    fields = ['stall_name', 'stall_type']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class StallDeleteView(LoginRequiredMixin, DeleteView):
    model = Stall
    success_url = '/dashboard'


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'boimelawebApp/dash.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['book_name', 'author', 'isbn', 'book_genre', 'release_date', 'stalls']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['book_name', 'author', 'isbn', 'book_genre', 'release_date', 'stalls']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/dashboard'


def searchposts(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(book_name__icontains=query) | Q(author__icontains=query)

            results = Book.objects.filter(lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'boimelawebApp/search.html', context)

        else:
            return render(request, 'boimelawebApp/search.html')

    else:
        return render(request, 'boimelawebApp/search.html')


# Create your views here.
