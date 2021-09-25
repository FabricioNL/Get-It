from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('update/save', views.save, name='editing'),
    path('tags', views.tags, name='all-tags'),
    path('tags/Home', views.goHome, name="tag-home"),
    path('/Home', views.goHome, name="tag-home"), 
    path('tags/<str:name>', views.tagVisualization, name="Tag-notes"),
]