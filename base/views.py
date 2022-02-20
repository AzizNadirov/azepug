from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View
from .utils import search_by_upi




class LikeView(LoginRequiredMixin ,View):
    def post(self, request):
        #               value = <app_name's>'|'<value>
        # for example:  value = blogs|like
        app_name ,value = str(request.POST.get('value')).split('|')
        if app_name not in ['blogs', 'events', 'news', 'vacancies', 'questions']:
            raise ValueError(" Incorrect app name! ")
        postid = request.POST.get("postid")
        if value == "like":
            code = f"request.user.liked_{app_name}.add(postid)"
            eval(code)
        elif value == 'unlike':
            code = f"request.user.liked_{app_name}.remove(postid)"
            eval(code)
        return JsonResponse({'code': 200})
        

class SaveView(LoginRequiredMixin, View):
    def post(self, request):
        app_name ,value = str(request.POST.get('value')).split('|')
        if app_name not in ['blogs', 'events', 'news', 'vacancies', 'questions']:
            raise ValueError(" Incorrect app name! ")
        postid = request.POST.get("postid")
        if value == "save":
            code = f" request.user.treasure.{app_name}.add(postid)"
            eval(code)
        elif value == 'unsave':
            code = f" request.user.treasure.{app_name}.remove(postid)"
            eval(code)
        return JsonResponse({'code': 200})



class UpiView(View):
    def get(self, request, upi_code):
        post = search_by_upi(upi_code)
        if post:
            return redirect(post)
        else:
            return render(request, 'not_found.html')




