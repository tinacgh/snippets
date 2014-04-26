# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.html import escape
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Snippet
from .forms import AddForm, SnippetModelForm

from datetime import datetime

def index(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        snippet_list = Snippet.objects.filter(description__icontains=q).\
            order_by('-date')
    else:
        snippet_list = Snippet.objects.order_by('-date')
    paginator = Paginator(snippet_list, 5)

    page = request.GET.get('page', 1)
    try:
        snippets = paginator.page(page)
    except PageNotAnInteger:
        snippets = paginator.page(1)
    except EmptyPage:
        snippets = paginator.page(paginator.num_pages)
    return render(request, 'snippets/index.html',
                  {'snippets': snippets, 'query': q})


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_snippet = Snippet(
                description=cd['description'],
                files=cd['files'],
                link=cd['link'],
                extra=cd['extra'],
                code=cd['code'])
            new_snippet.save()
            return HttpResponseRedirect(reverse('snippets:index'))
    else:
         form = AddForm()
    return render(request, 'snippets/add_form.html', {'form': form})

def delete(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    snippet.delete()
    return HttpResponseRedirect(reverse('snippets:index'))

def edit(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            snippet.description = cd['description']
            snippet.files = cd['files']
            snippet.link = cd['link']
            snippet.extra = cd['extra']
            snippet.code = cd['code']
            snippet.date = datetime.now()
            snippet.save()
            return HttpResponseRedirect(reverse('snippets:index'))
    form = SnippetModelForm(instance=snippet)
    return render(request, 'snippets/edit_form.html', {'form': form})
