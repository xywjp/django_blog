from django.urls import path

from . import views
app_name = 'comments'

urlpatterns = [
    path('comment/<int:article_pk>', views.submit_comment, name='comment'),
]