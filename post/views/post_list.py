from django.shortcuts import render, get_object_or_404
from ..models.posts import Post
from taggit.models import Tag

def post_list(request, tag_slug=None):

    posts  = Post.objects.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    tags = Tag.objects.all()
    context = {'posts': posts, 'tag':tag, 'tags':tags}
    return render(request, 'index.html', context)
