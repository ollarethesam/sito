from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    form = ContactForm
    return render(request, 'show/index.html', {'form': form})

def success_view(request):
    form = ContactForm
    return render(request, 'show/success-msg.html', {'form': form})

def contact(request):
    form = ContactForm
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            html_message = render_to_string('show/email.html', {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
            })
            subject = form.cleaned_data['object']
            from_email = 'provaemailsito@gmail.com'
            recipient_list = ['provaemailsito@gmail.com']
            email = EmailMessage(subject, '', from_email, recipient_list)
            email.content_subtype = 'html'
            email.body = html_message  # Set the HTML content as the email body

            email.send()
        return redirect('success')
    else:
        return render(request, 'show/index.html', {'form': form})