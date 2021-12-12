from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, ListView, DeleteView, UpdateView

from forum.models import Answer, Question
from .forms import QuestionCreateForm,  AnswerCreateForm, CommentForm


class QuestionCreateView(CreateView):
    form_class = QuestionCreateForm
    template_name = 'forum/question/create.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class AnswerCreateView(CreateView):
    form_class = AnswerCreateForm()
    template_name = 'forum/answer/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question = self.request.question
        return super().form_valid(form)

###-----------------------------------------------------------------------------

class QuestionListView(ListView):
    model = Question
    template_name = 'forum/question/list.html'
    paginate_by = 4
    context_object_name = 'questions'
    ordering = ['-date_created']


# class AnswerListView(ListView):
#     model = Answer
#     template_name = 'forum/answer/list.html'
#     # get_queryset = Question.objects.all("answers")
#     paginate_by = 4
#     context_object_name = 'answers'
#     ordering = ['-date_created']

##------------------------------------------------------------------------------
class QuestionDetailView(View):
    def post(self, request, pk):
        question = get_object_or_404(Question, id = pk)
        context = {'question':question}
        return render(request, 'forum/question/about.html', context)
    
    def get(self, request, pk):
        question = get_object_or_404(Question, id = pk)
        answers = question.answers.all()
        context = {'question':question, 'answers': answers}
        return render(request, 'forum/question/about.html', context)



class AnswerDetailView(View):
    def post(self, request, pk, a_pk):
        answer = get_object_or_404(Answer, id = a_pk)
        comments = answer.comments.filter(active = True)
        new_comment = None
        comment_form = CommentForm(data = request.POST, files=request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.answer = answer
            new_comment.author = request.user
            new_comment.save()
        comment_form = CommentForm()

        context = {'answer':answer,'comments':comments, 'comment_form':comment_form}
        return render(request, 'forum/answer/about.html', context)
    

    def get(self, request, pk, a_pk):
        answer = get_object_or_404(Answer, id = a_pk)
        comments = answer.comments.filter(active = True)
        new_comment = None
        comment_form = CommentForm()
        context = {'answer': answer,'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}
        return render(request, 'forum/answer/about.html', context)

##-------------------------------------------------------------------------------------------------

class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['title', 'body', 'tags']
    template_name = 'forum/question/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.author

class AnswerUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Answer
    fields = ['body']
    template_name = 'forum/answer/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        answer = self.get_object()
        return self.request.user == answer.author
##-----------------------------------------------------------------------------
class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Question
    template_name = 'forum/question/delete.html'
    success_url = '/forum'

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.author

class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Answer
    template_name = 'forum/answer/delete.html'
    success_url = '/forum'

    def test_func(self):
        answer = self.get_object()
        return self.request.user == answer.author