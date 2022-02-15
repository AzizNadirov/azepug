from django.shortcuts import redirect, render
from django.views.generic import View
from .utils import search_by_upi




class UpiView(View):
    def get(self, request, upi_code):
        post = search_by_upi(upi_code)
        if post:
            return redirect(post)
        else:
            return render(request, 'not_found.html')




