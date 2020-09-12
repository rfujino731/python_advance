from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    #今回はデプロイしないので、publicに関する記述はいらないが、見本通りに記述する。
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'post': posts})
