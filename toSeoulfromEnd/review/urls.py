from django.urls import path
from . import views

urlpatterns = [
    path('', views.review,name='review'),
    path('<int:review_id>', views.review_detail,name='review_detail'),
    path('new', views.review_new,name='review_new'),
    path('create', views.review_create,name='review_create'),
    path('edit/<int:review_id>', views.review_edit,name='review_edit'),
    path('update/<int:review_id>', views.review_update,name='review_update'),
    path('delete/<int:review_id>', views.review_delete,name='review_delete'),
] 
