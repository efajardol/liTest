from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from DriversVehicles import views

urlpatterns = [
    path('drivers/', views.DriversList.as_view()),
    path('drivers/driver_id/<int:driver_id>', views.idDriverDetail.as_view()),
    path('drivers/name/<str:name>', views.nameDriverDetail.as_view()),
    path('drivers/plate/<str:vehicle__plate>', views.vplateDriverDetail.as_view()),
    path('vehicles',views.VehiclesList.as_view()),
    path('vehicles/hist',views.histBrandVehiclesList.as_view()),
    path('vehicles/count',views.countVehicles.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
