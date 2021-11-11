from django.urls import path
from django.urls import path
from .views import *


urlpatterns = [
    path("heading/", HeadingListView.as_view())
]