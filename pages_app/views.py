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


def gallery(request):
    return render(request, 'pages_app/gallery.html')


def service(request):
    return render(request, 'pages_app/service.html')



def contactus(request):
    form = ContactUsForm()
    if request.method == 'POST':
            form = ContactUsForm(request.POST)
        # if form.is_valid():
            # print(request.POST)
            subject = request.POST.get("subject", "")
            message = request.POST.get("message", "")
            from_email = request.POST.get("from_email", "")
            if subject and message and from_email:
                try:
                    send_mail(subject,message,from_email,["developer.web.dj@gmail.com"])
                    form = ContactUsForm()
                    return redirect('pages_app:index')
                
                except BadHeaderError:
                    return HttpResponse("Invalid header found.")
            else:
                form = ContactUsForm()
                return HttpResponse("Make sure all fields are entered and valid.")
            
                
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']
            # from_email = form.cleaned_data['mayalsanea2014@gmail.com']
            
            # send_mail(subject,from_email,message,[''])
            # print(send_mail(subject,from_email,message,['mayalsanea2014@gmail.com']))
            # messages.success(request,'thanks you are successfully send email to us :)')
            # form = ContactUsForm()
            # return redirect('pages_app:index')
    
    

    context = {
        'title': 'Contact Us',
        'form' : form,
    }
    return render(request, 'pages_app/contactus.html', context)




# def contactus(request):
#     if request.method == 'POST':
#         form = ContactUsForm(request.POST)
#         if form.is_valid():
#             # print(request.POST)
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject,from_email,message,['mayalsanea2014@gmail.com'])
#                 messages.success(request,'thanks you are successfully send email to us :)')
#                 form = ContactUsForm()
#                 return redirect('pages_app:index')
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
            
#             # full_name = form.cleaned_data['full_name'] ---field not work
#             # Mobile_num = form.cleaned_data['Mobile_num'] -- fied not work
#             # send_mail(subject, full_name, from_email, Mobile_num,message, ['mayalsanea2014@gmail.com'])notwork
#             # return redirect('pages_app:success_contactus')
            
            
#     else:
#         form = ContactUsForm()
#         # messages.warning(request,'There some error , please try contact us again')--not work good
    
#     context = {
#         'form': form,
#     }
#     return render(request, 'pages_app/contactus.html', context)
    






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

    
    
