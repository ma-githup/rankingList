
from django.urls import path
from . import views
urlpatterns = [
    path('addcli/',views.AddServer.as_view()),
    path('showcli/',views.ShowRank.as_view()),
]
