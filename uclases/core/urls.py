from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view

urlpatterns = [
	path('admin/', admin.site.urls),
	path('login/', login_view, name='login'),
	path('accounts/', include('accounts.urls')),
	path('', include('home.urls')),
]
