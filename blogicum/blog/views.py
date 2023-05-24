from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index(request):
    template = "blog/index.html"
    current_time = timezone.now()
    post_list = (
        Post.objects.select_related(
            "category"
            ).filter(
                pub_date__lte=current_time,
                is_published=True,
                category__is_published=True
            ).order_by("-pub_date")[:5]
    )
    context = {"post_list": post_list}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    current_time = timezone.now()
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
        )
    post_list = Post.objects.select_related(
            "category"
            ).filter(
                category__slug=category_slug,
                is_published=True,
                pub_date__lte=current_time
            )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    current_time = timezone.now()
    post = get_object_or_404(
        Post,
        id=id,
        is_published=True,
        pub_date__lte=current_time,
        category__is_published=True
    )
    context = {'post': post}
    return render(request, template, context)
