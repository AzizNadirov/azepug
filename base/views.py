from django.http import JsonResponse
from django.db.models.expressions import F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View
from .utils import search_by_upi, get_model_by_appname




class LikeView(LoginRequiredMixin ,View):
    print("\nLikeVyu is now\n")
    def increment_like(self, app_name, pk, decrement = False):
        """ like incerementer """
        post = get_model_by_appname(app_name).objects.get(pk = pk)
        if not decrement:
            print('\n-----Like Incrementer--------------\n')
            post.like_count = F('like_count') + 1
        else:
            print('\n-----Like Decrementer--------------\n')
            post.like_count = F('like_count') - 1
        post.save()
        post.refresh_from_db()

    def post(self, request):
        # value = <app_name>'|'<value>
        # for example:  value = blog|like
        app_name ,value = str(request.POST.get('value')).split('|')
        if app_name not in ['blog', 'event', 'news', 'vacancy']:
            raise ValueError(" Incorrect app name! ")
        postid = int(request.POST.get("postid"))
        if value == "like":
            code = f"request.user.liked_{app_name}.add(postid)"
            eval(code)
            self.increment_like(app_name, postid)
        elif value == 'unlike':
            code = f"request.user.liked_{app_name}.remove(postid)"
            eval(code)
            self.increment_like(app_name, postid, decrement = True)
        return JsonResponse({'code': 200})


class SupportView(LoginRequiredMixin ,View):
    def increment_support(self, app_name, pk, decrement = False):
        """ support incerementer """
        post = get_model_by_appname(app_name).objects.get(pk = pk)
        if not decrement:
            post.supports_count = F('supports_count') + 1
        else:
            post.supports_count = F('supports_count') - 1
        post.save()
        post.refresh_from_db()

    def post(self, request):
        #               value = <app_name>'|'<value>
        # for example:  value = blog|support
        app_name, value = str(request.POST.get('value')).split('|')
        if app_name not in ['question', 'answer']:
            raise ValueError(" Incorrect app name! ")
        postid = request.POST.get("postid")
        if value == "support":
            code = f"request.user.supported_{app_name}.add(postid)"
            eval(code)
            self.increment_support(app_name, postid)
        elif value == 'unsupport':
            code = f"request.user.supported_{app_name}.remove(postid)"
            eval(code)
            self.increment_support(app_name, postid, decrement = True)
        return JsonResponse({'code': 200})
        

class SaveView(LoginRequiredMixin, View):
    def post(self, request):
        app_name ,value = str(request.POST.get('value')).split('|')
        if app_name not in ['blog', 'event', 'news', 'vacancy', 'question']:
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




