from django.contrib import admin
from .models import Student_Details, Emotional_Intelligence, Intellectual_Capacity, Personal_Test, Meta_Cognitive_Test

# Register your models here.
admin.site.register(Student_Details)
admin.site.register(Emotional_Intelligence)
admin.site.register(Intellectual_Capacity)
admin.site.register(Personal_Test)
admin.site.register(Meta_Cognitive_Test)