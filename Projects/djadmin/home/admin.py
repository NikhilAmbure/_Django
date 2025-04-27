from django.contrib import admin
from home.models import Customer, Order

# Register your models here.

@admin.register(Customer)
# TO customize 
class CustomerAdmin(admin.ModelAdmin):
    # To display the details in table format
    list_display=(
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "address"
    )


admin.site.register(Order)
# OR also can be register as
# admin.site.register(Customer)