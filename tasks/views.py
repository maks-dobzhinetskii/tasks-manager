import logging
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.db.models import F
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect

from tasks.models import Task
from tasks.forms import TaskForm


logger = logging.getLogger(__name__)


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    queryset = model.objects.order_by("-created_at").select_related("author")


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    form_class = TaskForm

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        queryset = Task.objects.filter(pk=pk).select_related("author")
        queryset.update(views=F("views") + 1)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("task_detail", kwargs={"pk": self.object.pk}))
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "body", "is_completed"]
    template_name = "tasks/task_edit.html"
    login_url = "login"

    def get_object(self, queryset=None):
        obj = super(TaskUpdateView, self).get_object(queryset)
        if self.request.user.is_superuser:
            return obj
        if obj.author != self.request.user:
            raise ValueError(
                "You are not the author of this post, so you cannot edit it"
            )
        return obj

    def form_valid(self, form):
        form.instance.updated_at = datetime.datetime.now()
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("task_list")
    login_url = "login"

    def get_object(self, queryset=None):
        obj = super(TaskDeleteView, self).get_object(queryset)
        if self.request.user.is_superuser:
            return obj
        if obj.author != self.request.user:
            raise ValueError(
                "You are not the author of this post, so you cannot delete it"
            )
        return obj


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/task_new.html"
    fields = ["title", "body", "execute_at"]
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.created_at = datetime.datetime.now()
        return super().form_valid(form)


def hello_reader(request):
    logger.warning(
        "Endpoint tasks/logger was accessed at "
        + str(datetime.datetime.now())
        + " hours!"
    )

    return HttpResponse("<h2>Custom logger</h2>")
