from django.shortcuts import render
from django.db.models import Q

from seeds.models import Seeds
from user.models import Avatar


def index(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    seeds = Seeds.objects.all()
    context_dict.update({
        'seeds': seeds,
    })
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html"
    )


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}


def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    if request.GET['search_param']:
        search_param = request.GET['search_param']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        seeds = Seeds.objects.filter(query)
        context_dict.update({
            'seeds': seeds,
            'search_param': search_param,
        })
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html",
    )

def contacto(request):
    context_dict = {}
    return render(
        request=request,
        context=context_dict,
        template_name='home/contacto.html'
    )


def about(request):
    context_dict = {}
    return render(
        request=request,
        context=context_dict,
        template_name='home/about.html'
    )