from django.urls import include, path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', agency_view, name='agency_upload'),
    path('preference/', preference_view, name='agency_preference'),
    path('myPreference', preference_success, name='agency_preference_success'),
    path('contact/', agency_contact, name='agency_contact'),
    # path('contact/<int:pk>/', agency_contact, name='agency_contact'),
    path('profile_success/', agency_success, name='agency_success'),
    path('contact_success/', agency_contact_success, name='agency_contact_success'),
    path('edit/', edit_post, name='edit_post'),
    path('contact/edit/', edit_post_contact, name='edit_post_contact'),
    path('clientlist/', clientlist_view, name='clientlist'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
