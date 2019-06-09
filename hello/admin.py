from django.contrib import admin
from .models import Friend, Message, place, purpose, urldata, suggest

admin.site.register(Friend)
admin.site.register(Message)
admin.site.register(place)
admin.site.register(purpose)
admin.site.register(urldata)
admin.site.register(suggest)
