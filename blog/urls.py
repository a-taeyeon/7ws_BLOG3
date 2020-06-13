from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('delete/<int:blog_id>', views.delete, name="delete"),
    path('update/<int:blog_id>', views.update, name="update"),
  
    #url 한개만 써줘야함! 필요없는 url은 안써주기!!
    # path('createForm/', views.createForm, name='createForm'),
    # path('updateForm/<int:blog_id>/', views.updateForm, name='updateForm'),
]