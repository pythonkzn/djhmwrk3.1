from django.contrib import admin
from .models import Phone, Prod


class ProdAdmin(admin.ModelAdmin):
    pass


class PhoneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Prod, ProdAdmin)
admin.site.register(Phone, PhoneAdmin)

