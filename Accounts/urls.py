from django.urls import path, include

app_name = 'Accounts'

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
]