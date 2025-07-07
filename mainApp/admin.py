from django.contrib import admin
from .models import *
# Register your models here.

class PostImageAdmin(admin.StackedInline):
    model = CarImages
 
@admin.register(Cars)

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Cars
admin.site.register(Booking)
admin.site.register(Slides)
admin.site.register(Services)
admin.site.register(Staff)
admin.site.register(Testimonials)
admin.site.register(Cargo)