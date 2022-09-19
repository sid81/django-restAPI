from django.urls import path,include
from . import views

from .views import RegisterUser

urlpatterns = [
    path('',views.home,name='home'),
    path('task-list',views.tasklist,name='tasklist'),
    path('task-detail/<str:pk>',views.taskdetail,name='taskdetail'),
    path('task-create',views.taskCreate,name='taskCreate'),
    path('task-update/<str:pk>',views.taskUpdate,name='taskUpdate'),
    path('task-delete/<str:pk>',views.taskDelete,name='taskDelete'),
    path('resgister',RegisterUser.as_view()),
    
]