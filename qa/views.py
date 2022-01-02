from django.shortcuts import render, redirect
from django.views import generic
from .models import Question
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')


class QuestionListView(generic.ListView):
    model = Question
    paginate_by = 10

class QuestionDetailView(generic.DetailView):
    model = Question

from django.contrib.auth.mixins import LoginRequiredMixin

class QuestionsAskedByUser(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Question
    template_name ='qa/questions_asked_by_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'qa/signup.html', {'form': form})

@csrf_exempt 
def save_question(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            question_text = json_data['question']
            question_answer = json_data['answer']
            print(json_data, question_answer)
            question_user = User.objects.filter(username=json_data['username']).first()
            question = Question(question_text=question_text, question_answer=question_answer, user=question_user)
            question.save()
            return JsonResponse({'question_id': question.id})
        except KeyError:
            print("Invalid format of json!!!")

@csrf_exempt 
def save_feedback(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        try:
            question_id = json_data['question_id']
            feedback_text = json_data['feedback']
            print(feedback_text)
            question = Question.objects.get(id=question_id)
            question.question_feedback = feedback_text
            question.save()
            return JsonResponse({'question_id': question.id})
        except KeyError:
            print("Invalid format of json!!!")

class ChangeInfoView(UpdateView):
    form_class = EditProfileForm
    template_name = 'qa/edit_profile.html'
    success_url = reverse_lazy('edit-profile')
    
    def get_object(self):
        return self.request.user

def search_question(request):
    if request.method == "POST":
        query_name = request.POST.get('query', None)
        if query_name:
            question_list = Question.objects.filter(question_text__contains=query_name)
            return render(request, 'qa/question_search.html', {"question_list": question_list})

    return render(request, 'qa/question_search.html')
