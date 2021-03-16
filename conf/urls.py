from django.urls import path
from tours.views import custom_404, custom_500, departure_view, main_view, tour_view

handler404 = custom_404
handler500 = custom_500

urlpatterns = [
    path("", main_view, name="main"),
    path("departure/<str:dep_code>", departure_view, name="departure"),
    path("tour/<int:tour_id>", tour_view, name="tour"),
]
