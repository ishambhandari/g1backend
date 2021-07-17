from rest_framework import generics
from rest_framework.views import APIView
from .models import Employees, Customers, Products, Orders, Order_Product, Company_Expense, ProductImage
from .serializers import EmployeeSerializer, CustomerSerializer, Order_ProductSerializer, ProductSerializer, OrderSerializer, ExpenseSerializer, ProductImageSerializer
from rest_framework import permissions, authentication 
from django.db.models.query_utils import Q
from .custompermissions import ExpensePermission 
qq = Q()

class EmployeeList(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAdminUser,)
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
   
class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAdminUser,)
    queryset = Employees.objects.all() 
    serializer_class = EmployeeSerializer

class CustomerList(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all() 
    serializer_class = CustomerSerializer

class OrderList(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderSerializer 
    def get_queryset(self):
        queryset = Orders.objects.all()
        start_date_param = self.request.query_params.get('startDate')
        end_date_param= self.request.query_params.get('endDate')
        orderParam = self.request.query_params.get('orderParam')
        earningParam = self.request.query_params.get('earningParam')
        if orderParam == 'Credit':
            queryset = queryset.filter(method = 'Credit')
        elif start_date_param is not None: 
            queryset_initial = Orders.objects.filter(added_date__range=[start_date_param, end_date_param])
            if earningParam is not None:
                queryset = queryset_initial.filter(added_by=earningParam)
            else :
                queryset = queryset_initial
        elif orderParam == 'Pending':
            queryset = queryset.filter(delivery_status = 'Pending')
        elif earningParam:
            queryset = Orders.objects.filter(added_by=earningParam)
        return queryset

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Orders.objects.all() 
    serializer_class = OrderSerializer
    
class ProductList(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Products.objects.all() 
    serializer_class = ProductSerializer
    
class Expenses(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated, ExpensePermission)
    serializer_class = ExpenseSerializer 
    def get_queryset(self):
        permissions_classes = (permissions.IsAdminUser,)
        queryset = Company_Expense.objects.all()
        start_date = self.request.query_params.get('startDate')
        end_date= self.request.query_params.get('endDate')
        if start_date:
            queryset = Company_Expense.objects.filter(added_date__range=[start_date, end_date])
        return queryset 


class ExpensesDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Company_Expense.objects.all()
    serializer_class = ExpenseSerializer

class OrderProduct(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    serializer_class = Order_ProductSerializer

    def get_queryset(self):
        queryset = Order_Product.objects.all()
        orderDetail = self.request.query_params.get('orderDetail')
        if orderDetail is not None:
            queryset = queryset.filter(ord_id = orderDetail)
        return queryset
        

class ProductImage(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        queryset = ProductImage.objects.all()
        prodImg = self.request.query_params.get('prodImg')
        if prodImg is not None:
            queryset = queryset.filter(prodImg = prodImg)
        return queryset
