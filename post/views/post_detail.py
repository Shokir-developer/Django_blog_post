from django.shortcuts import render
from ..models.posts import Post

def post_detail(request, slug=None):

    post = Post.objects.get(slug=slug)

    if 'Like' in request.POST:
        post.like_count +=1
        post.save()
    if 'Dislike' in request.POST:
        post.dislike_count += 1
        post.save()

    context = {'post':post}
    return render(request, 'detail.html', context)