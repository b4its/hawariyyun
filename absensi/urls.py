from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_absensi, name="index_absensi"),
    path('kehadiran', views.absensi, name="absensi"),
    path('sekretaris/list_kehadiran', views.list_kehadiran, name="list_kehadiran"),
    path('sekretaris/list_kehadiran/rincian', views.search_rinci, name="search_rinci"),
    path('sekretaris/show_kehadiran/<int:id>', views.show_kehadiran, name="show_kehadiran"),
    path('sekretaris/show_anggota/<int:id>', views.show_anggota, name="show_anggota"),
    path('sekretaris/list_kehadiran/nama', views.list_nama, name="list_nama"),
    path('sekretaris/list_kehadiran/hadir', views.list_hadir, name="list_hadir"),
    path('sekretaris/list_kehadiran/izin', views.list_izin, name="list_izin"),
    path('sekretaris/list_kehadiran/tidak_hadir', views.list_thadir, name="list_thadir"),
    path('sekretaris/list_pengurus', views.list_pengurus, name="list_pengurus"),
    path('pengurus/list_petinggi', views.list_petinggi, name="list_petinggi"),
    path('pengurus/list_sekretaris', views.list_sekretaris, name="list_sekretaris"),
    path('pengurus/list_bendahara', views.list_bendahara, name="list_bendahara"),
    path('pengurus/list_psdm', views.list_psdm, name="list_psdm"),
    path('pengurus/list_medkom', views.list_medkom, name="list_medkom"),
    path('pengurus/list_anggota', views.list_anggota, name="list_anggota"),
]