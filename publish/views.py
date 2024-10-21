from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.conf import settings
from urllib.parse import urlparse
from django.contrib import messages

from publish.models import *

def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
def index(request):
    context = {
        'homes': Home.objects.all()[:1],
    }
    return render(request, 'Base/index.html', context)

def about(request):
    context = {
        "aboutMe": About.objects.all()[:1],
        "skills": Experience.objects.all(),
    }
    return render(request, 'Base/about.html', context)

def contact(request):
    context = {
        'about': About.objects.all()[:1],
        'subjects': SubjectContact.objects.all()
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        subject_id = request.POST.get('subject')


        if subject_id is not "Other" and subject_id is not None:
            subject = get_object_or_404(SubjectContact, id=subject_id)
        elif subject_id == "Other":
            subject = request.POST.get('otherSubject')
        else:
            subject = None

        message = request.POST.get('message')
        Contact.objects.create(name=name, surname=surname, email=email, phone=phone, subject=subject, message=message)
        messages.info(request, 'Your message has been sent. Thank you ' + name + ' ' + surname + '!')
        return redirect('contact')
    return render(request, 'Base/contact.html', context)

def staff(request):
    return render(request, 'Base/staff.html')

def books(request):
    context = {
        'books': Books.objects.all()[:1],
        'book_images': Book_images.objects.all(),
    }
    return render(request, 'Service/books.html', context)

def skill(request):
    context = {
        'skills': Skills.objects.all()[:1],
    }
    return render(request, 'Service/skills.html', context)

def skill_page(request):
    context = {
        'skills': Skills.objects.all()[1:],
    }
    return render(request, 'Service/skill-page.html', context)

def portfolio(request):
    return render(request, 'Portfolio/portfolio.html')

def portfolio_detail(request):
    return render(request, 'Portfolio/protfolio-detail.html')

def service(request):
    return render(request, 'Service/service.html')

def membership(request):
    context = {
        'memberships': Membership.objects.all()
    }
    return render(request, 'Service/membership.html', context)

def trainingConsulting(request):
    context = {
        'trainingConsultings': TrainingConsulting.objects.all()
    }
    return render(request, 'Service/training-consulting.html', context)

def honoursAwards(request):
    context = {
        'honoursAwards': HonoursAwards.objects.all()
    }
    return render(request, 'Service/honoursAwards.html', context)

def blog(request):
    return render(request, 'Blog/blog.html')

def autism(request):
    context = {
        'autisms': Autism.objects.all()
    }
    return render(request, 'Blog/Autism.html', context)

def rare_diseases(request):
    context = {
        'rare_diseases': RareDiseases.objects.all()
    }
    return render(request, 'Blog/rare-diseases.html', context)

def blog_detail(request):
    return render(request, 'Blog/blog-detail.html')




