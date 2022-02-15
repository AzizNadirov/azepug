from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect

from blog.models import Post
from events.models import Event
from news.models import News
from vacancy.models import Vacancy
from forum.models import Question



def get_top_n(n:int = 5):
    """
    returns a dict of top n posts from all apps

    """
    qsets = {}
    qsets['blogs'] = Post.objects.all().order_by('-date_created')[:n]
    qsets['events'] = Event.objects.all().order_by('-date_created')[:n]
    qsets['news'] = News.objects.all().order_by('-date_created')[:n]
    qsets['vacancies'] = Vacancy.objects.all().order_by('-date_created')[:n]
    qsets['questions'] = Question.objects.all().order_by('-date_created')[:n]

    return qsets


def get_object_or_none(model, pk):
    try:
        obj = model.objects.get(pk = pk)
        return obj
    except:
        return None


def search_in_apps(text:str, in_content = False):
    """
    takes string for searching and searchs in all app's
    models. Returns dict of querysets, where each of keys are 
    name of app and walues are the querysets.
    in_content makes including contents of posts also to 
    searching. 

    """

    def search_in(model):
        if not in_content:
            posts = model.objects.filter(title__icontains = text).order_by("-date_created")
        else:
            posts = model.objects.filter(Q(title__icontains = text) | Q(content__icontains = text)).order_by("-date_created")
        return posts


    apps = {'blogs':Post, 'events':Event, 'news': News, 'vacancies': Vacancy, 'questions': Question}
    qsets = {}
    for app_name in apps.keys():
        app_name = str(app_name)
        posts = search_in(apps[app_name])
        if posts:
            qsets[app_name] = posts

    return qsets






def search_by_upi(code_str:str):
    """"
        Takes code string as '<app><id_num>'
        and returns post with 'id_num' id of 
        'app' application's model.
        
        Abbrivations for apps:
        {'b':blog, 'e':events, 'fq': forum-question,'n': news, 'v': vacancy}

    """

    app_list = ['b', 'e', 'fa', 'fq', 'n', 'v']
    try:
        app = code_str[:code_str.index(':')]
        ID = code_str[code_str.index(':')+1 : ]
        if app not in app_list:
            post = None
        elif app == 'b':
            from blog.models import Post
            post = get_object_or_none(Post, pk = ID)

        elif app == 'e':
            from events.models import Event
            post = get_object_or_none(Event, pk = ID)
        
        elif app == 'fq':
            from forum.models import Question
            post = get_object_or_none(Question, pk = ID)

        elif app == 'n':
            from news.models import News
            post = get_object_or_none(News, pk = ID)

        elif app == 'v':
            from vacancy.models import Vacancy
            post = get_object_or_none(Vacancy, pk = ID)
    except ValueError:
        post = None
        
    return post



