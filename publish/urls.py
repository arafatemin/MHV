from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('staff/', staff, name='staff'),

    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio-detail/', portfolio_detail, name='portfolio-detail'),

    path('service/', service, name='service'),
    path('skill/', skill, name='skill'),
    path('skill-page/', skill_page, name='skill-page'),
    path('books/', books, name='books'),
    path('membership/', membership, name='membership'),
    path('honoursAwards/', honoursAwards, name='honoursAwards'),
    path('trainingConsulting/', trainingConsulting, name='trainingConsulting'),



    path('blog/', blog, name='blog'),
    path('autism/', autism, name='autism'),
    path('rare-diseases/', rare_diseases, name='rare-diseases'),
    path('blog-detail/', blog_detail, name='blog-detail'),

]
