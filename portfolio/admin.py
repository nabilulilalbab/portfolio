from django.contrib import admin
from .models import Profile,Project,Technology,Contact
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Technology)

admin.site.register(Contact)
# Register your models here.category = models.ForeignKey('GalleryCategory', on_delete=models.SET_NULL, null=True)

