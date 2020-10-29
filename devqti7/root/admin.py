from django.contrib import admin
# from .models import user

# # Register your models here.


# @admin.register(user)
# class userAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'email', 'password')


from root.models import user


@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
