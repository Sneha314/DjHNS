
from stocks.views import create_bloodstock, update_bloodstock, create_vaccinestock, update_vaccinestock
from django.urls import path

app_name = 'stocks'

urlpatterns = [
    path('create_bloodstock/',create_bloodstock, name='create-bloodstock' ),
    path('<int:id>/update_bloodstock/',update_bloodstock, name='update-bloodstock' ),
    path('create_vaccinestock/',create_vaccinestock, name='create-vaccinestock' ),
    path('<int:id>/update_vaccinestock/',update_vaccinestock, name='update-vaccinestock' ),

]