from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Track, ImageGallery, Video_Gallery
from django.core.paginator import Paginator
from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
# Create your views here.

def index(request):
	tracks = Track.objects.all()
	gallery = ImageGallery.objects.all()
	videos = Video_Gallery.objects.all()
	paginator= Paginator(tracks, 2)
	page_number=request.GET.get('page')
	page_obj=paginator.get_page(page_number)

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact_name = form.cleaned_data['name']
			contact_email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			contact_message = f"{contact_name} has sent you a new message: " + f"{message}"
			email_msg = EmailMessage(
				subject=subject, body=contact_message, 
				from_email='dpsalmist546@gmail.com', 
				to=['dpsalmist546@gmail.com'],
				headers={'Reply-To': contact_email})
			email_msg.send()
			messages.success (request, f'Thank you for contacting us!.')
			return redirect('/')
	else:
		form = ContactForm()

	context = {
	'tracks':tracks,
	'gallery':gallery,
	'videos':videos,
	'page_obj':page_obj,
	'form': form,
	}

	return render(request, 'seyi_app/index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
        	contact_name = form.cleaned_data['name']
        	contact_email = form.cleaned_data['email']
        	subject = form.cleaned_data['subject']
        	contact_message = f"{contact_name} has sent you a new message ..."
        	email_msg = EmailMessage(
        		subject=subject, body=contact_message, 
        		from_email='dpsalmist546@gmail.com',  #your Zoho domain name(i createdan external email)
         		to=['dpsalmist546@gmail.com'],
        		headers={'Reply-To': contact_email})
        	email_msg.send()
        	messages.success (request, f'Thank you for contacting us!.')
        	return redirect('school-contact')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})
