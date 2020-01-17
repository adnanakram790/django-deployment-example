from django.urls import path
from myapp import views
urlpatterns = [
    path ('index', views.index, name='index'),
    path ('signup', views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('otherfile',views.otherfile, name='otherfile'),
    path('base',views.base, name='base'),
    path('about',views.about, name='about'),
    

    #exercise
    # path ('facebook', views.facebook, name='facebook'),
    # path ('youtube', views.youtube, name='youtube'),
    # path ('instagram', views.instagram, name='instagram'),
]
