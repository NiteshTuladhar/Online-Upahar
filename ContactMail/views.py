from django.shortcuts import render, redirect
from .mail import CustomMail
from django.contrib import messages

# Create your views here.
def contactpage(request):
	return render(request,'contact.html')

def mailsend(request):
    if request.method == 'POST':
        hostemail = 'sushek69@gmail.com'
        name = request.POST.get('name')
        email = request.POST.get('email')
        subjects = request.POST.get('subject')
        number = request.POST.get('phone')
        textmessage = request.POST.get('message')
        mail = CustomMail('mail/email_template.html', 'From Website Mail Notification', [hostemail,], nameofcustomer=name, numberofcustomer=number, messageofcustomer=textmessage, emailofcustomer=email, subjects=subjects)
        mail.push()
        messages.success(request, message="Mail sent successfully")
        return render(request, 'Store:homepage')

    else:
        messages.error(request, message="Sorry couldn't send mail")
        return redirect('ContactMail:contactpage')