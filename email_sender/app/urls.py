from django.urls import path

from app.views import MessageFormView, SuccessView

urlpatterns = [
    path('send_emails/', MessageFormView.as_view()),
    path('success/', SuccessView.as_view())
]
