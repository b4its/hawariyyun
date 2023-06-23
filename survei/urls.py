from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_survei, name="index_survei"),
    path('sekretaris', views.sekretaris_survei, name="sekretaris_survei"),
    path('sekretaris/show/<int:id>', views.show_survei, name="show_survei"),
    path('sekretaris/nama', views.survei_nama, name="survei_nama"),
]