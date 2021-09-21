from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('update/save', views.save, name='editing'),
]