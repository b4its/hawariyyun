from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_helpdesk, name="index_helpdesk"),
    path('kritik-dan-saran', views.saran, name="saran"),
    path('pengurus/list-kritik-saran', views.list_kritik_saran, name="list_kritik_saran"),
    path('pengurus/list-kritik', views.list_kritik, name="list_kritik"),
    path('pengurus/list-saran', views.list_saran, name="list_saran"),
    path('pengurus/list-kritik-saran/nama', views.list_nama, name="list_nama"),
    path('pengurus/update_kritik_saran/<int:id>', views.update_kritik_saran, name="update_kritik_saran"),
]