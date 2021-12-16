from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, ListView,UpdateView, DeleteView, View

from events.models import Event
from .forms import CommentForm, EventCreateForm




class EventCreateView(LoginRequiredMixin,CreateView):
    form_class = EventCreateForm
    template_name = 'events/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventListView(ListView):
    model = Event
    template_name = 'events/list.html'
    paginate_by = 4
    context_object_name = 'events'
    ordering = ['-date_created']



class EventDetailView(View):
    def post(self, request, pk):
        event = get_object_or_404(Event, id = pk)
        comments = event.e_comments.filter(active = True)
        new_comment = None
        comment_form = CommentForm(data = request.POST, files=request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.event = event
            new_comment.author = request.user
            new_comment.save()
            comment_form = CommentForm()
        else:
            comment_form = CommentForm()

        context = {'event':event,'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}
        return render(request, 'events/detail.html', context)
    

    def get(self, request, pk):
        event = get_object_or_404(Event, id = pk)
        comments = event.e_comments.filter(active = True)
        new_comment = None
        comment_form = CommentForm()
        context = {'event':event,'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}
        return render(request, 'events/detail.html', context)


class EventUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'organiser', 'desc', 'starts_at', 'ends_at', 'tags']
    template_name = 'events/createt.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.author



class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Event
    template_name = 'events/deletet.html'
    success_url = '/events'

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.author