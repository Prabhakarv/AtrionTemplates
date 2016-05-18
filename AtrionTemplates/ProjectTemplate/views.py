# Create your views here.

from django.http import Http404

from ProjectTemplate.models import ProjectDetails, Customer, Employee
from ProjectTemplate.serializers import ProjectDetailsSerializer, CustomerSerializers, EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
											CRUD operations on all the Project object
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class ProjectViewSet(viewsets.ModelViewSet):
	queryset = ProjectDetails.objects.all()
	serializer_class = ProjectDetailsSerializer


	def perform_create(self, serializer):		
		custid = self.request.data.get("customer_id")
		empid = self.request.data.get("employee_id")
		projstatus =self.request.data.get("project_status")
		serializer.save(
					customer=Customer.objects.get(pk=custid),
					employee=Employee.objects.get(pk=empid),					
		)

	def perform_update(self, serializer):		
		custid = self.request.data.get("customer_id")
		empid = self.request.data.get("employee_id")
		serializer.save(
		customer=Customer.objects.get(pk=custid),
		employee=Employee.objects.get(pk=empid))
			
	def perform_destroy(self, instance):
			instance = self.get_object()
			instance.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
											CRUD operations on all the Employee object
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer


	def perform_create(self, serializer):		
		serializer.save()

	def perform_update(self, serializer):				
		serializer.save()
			
	def perform_destroy(self, instance):
			instance = self.get_object()
			instance.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
											CRUD operations on all the Customer object
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializers


	def perform_create(self, serializer):		
		serializer.save()

	def perform_update(self, serializer):				
		serializer.save()
			
	def perform_destroy(self, instance):
			instance = self.get_object()
			instance.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)