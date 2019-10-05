from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('single_point_map/<str:lat>/<str:long>/', views.single_point_map, name='single_point_map'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]