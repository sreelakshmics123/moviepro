
from django.urls import path
from app import views
app_name="app"
urlpatterns = [

    #path('',views.home,name="home"),
    path('',views.MovieList.as_view(),name="home"),
    #path('details/<p>',views.details,name="details"),
    path('m/<pk>',views.MovieDetail.as_view(),name="details"),
    path('addmovie',views.MovieAdd.as_view(),name="addmovie"),
    #path('update/<p>',views.update,name="update"),
    path('update/<pk>',views.Movieupdate.as_view(),name="update"),
    path('delete/<pk>',views.Moviedelete.as_view(),name="delete"),
    #path('delete/<p>',views.delete,name="delete"),
]