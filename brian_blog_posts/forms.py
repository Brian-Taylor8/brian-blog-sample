from django import forms

from .models import BlogPost

class TopicForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['post_title', 'text']
		labels = {'text': ''}