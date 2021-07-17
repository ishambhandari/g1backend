from rest_framework import serializers 
from .models import Employees, Products, Customers, Orders, Order_Product,  ProductImage, Company_Expense
from login.models import UserAccount
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source = 'customer_id.name', read_only = True)
    class Meta:
        model = Orders 
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers 
        fields = "__all__"


class Order_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Product
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Expense 
        fields = "__all__" 
    
        

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
