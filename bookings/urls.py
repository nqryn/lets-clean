from django.conf.urls import url

from .views import BookingList, BookingCreateView

urlpatterns = [

    url(r'^$', BookingList.as_view(), name='list'),
    url(r'^new$', BookingCreateView.as_view(), name='new'),

]