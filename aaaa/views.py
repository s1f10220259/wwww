from django.http import HttpResponse
from django.utils import timezone
from aaaa.models import Article
from django.http import Http404
# Create your views here.
from django.shortcuts import render, redirect
from .models import Article  # Ensure you have imported the Article model from your models.py

from django.shortcuts import redirect
def index(request):
    if request.method == "POST":
        article = Article(title=request.POST.get('title'), body=request.POST.get('text'))
        article.save()
        return redirect('aaaa:detail', article_id=article.id)  # 名前空間を含めた形に修正
    context = {
        "articles": Article.objects.all()
    }
    return render(request, 'blog/index2.html', context)

def hello(request):
	data = {
		'name':'alice',
		'weather':'cloudy',
		'fortune':'well'
	}
	return render(request,'blog/hellow.html',data)

def redirect_test(request):
	return redirect(hello)

def detail(request,article_id):
	try:
		article = Article.objects.get(pk = article_id)
	except Article.DoesNotExist:
		raise Http404("指定された記事は存在しません")
	context = {"article":article}
	return render(request,"blog/detail2.html",context)
	#return render(request,"blog/detail2.html",context)


def update(request,article_id):
	try:
		article = Article.objects.get(pk = article_id)
	except Article.DoesNotExist:
		raise Http404("指定された記事は存在しません")
	if request.method == 'POST':
		article.title = request.POST['title']
		article.body = request.POST['text']
		article.save()
		return redirect('aaaa:detail', article_id=article.id)
	context = {
		"article":article
	}
	return render(request,"blog/edit.html",context)

def delete(request,article_id):
	try:
		article = Article.objects.get(pk = article_id)
	except Article.DoesNotExist:
		raise Http404("指定された記事は存在しません")
	article.delete()
	return redirect("aaaa:index")



def index2(request):
    context = {
        "articles": Article.objects.all()
    }
    return render(request, 'blog/list.html', context)

def ques(request):
    return render(request, 'blog/ques.html')

###############################
from django.shortcuts import render, redirect,get_object_or_404
from .models import Article, Comment
from .forms import CommentForm

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comments.all()  # 関連するコメントを取得

    if request.method == 'POST':
        form = CommentForm(request.POST)  # request.POSTはエラーの原因のようですので削除しても問題ありません
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('aaaa:detail', article_id=article.id)
    else:
        form = CommentForm()

    return render(request, 'blog/detail2.html', {
        'article': article,
        'form': form,
        'comments': comments,  # コメントをコンテキストに追加
    })