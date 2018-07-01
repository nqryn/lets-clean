from django.conf.urls import url

from .views import (
    CityList,
    CityDetail,
    CityCreation,
    CityUpdate,
    CityDelete
)

urlpatterns = [

    url(r'^$', CityList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', CityDetail.as_view(), name='detail'),
    url(r'^new$', CityCreation.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)$', CityUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', CityDelete.as_view(), name='delete'),

]