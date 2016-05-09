from django.db import models

# Create your models here.
class Customer(models.Model):

	cust_firstname=models.TextField(max_length=50)
	cust_lastname=models.TextField(max_length=50)
	cust_company=models.TextField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	cust_contact_number = models.IntegerField()
	cust_email = models.TextField(max_length=100)
	cust_address=models.TextField(max_length=200,default=None)
	
	def __unicode__(self):
		return self.cust_firstname

class Employee(models.Model):

	employee_firstname = models.TextField(max_length=50)
	employee_lastname = models.TextField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	employee_contact_number = models.IntegerField()
	employee_email = models.TextField(max_length=100)
	employee_designation = models.TextField(max_length=50)
	employee_address=models.TextField(max_length=200, default=None)
	
	def __unicode__(self):
		return self.employee_firstname

class ProjectDetails(models.Model):
	
	customer = models.ForeignKey(Customer)
	employee=models.ForeignKey(Employee)
	project_name = models.TextField(max_length=50)
	project_startdate = models.DateField(auto_now=False, default=None)
	project_status = models.TextField(default="Initial")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.project_name


