from django.contrib import admin

from .models import * 

class MenuExtraAdmin(admin.ModelAdmin):
    filter_horizontal = ("items" , "dishes")
    
    
admin.site.register(MenuDish)
admin.site.register(MenuItem)
admin.site.register(MenuExtra , MenuExtraAdmin)