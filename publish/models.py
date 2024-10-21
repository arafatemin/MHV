from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe


class Experience(models.Model):
    about = models.ForeignKey('About', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    isActive = models.BooleanField(default=True, blank=True, null=True)
    startedDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    github = models.CharField(max_length=200, blank=True, null=True)
    description1 = RichTextField(blank=True, null=True)
    description2 = RichTextField(blank=True, null=True)
    description3 = RichTextField(blank=True, null=True)
    sub_description1 = RichTextField(blank=True, null=True)
    sub_description2 = RichTextField(blank=True, null=True)
    startedDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Home(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)



    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    comment = RichTextField(blank=True, null=True)
    message = RichTextField(blank=True, null=True)
    sub_message = RichTextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    sub_description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    image1 = models.ImageField(upload_to='media/', blank=True, null=True)


    def __str__(self):
        return self.name



class SubjectContact(models.Model):
    subject = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.subject


class Contact(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    subject = models.ForeignKey(SubjectContact, on_delete=models.CASCADE, blank=True, null=True)
    otherSubject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name







class Autism(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200, blank=True, null=True)
    finance = models.CharField(max_length=200, blank=True, null=True)
    startedDate = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.title

class RareDiseases(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200, blank=True, null=True)
    finance = models.CharField(max_length=200, blank=True, null=True)
    startedDate = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.title

class Book_images(models.Model):
    url = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.url

class Books(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title



class Membership(models.Model):
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.description


class TrainingConsulting(models.Model):
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.description


class HonoursAwards(models.Model):
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.description