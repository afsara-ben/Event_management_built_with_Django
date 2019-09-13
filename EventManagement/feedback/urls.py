from django.urls import include, path
from .views import feedback_form, service_feedback_form


urlpatterns = [
    path('', feedback_form, name='feedback_form'),
    path('service/', service_feedback_form, name='service_feedback_form'),
]

