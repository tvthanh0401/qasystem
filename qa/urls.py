from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', views.QuestionListView.as_view(), name='questions'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('myquestions/', views.QuestionsAskedByUser.as_view(), name='my-questions'),
    path('signup/', views.signup, name='signup'),
    path('save/', views.save_question, name='save-question'),
    path('feedback/', views.save_feedback, name='save-feedback'),
    path('edit-profile/', views.ChangeInfoView.as_view(), name='edit-profile'),
    path('search/', views.search_question, name='search'),
]
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]