from django import forms

from app.tasks import send_email_task


class MessageForm(forms.Form):
    subject = forms.CharField(max_length=200, label='Тема сообщения')
    email = forms.EmailField(label="Email")
    message = forms.CharField(
        label="Cообщение", widget=forms.Textarea()
    )

    def send_email(self):
        send_email_task.delay(
            self.data['subject'],
            self.data['message'],
            self.data['email'])
