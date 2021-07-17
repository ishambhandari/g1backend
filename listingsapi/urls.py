
from django.urls import path, include
from .views import EmployeeList, EmployeeDetails, CustomerList, ProductList, OrderList, Expenses, OrderProduct, ProductImage, ProductDetail, OrderDetail, CustomerDetail, ExpensesDetail 

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name="employeesList"),
    path('employees/<int:pk>', EmployeeDetails.as_view(), name="employeesDetail"),
    path('customer/', CustomerList.as_view(), name="CustomerList"),
    path('customer/<int:pk>', CustomerDetail.as_view(), name="customerDetail"),
    path('product/', ProductList.as_view(), name="ProductList"),
    path('product/<int:pk>', ProductDetail.as_view(), name="productDetail"),
    path('order/', OrderList.as_view(), name="OrderList"),
    path('order/<int:pk>', OrderDetail.as_view(), name="orderDetail"),
    path('expense/', Expenses.as_view(), name="expenseList"),
    path('expense/<int:pk>', ExpensesDetail.as_view()),
    path('order_product/', OrderProduct.as_view(), name = "OrderProduct"),
    path('product_image/', ProductImage.as_view(), name = "productImage"),



]
