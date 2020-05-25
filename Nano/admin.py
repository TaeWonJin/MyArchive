from django.contrib import admin
from .models import WordDict,WordImg,Summary,SummaryImg,Solution

admin.site.register(WordDict)
admin.site.register(WordImg)
admin.site.register(Summary)
admin.site.register(SummaryImg)
admin.site.register(Solution)
# Register your models here.
