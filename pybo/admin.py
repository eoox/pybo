from django.contrib import admin

# Register your models here.
from .models import Inverter
from .models import Question
from .models import Answer

admin.site.register(Inverter)
admin.site.register(Question)
admin.site.register(Answer)

