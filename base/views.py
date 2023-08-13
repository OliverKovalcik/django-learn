from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.


def home(request):
    return render(request, 'home.html')

def articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'list.html', context)

def createArticle(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
    context = {'form': form}
    return render(request, 'article_form.html', context)