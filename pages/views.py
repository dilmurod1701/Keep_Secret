from datetime import datetime
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView

from .models import Question, Comment
from .forms import QuestionForm, CommentForm

# Create your views here.


@login_required(login_url='login')
def all_questions(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'pages/quest.html', {'questions': questions})


class DetailQuestion(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'pages/detail.html'
    context_object_name = 'question'


class CreateQuestion(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'pages/posts.html'
    success_url = 'ques'
    login_url = 'login'
