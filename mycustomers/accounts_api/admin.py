from django.contrib import admin

# Register your models here.
from .models import Customers

class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "customer_name","customer_email" ]
    list_display_links = ["customer_name"]   
    list_filter = ["created_at", "updated_at"]
    search_fields = ["customer_name", "pk"]
    class Meta:
        model = Customers


admin.site.register(Customers, CustomerModelAdmin)