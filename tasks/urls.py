from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
    path("<int:pk>/edit/", views.TaskUpdateView.as_view(), name="task_edit"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task_delete"),
    path("new/", views.TaskCreateView.as_view(), name="task_new"),
    path("logger/", views.hello_reader, name="hello_reader"),
]
