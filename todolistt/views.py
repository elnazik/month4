from django.shortcuts import render
from django.template.context_processors import request
from .models import Task, Category
from .forms import TaskFilterForm


class task_list_view(request):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_filter = self.request.GET.get('category')
        search_query = self.request.GET.get('search')

        if category_filter:
            queryset = queryset.filter(category_id=category_filter)

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset

class task_detail_view(request,):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

