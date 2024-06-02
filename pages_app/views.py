from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from.forms import ContactUsForm

# Create your views here.
def index( request):
    return render(request,'pages_app/index.html')


def about(request):
    return render(request, 'pages_app/about.html')

def commerical(request):
    return render(request, 'pages_app/commerical.html')

def gallery(request):
    return render(request, 'pages_app/gallery.html')


def service(request):
    return render(request, 'pages_app/service.html')




def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd["subject"]
            # print(subject)
            message = cd["message"]
            # print(message)
            from_email = cd["from_email"]
            msg_sender = str(message) + " " + str(from_email)
            message = msg_sender
            # print(from_email)
            recipient_list = ["developer.web.dj@gmail.com"]
            send_mail(subject,message,from_email,recipient_list,fail_silently=False)
        
            # You might want to add a success message or redirect to a thank you page
            messages.success(request,f'Thank you, your message sent successfully to us.')
            return redirect('pages_app:index')
    else:
        form = ContactUsForm()

    context = {
        'title': 'Contact Us',
        'form' : form,
    }
    return render(request, 'pages_app/contactus.html', context)





def success_contactus(request):
    return render(request, 'pages_app/contactus.html')
    # return HttpResponse('Success! Thank you for your message.')


def under_construction(request):
    return render(request, 'pages_app/under_construction.html')
   


# from book 
# def contactView(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "email.html", {'form': form})


# def successView(request):
#     return HttpResponse('Success! Thank you for your message.')

    
    
