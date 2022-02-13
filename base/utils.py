from xml.etree.ElementInclude import include
from django.shortcuts import get_object_or_404, redirect



def get_object_or_none(model, pk):
    try:
        obj = model.objects.get(id = pk)
        return obj
    except:
        return None





def search_global(code_str:str):
    """"
        Takes code string as '<app><id_num>'
        and returns post with 'id_num' id of 
        'app' application's model.
        
        Abbrivations for apps:
        {'b':blog, 'e':events, 'f-a':forum-answer, 'f-q': forum-question,'n': news, 'v': vacancy}

    """

    app_list = ['b', 'e', 'f-a', 'f-q', 'n', 'v']
    app = code_str[0]
    ID = code_str[1:]
    if app not in app_list:
        post = None
    elif app == 'b':
        from blog.models import Post
        post = get_object_or_none(Post, pk = ID)

    elif app == 'e':
        from events.models import Event
        post = get_object_or_none(Event, pk = ID)
     
    elif app == 'f-a':
        from forum.models import Answer
        post = get_object_or_none(Answer, pk = ID)
  
    elif app == 'f-q':
        from forum.models import Question
        post = get_object_or_none(Question, pk = ID)

    elif app == 'n':
        from news.models import News
        post = get_object_or_none(News, pk = ID)

    elif app == 'v':
        from vacancy.models import Vacancy
        post = get_object_or_none(Vacancy, pk = ID)
    
    return post


