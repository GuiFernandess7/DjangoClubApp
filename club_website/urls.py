from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

# Configure admin titles
admin.site.site_header = "Admin Session"
admin.site.site_title = "Admin Session"
admin.site.index_title = "Admin Area"