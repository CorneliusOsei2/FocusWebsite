from django.urls import path
from .views import home, contents

urlpatterns = [
    path('', home, name='home'),
]