from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # the request return a URLs
    return HttpResponse("Welcome to the Blog Home Page!")

def about(request, article_id):
    # article_id is a parametre from <int:article_id>
    return HttpResponse(f"Welcome to the Blog Article: {article_id}")

# --------------------------------

# from django.shortcuts import render, get_object_or_404
# from .models import Article

# def list_articles(request):
#     articles = Article.objects.all().order_by('-published_date')  
#     context = {
#         'articles': articles
#     }  
#     return render(request, 'blog/article_list.html', context)

# def article_detail(request, article_id):
#     article = get_object_or_404(Article, id=article_id)  
#     context = {
#         'article': article
#     }  
#     return render(request, 'blog/article_detail.html', context)

# --------------------------------
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    ordering = ['-published_date']
    paginate_by = 10  # 10 articles per page

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

# @login_required
# class ArticleCreateView(LoginRequiredMixin, CreateView):
#     model = Article
#     form_class = ArticleForm
#     template_name = 'blog/create_article.html'
#     success_url = '/article_list/'  # Redirect to article list after creation


#---------------------------------
@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Article created successfully!")
            return redirect('article_list')
    else:
        form = ArticleForm()
    
    return render(request, 'blog/create_article.html', {'form': form})


#---------------------------------
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate , logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('article_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "You have successfully logged out.")
    
    return render(request, 'registration/logout.html')
