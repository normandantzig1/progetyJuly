from django.urls import path

from . import views

urlpatterns = [
  #  path('index', views.index, name='index'), #index used to look like ('', views.index, name='index')
#search page / home
    #term page
    path('', views.home, name='home'), # home 
    #progety/term/someTerm
    path('<term>/', views.term, name='term'), # the term

]







