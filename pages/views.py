from datetime import datetime
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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


@login_required(login_url='login')
def add_comment(request, pk):
    eachquestion = Question.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachquestion)
        if form.is_valid():
            name = request.user
            text = form.cleaned_data['text']
            data = Comment(question=eachquestion, user=name, text=text, created_at=datetime.now())
            data.save()
            return redirect('question')
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    return render(request, 'pages/add_comment.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    page_search = Question.objects.filter(Q(hashtag__icontains=query))

    return render(request, 'pages/search.html', {'search': page_search})


@login_required(login_url='login')
def LikeView(request, pk):
    like = get_object_or_404(Question, id=pk)
    like.likes.add(request.user)
    return HttpResponseRedirect('question')


def migration(request):
    import os
    os.system('python3 manage.py makemigrations')
    os.system('python3 manage.py migrate --no-input')
    return HttpResponse('Migration Done')
