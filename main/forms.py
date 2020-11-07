from django.forms import ModelForm, DateInput, TextInput
from .models import *
from django.contrib.auth.models import User

class SpaceForm(ModelForm):
	class Meta:
		model = Space
		fields = ('name', 'photo', 'assign', 'status', 'created_by', 'color')



class ListForm(ModelForm):
	class Meta:
		model = List
		fields = ('space','name_list',)

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ('lists','task_name', 'assign', 'dead_line', 'attachments', 'status', 'description', 'change_date', 'end_date', 'created_by')

		widgets = {
			'dead_line': DateInput(attrs={'type': 'date'}),
			'change_date':DateInput(attrs={'type': 'date'}),
			'end_date': DateInput(attrs={'type': 'date'}),
		}

class SubTaskForm(ModelForm):
	class Meta:
		model = SubTask
		fields = ('task','task_name', 'assign', 'dead_line', 'attachments', 'status', 'description', 'change_date', 'end_date', 'created_by')

		widgets = {
			'dead_line': DateInput(attrs={'type': 'date'}),
			'change_date':DateInput(attrs={'type': 'date'}),
			'end_date': DateInput(attrs={'type': 'date'}),
		}