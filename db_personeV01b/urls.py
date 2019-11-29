from django.conf.urls import url
from db_personeV01b.apps.welcome.views import index

urlpatterns = [
    url('^$', index)
]
