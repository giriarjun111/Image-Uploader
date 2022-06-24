from django.urls import path
from .views import home, home_delete

urlpatterns = [
	path('', home, name='home'),
	path('delete/<int:id>/', home_delete, name='delete'),
]