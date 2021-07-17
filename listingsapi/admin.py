from django.contrib import admin
from .models import Employees, Products, Company_Expense, Customers, Order_Product, Orders, ProductImage
# Register your models here.

class EmployeesAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self,request):
        get_data = super(EmployeesAdmin,self).get_changeform_initial_data(request)
        get_data['added_by'] = request.user.pk
        return get_data 
   
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Order_Product)
admin.site.register(Orders)
admin.site.register(ProductImage)
admin.site.register(Company_Expense)
