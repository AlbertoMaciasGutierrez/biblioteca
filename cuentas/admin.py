from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
# Register your models here.


#Usuario = get_user_model()

admin.site.register(Usuario, UserAdmin)