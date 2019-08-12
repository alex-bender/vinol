from django.contrib import admin
from labs.models import Activity, Client, Order


class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ActivityInline
    ]


class ClientAdmin(admin.ModelAdmin):
    pass


class ActivityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
