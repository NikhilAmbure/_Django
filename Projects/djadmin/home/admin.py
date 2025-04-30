from django.contrib import admin
from .models import Customer, Order
from django import forms


# To customize the widgets of the form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'address' : forms.Textarea(attrs={'rows': 3})
        }
        # Mention this form in CustomerAdmin

# To create customer and Order at same time on a page
# Also there is StackedInline -> changes the UI
class OrderInline(admin.TabularInline):
    model = Order
    # try this extra 
    extra = 2

# Two ways to register
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    form = CustomerForm
    # Customize the panel
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "address"
    )

    # Search filter
    search_fields = ('first_name',
                     'phone_number',
                     'email',
                     'address')
    
    inlines = [OrderInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "order_date",
        "total_amount",
        "status"
    )
    
    # All about Search_filter :
    # foreign key
    search_fields = ['customer__first_name', 'customer__last_name']

    list_filter = ('status',)
    autocomplete_fields = ['customer']

    # exclude -> Cannot edit that field
    # exclude = ('total_amount',)

    # readonly_fields = ('total_amount', 'customer', 'status',)


    # Customizing actions
    actions = ["mark_as_shipped"]
    def mark_as_shipped(self, request, queryset):
        queryset.update(status = "Shipped")
    mark_as_shipped.short_description = 'Mark Selected As Shipped'


    