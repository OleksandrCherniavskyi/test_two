from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import ArticleForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article



def index(request):
    return HttpResponseRedirect('/articles_list')



# Function-based views with login required decorator


def articles_list(request):
    articles = Article.objects.all().order_by('-created_at')  # Get all articles, ordered by creation date descending
    return render(request, 'articles/articles_list.html', {'articles': articles})


def article_detail(request, slug):  # Pass slug for unique article identification
    article = get_object_or_404(Article, slug=slug)  # Get article by slug or raise 404 error
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # Use ArticleForm for validation and data handling
        if form.is_valid():
            article = form.save(commit=False)  # Save without saving directly to avoid potential issues
            article.author = request.user  # Assign current user as author
            article.save()
            return redirect('articles_list')  # Redirect to articles list after successful creation
    else:
        form = ArticleForm()
    return render(request, 'articles/article_create.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

@login_required
def article_update(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.user != article.author:
        return redirect('articles_list')  # Redirect to articles list if not the author

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', slug=article.slug)  # Redirect to the updated article's detail page
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/article_update.html', {'form': form, 'article': article})

@login_required
def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.user != article.author:
        return redirect('articles_list')  # Redirect if not the author

    if request.method == 'POST':
        if request.user == article.author:
            article.delete()
            return redirect('articles_list')  # Redirect to articles list after successful deletion
        else:
            # Handle unauthorized deletion attempt
            message = "You are not authorized to delete this article."
            return render(request, 'articles/article_detail.html', {'article': article, 'error_message': message})

    return render(request, 'articles/article_detail.html', {'article': article})



class CustomLoginView(LoginView):
    template_name = 'articles/login.html'  # Specify your login template

    def get_success_url(self):
        return redirect('articles_list')  # Redirect to your desired view after successful login

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('articles_list')  # Redirect to articles list after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'articles/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'articles/register.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('articles_list')  # Redirect to the login page after logout

class CustomLogoutView(LogoutView):
    template_name = 'articles/logout.html'  # Specify your logout template

    def get_next_login_url(self):
        return reverse('login')  # Redirect to the login page after logout