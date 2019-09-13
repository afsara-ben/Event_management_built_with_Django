from django.urls import include, path

from .views import client, agency, reg_group, vendor
from imageapp.views import image_view, success
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', reg_group.home, name='home'),

    path('client/', include(([
                                 path('', client.QuizListView.as_view(), name='client_profile'),
                             ], 'reg_group'), namespace='client')),

    path('agency/', include(([
                                 path('', agency.QuizListView.as_view(), name='agency_profile'),
                                 path('map/', agency.MapView.as_view(), name='google_map'),
                             ], 'reg_group'), namespace='agency')),

    path('vendor/', include(([
                                 path('', vendor.QuizListView.as_view(), name='vendor_profile'),
                             ], 'reg_group'), namespace='vendor')),

    path('agency/profile/', include('agency.urls')),
    path('agency/payment/', include('transaction.urls')),
    path('vendor/payment/', include('transaction.urls')),
    path('vendor/profile/', include('vendor.urls')),
    path('client/profile/', include('client.urls')),
    path('agency/image_upload/', include('imageapp.urls')),
    path('vendor/image_upload/', include('imageapp.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
