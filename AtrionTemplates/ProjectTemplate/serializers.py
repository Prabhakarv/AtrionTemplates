from ProjectTemplate.models import Customer, Employee, ProjectDetails

from rest_framework import serializers

class CustomerSerializers(serializers.ModelSerializer):
	class Meta:
		model=Customer
		fields = ('id','cust_firstname','cust_lastname','cust_company','created_at','updated_at','cust_contact_number','cust_email','cust_address')

		read_only_fields = ('created_at', 'updated_at')

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employee
		fields = ('id','employee_firstname','employee_lastname','created_at','updated_at','employee_contact_number','employee_email','employee_designation','employee_address')
			
		read_only_fields = ('created_at', 'updated_at')

class ProjectDetailsSerializer(serializers.ModelSerializer):
	#customer = CustomerSerializers(read_only=True)
	#employee = EmployeeSerializer(read_only=True)
	customer = serializers.SlugRelatedField(slug_field='cust_firstname', read_only=True)
	employee = serializers.SlugRelatedField(slug_field='employee_firstname', read_only=True)
	class Meta:
			model = ProjectDetails
			fields = ('id','project_name','project_startdate','created_at','updated_at','project_status','customer','employee')
			read_only_fields = ('created_at', 'updated_at')			