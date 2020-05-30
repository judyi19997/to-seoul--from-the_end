"""toSeoulfromEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import review.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', review.views.review,name='review'),
    path('review/<int:review_id>', review.views.review_detail,name='review_detail'),
    path('review/new', review.views.review_new,name='review_new'),
    path('review/create', review.views.review_create,name='review_create'),
    path('review/edit/<int:review_id>', review.views.review_edit,name='review_edit'),
    path('review/update/<int:review_id>', review.views.review_update,name='review_update'),
    path('review/delete/<int:review_id>', review.views.review_delete,name='review_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
