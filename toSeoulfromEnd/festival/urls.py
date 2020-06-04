from django.urls import path,include
from . import views

urlpatterns = [
    path('home', views.festival_home, name = "festival_home"),
    path('writing', views.writing, name = "writing"),
    path('detail/<int:festival_id>',views.detail, name = "detail"),
    path('delete/<int:festival_id>', views.delete, name = "delete"),
    path('edit/<int:festival_id>', views.edit, name = 'edit'),
    path('update/<int:festival_id>', views.update, name = 'update'),
    # path('likes/<int:festival_id>', views.like, name = 'like'),
]