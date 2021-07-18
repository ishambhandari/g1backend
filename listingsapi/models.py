from django.db import models
# from django.contrib.auth import get_user_model 
from django.conf import settings
from login.models import UserAccount
from datetime import datetime
class Employees(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 100)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=254, unique=True)
    designation = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    accountName = models.CharField(max_length = 200, blank = True)
    accountNumber = models.CharField(max_length = 200,  blank = True)
    salary = models.PositiveIntegerField(blank = True)
    # added_by = models.ForeignKey(User, on_delete= models.DO_NOTHING )

    def __str__(self):
        return self.name


class Customers(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length =100)
    phone = models.PositiveBigIntegerField()
    location = models.CharField(max_length = 200) 

    def __str__(self):
        return str(self.name)

class Products(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100,  unique=True)
    description = models.TextField(blank = True)
    stock_100 = models.PositiveIntegerField(default=0)
    stock_500 = models.PositiveIntegerField(default = 0)
    stock_1000 = models.PositiveIntegerField(default=0)
    price_100 = models.PositiveIntegerField(default = 0)
    price_500 = models.PositiveIntegerField(default = 0)
    price_1000 = models.PositiveIntegerField(default = 0)
    # product_image = models.ImageField(upload_to = 'photos)
    # product_image_2 = models.ImageField(upload_to = 'photos' blank = True)


    def __str__(self):
        return self.name



# CHOICES FOR ORDERS
# 
class PaymentMethod(models.TextChoices):
    CASH = "Cash"
    CREDIT = "Credit"

class DeliveryStatus(models.TextChoices):
    DELIVERED = "Delivered"
    PENDING = "Pending"

class OrderStatus(models.TextChoices):
    COMPLETED= "Completed"
    PENDING = "Pending"
    CANCLED = "Cancled"
#END

class Orders(models.Model):
    id = models.AutoField(primary_key = True)
    customer_id = models.ForeignKey(Customers, on_delete = models.CASCADE)
    method = models.CharField(max_length = 50, choices = PaymentMethod.choices, default = PaymentMethod.CASH)
    delivery_status = models.CharField(max_length = 50, choices = DeliveryStatus.choices, default = DeliveryStatus.DELIVERED)
    total = models.PositiveIntegerField()
    added_date = models.DateField(auto_now_add=True, null=True)
    added_by = models.ForeignKey(
        UserAccount, on_delete=models.DO_NOTHING, null = True )


class Order_Product(models.Model):
    id = models.AutoField(primary_key = True)
    ord_id = models.ForeignKey(Orders, on_delete = models.CASCADE, null=True)
    prod_id = models.ForeignKey(Products, on_delete = models.CASCADE, db_column = "name")
    prod_size = models.PositiveIntegerField(default = 100)
    quantity = models.IntegerField()


#CHOICES FOR EXPENSE 
class ExpenseMethod(models.TextChoices):
    OPERATIONS = "Operation"
    MANAGEMENT = "Management"
    MISCELLANEOUS= "Miscellaneous"

# class Expenses(models.Model):
#     id = models.AutoField(primary_key = True)
#     expense_category = models.CharField(max_length = 50, choices  = ExpenseMethod.choices, default = ExpenseMethod.OPERATIONS)
#     amount = models.IntegerField()
#     description = models.TextField()
#     added_by = models.ForeignKey(
#         UserAccount, on_delete=models.DO_NOTHING, null = True )
#     added_date = models.DateTimeField(default=datetime.now, blank=True)
class Company_Expense(models.Model):
    id = models.AutoField(primary_key = True)
    expense_category = models.CharField(max_length = 50, choices = ExpenseMethod.choices, default = ExpenseMethod.OPERATIONS)
    amount = models.PositiveIntegerField()
    description = models.TextField()
    added_date = models.DateField(auto_now_add = True, null = True)
    added_by = models.ForeignKey(UserAccount, on_delete = models.DO_NOTHING, null = True)
class ProductImage(models.Model):
    id = models.AutoField(primary_key = True )
    prod_id = models.ForeignKey(Products, on_delete = models.CASCADE, db_column="name")
    product_image = models.ImageField(upload_to = 'photos')
    
