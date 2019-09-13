from django.urls import include, path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', vendor_view, name='vendor_upload'),
    path('profile_success/', vendor_success, name='vendor_success'),
    path('edit/', edit_post, name='edit_post_vendor'),
    path('contact/', vendor_contact, name='vendor_contact'),
    path('contact_success/', vendor_contact_success, name='vendor_contact_success'),
    path('preference/', preference_view, name='vendor_preference'),
    path('myPreference', preference_success, name='vendor_preference_success'),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

