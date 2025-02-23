from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from app.forms import MessageForm


class MessageFormView(FormView):
    template_name = 'message.html'
    form_class = MessageForm
    success_url = '/success/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
    
class SuccessView(TemplateView):
    template_name = 'success.html'