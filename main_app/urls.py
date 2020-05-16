from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('view/<int:widget_id>', views.view, name="view"),
    path('delete/<int:widget_id>', views.delete, name="delete"),
    
]