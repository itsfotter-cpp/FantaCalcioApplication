from django.urls import path
from .views import registrazioneView

urlpatterns = [
    path('registrazione/', registrazioneView, name='registration_view')
]
