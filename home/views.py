from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from base.forms import SearchForm
from base.utils import search_global




class HomeView(View):
    def post(self, request):
        search_form = SearchForm(request.POST)
        data = {'form': SearchForm()}
        if search_form.is_valid():
            text = search_form.cleaned_data['text']
            if text[0] == '#':
                post = search_global(text[1:])  # pass after # part of query for getting result
                if post:
                    return redirect(post)
                else:
                    return render(request, 'not_found.html', data)
            else:
                pass # do searching
    def get(self, request):
        search_form = SearchForm()
        data = {'form' : search_form}
        return render(request, 'home/home_page.html', context=data)

