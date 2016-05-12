from django.conf.urls import patterns, url, include
from AtrionTemplates.views import IndexView
from rest_framework_nested import routers
from authentication.views import AccountViewSet
from django.views.generic import TemplateView


from authentication.views import LoginView, LogoutView
from ProjectTemplate.views import ProjectViewSet, CustomerViewSet, EmployeeViewSet

from django.contrib import admin
admin.autodiscover()


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'accounts', AccountViewSet)
router.register(r'projects',ProjectViewSet)
router.register(r'customers',CustomerViewSet)
router.register(r'employees',EmployeeViewSet)



urlpatterns = patterns(
    '',
    # urls    
	url(r'^api/v1/', include(router.urls)),
	url(r'^admin/', include(admin.site.urls)),
	url('^$', IndexView.as_view(), name='index'),
#	url(r'^api/v1/projects/$', ProjectListView.as_view()),    
#	url(r'^api/v1/customers/$', CustomerListView.as_view()),   
#	url(r'^api/v1/employees/$', EmployeeListView.as_view()),  
	url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
	url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout')
)
	

