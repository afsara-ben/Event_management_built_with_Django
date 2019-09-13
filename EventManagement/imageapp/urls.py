from django.urls import include, path
from .views import image_view, success, design_view, design_work, vendor_image_view, vendor_design_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', image_view, name='image_upload'),
    path('images/', vendor_image_view, name='vendor_image_upload'),
    path('design', design_view, name='design_upload'),
    path('vendordesign', vendor_design_view, name='vendor_design_upload'),
    path('success/', success, name='success'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

