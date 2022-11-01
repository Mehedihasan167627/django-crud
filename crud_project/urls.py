
from django.contrib import admin
from django.urls import path
from app.views import HomeView,DeleteStudent, SearchView, UpdateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",HomeView.as_view(),name="home"),
    path("delete-student/",DeleteStudent.as_view(),name="delete-student"),
    path("update-student/",UpdateView.as_view(),name="update-student"),
    path("search-student/",SearchView.as_view(),name="search-student"),
]
