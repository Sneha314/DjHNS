
<<<<<<< HEAD

from django.urls import path, include
from .views import create_bloodstock, create_vaccinestock, update_bloodstock, update_vaccinestock



urlpatterns = [
    path('create_bloodstock', create_bloodstock, name="create-bloodstock"),
    path('<int:id>/update_bloodstock', update_bloodstock, name="update-bloodstock"),
    path('create_vaccinestock', create_vaccinestock, name="create-vaccinestock"),
    path('<int:id>/update_vaccinestock', update_vaccinestock, name="update-vaccinestock"),
    
=======
from stocks.views import create_bloodstock, update_bloodstock, create_vaccinestock, update_vaccinestock
from django.urls import path

app_name = 'stocks'

urlpatterns = [
    path('create_bloodstock/',create_bloodstock, name='create-bloodstock' ),
    path('<int:id>/update_bloodstock/',update_bloodstock, name='update-bloodstock' ),
    path('create_vaccinestock/',create_vaccinestock, name='create-vaccinestock' ),
    path('<int:id>/update_vaccinestock/',update_vaccinestock, name='update-vaccinestock' ),

>>>>>>> cc211a397fdeca62c41250165c08d2b64aa99404
]