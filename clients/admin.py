from django.contrib import admin
from .models import Client, Order


#Регистрация моделя
admin.site.register(Client)

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["name", "contacts", "created_at", "finished"]
    list_editable = ["contacts", "finished"]
    fields = ["name", "contacts", "create_at", "update_at", "description", "finished"]
    readonly_fields = ["created_at", "update_at"]

#регистрируем моделя каждый раз когда создаем
admin.site.register(Order, OrderAdmin)