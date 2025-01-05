from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import EmailValidator, URLValidator
from ckeditor.fields import RichTextField


class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)  # e.g., "Full Stack Developer"
    bio = RichTextField()
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)
    cv_file = models.FileField(upload_to='cv/', null=True, blank=True)
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)

    # Social Media Links
    linkedin = models.URLField(validators=[URLValidator()], blank=True)
    github = models.URLField(validators=[URLValidator()], blank=True)

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.full_name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    thumbnail = models.ImageField(upload_to='projects/')
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    created_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    technologies = models.ManyToManyField('Technology')

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class Technology(models.Model):
    name = models.CharField(max_length=50)
    icon = models.FileField(upload_to='technology_icons/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.name} - {self.subject}"