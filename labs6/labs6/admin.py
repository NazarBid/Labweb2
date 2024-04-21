from django.contrib import admin
from .models import Agent,Property,Client,Request,CustomUser

admin.site.register(Agent)
admin.site.register(Property)
admin.site.register(Client)
admin.site.register(Request)
admin.site.register(CustomUser)