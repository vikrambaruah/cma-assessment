from django.urls import path
from main.views import Dashboard, IndexView
app_name='main'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    #path('download/', Download.as_view(), name='download'),
]