from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=1000, verbose_name="Question")
    question_answer = models.CharField(max_length=1000, verbose_name="Answer")
    question_feedback = models.CharField(max_length=1000, verbose_name="Feedback")
    question_likes_count = models.IntegerField(default=0, verbose_name="Likes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('question-detail', args=[str(self.id)])