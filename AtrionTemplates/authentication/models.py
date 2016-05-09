from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class AccountManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		if not email:
			raise ValueError('Users must have a valid email address.')

		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username.')

		account = self.model(
			email=self.normalize_email(email), username=kwargs.get('username')
		)

		account.set_password(password)
		account.save()

		return account

	def create_superuser(self, email, password, **kwargs):
		account = self.create_user(email, password, **kwargs)

		account.is_admin = True
		account.save()

		return account

class Account (AbstractBaseUser, PermissionsMixin):

		email=models.EmailField(unique=True)
		username=models.CharField(max_length=40,unique=True)

		first_name=models.CharField(max_length=40,blank=True)
		last_name=models.CharField(max_length=40,blank=True)

# a new field added to User just to know about the User with his tagline		
		tagline=models.CharField(max_length=140,blank=True)  		

		is_admin=models.BooleanField(default=False)
		is_staff=models.BooleanField(default=True)

#auto_now_add sets the current date time and makes sure it is not edited in future		
		created_at=models.DateTimeField(auto_now_add=True) 		

#auto_now sets the current date time and makes sure it is updated on every time user object is saved
		updated_at=models.DateTimeField(auto_now=True)

#When you want to get a model instance in Django, you use an expression of the form Model.objects.get(**kwargs). The objects attribute here is a Manager class whose name typically follows the <model name>Manager convention. In our case, we will create an AccountManager class. We will do this momentarily.
		objects = AccountManager() 									

		
#tell Django that we want to treat the email field as the username for this model, we set the USERNAME_FIELD attribute to email. The field specified by USERNAME_FIELD must be unique, so we pass the unique=True argument in the email field.
	
		USERNAME_FIELD = 'email'               						
		REQUIRED_FIELDS = ['username']
	
		def __unicode__(self):  
			return self.email

		def get_full_name(self):
			return ' '.join([self.first_name, self.last_name])

		def get_short_name(self):
			return self.first_name