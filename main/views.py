from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import *
from django.views.generic import View
from django.urls import reverse

def main(request):
	space = Space.objects.filter(assign=request.user.id)
	if request.method == "POST":
		form_list = ListForm(request.POST)
		if form_list.is_valid():
			post = form_list.save()
			post.save()
			return redirect ('/')
	else:
		form_list = ListForm()

	if request.method == "POST":
		form_space = SpaceForm(request.POST)
		if form_space.is_valid():
			post = form_space.save()
			post.save()
			return redirect ('/')
	else:
		form_space = SpaceForm()
	return render(request, 'main/index.html', context = {'space':space, 'form_list': form_list, 'form_space': form_space})

    			

def task(request, list_id):
	space = Space.objects.filter(assign=request.user.id)
	lists = get_object_or_404(List, id=list_id)

	form_list = ListForm()
	form_space = SpaceForm()


	if request.method == "POST":
		task_form = TaskForm(request.POST or None)
		if task_form.is_valid():
			task = task_form.save()
			task.save()
			return redirect(reverse('task_url', args = (lists.id,)))
	else:
		task_form = TaskForm(initial = {'lists': lists})

	

	return render(request, 'main/task.html', context = {'lists':lists, 'space':space, 'form_list': form_list, 'form_space': form_space, 'task_form': task_form})



def subtask(request, task_id):
	space = Space.objects.filter(assign=request.user.id)
	task = get_object_or_404(Task, id=task_id)
	form_list = ListForm()
	form_space = SpaceForm()

	form = TaskForm(instance = task) #  instancе это и есть метод редактирование но оно не работает  я знаю из за чего . Ты думаю поймешь из за initial 

	forms = TaskForm(request.POST,instance = task)
	if form.is_valid():
		upd_task = form.save()
		return redirect(reverse('subtask_url', args = (task.id,)))


	if request.method == "POST":
		subtask_form = SubTaskForm(request.POST)
		if subtask_form.is_valid():

			post = subtask_form.save()
			post.save()
			return redirect(reverse('subtask_url', args = (task.id,)))
	else:
		subtask_form = SubTaskForm(initial = {'task': task})

	context = {
		'task':task,
		'subtask_form': subtask_form,
		'space':space, 
		'form_list': form_list, 
		'form_space': form_space,
		'form':form,
	}
	return render(request, 'main/subtask.html', context = context)

def SpaceDetail(request, space_id):
	space = get_object_or_404(Space, id=space_id)
	form_list = ListForm()
	form_space = SpaceForm()
	if request.method == 'POST':
		space.delete()
		return redirect(reverse('main'))

	return render(request, 'main/space_detail.html', context = {'space': space, 'form_list': form_list, 'form_space': form_space})


if __name__ == '__main__':
    	DEBAG = True
