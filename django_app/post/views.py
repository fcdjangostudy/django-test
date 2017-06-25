from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_modify(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('post:post_list')
    else:
        form = PostForm()

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post/post_modify.html', context)
