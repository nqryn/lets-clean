from django.conf.urls import include, url
from django.contrib import admin
from main import views as main_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'assignment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^manager/cleaners/', include('cleaners.urls', namespace='cleaners')),
    url(r'^manager/customers/', include('customers.urls', namespace='customers')),
    url(r'^manager/cities/', include('cities.urls', namespace='cities')),
    url(r'^manager/bookings/', include('bookings.urls', namespace='bookings')),
    url(r'^manager/', main_views.home_manager),
    url(r'^$', main_views.home)
]
