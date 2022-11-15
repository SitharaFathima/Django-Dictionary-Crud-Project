from dictionary import views
from django.urls import path

app_name = "dictionary"

urlpatterns = [
    path('',views.index, name="index"),
    path('add_word/', views.create_word, name="create_word"),
]
