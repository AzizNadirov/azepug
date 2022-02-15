from django.shortcuts import redirect, render
from django.views.generic import View
from base.forms import SearchForm
from base.utils import search_by_upi, search_in_apps, get_top_n



class HomeView(View):
    def post(self, request):
        search_form = SearchForm(request.POST)
        data = {'form': SearchForm()}
        if search_form.is_valid():
            text = search_form.cleaned_data['text']
            if text[0] == '#':                  #       search by UPI
                post = search_by_upi(text[1:])  #       pass after `#` part of query for getting result
                if post:
                    return redirect(post)
                else:
                    return render(request, 'not_found.html', data)
            else:  
                if request.POST.get('in_context'):
                    qsets = search_in_apps(text, in_content = True)              # do ordinary search
                else: qsets = search_in_apps(text)
                return render(request, 'home/search_results.html', {'qsets':qsets, 'text': text})

    def get(self, request):
        search_form = SearchForm()
        qsets = get_top_n()


        data = {'form' : search_form, 'qsets':qsets}
        return render(request, 'home/home_page.html', context=data)

