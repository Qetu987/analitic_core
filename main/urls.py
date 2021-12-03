from django.urls import path
from .views import (
    HeadingListView,
    CategoryListView,
    TypeListView,
    BrandListView,
    Item_modelListView,
    OlxSetView,
    OlxResultView,
)


urlpatterns = [
    path("heading/", HeadingListView.as_view()),
    path('category/<int:item>', CategoryListView.as_view()),
    path('type/<int:item>', TypeListView.as_view()),
    path('brand/<int:item>', BrandListView.as_view()),
    path('item/<int:item>', Item_modelListView.as_view()),
    path('olx/', OlxSetView.as_view()),
    path('result/<int:item>', OlxResultView.as_view()),
]