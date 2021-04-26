from os import name
from django.urls import path
from . import views
from webfisika import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tabel_user/', views.UserView.as_view(), name='tabel_user'),
    path('upload_berkas_jurnal/', views.UploadBerkasJurnalView.as_view(), name='upload_berkas_jurnal'),
    path('upload_berkas_prosiding/', views.UploadBerkasProsidingView.as_view(), name='upload_berkas_prosiding'),
    path('upload_berkas_buku/', views.UploadBerkasBukuView.as_view(), name='upload_berkas_buku'),
    path('upload_berkas_haki/', views.UploadBerkasHakiView.as_view(), name='upload_berkas_haki'),
    ######### End Upload #########
    path('histori_pengajuan/jurnal/', views.ListBerkasJurnalView.as_view(), name='list_berkas_jurnal'),
    path('histori_pengajuan/prosiding/', views.ListBerkasProsidingView.as_view(), name='list_berkas_prosiding'),
    path('histori_pengajuan/buku/', views.ListBerkasBukuView.as_view(), name='list_berkas_buku'),
    path('histori_pengajuan/haki/', views.ListBerkasHakiView.as_view(), name='list_berkas_haki'),
    ######### End List Pengajuan #########
    path('histori_pengajuan/jurnal/<slug>/', views.DetailBerkasJurnalView.as_view(), name='detail_berkas_jurnal'),
    path('histori_pengajuan/prosiding/<slug>/', views.DetailBerkasProsidingView.as_view(), name='detail_berkas_prosiding'),
    path('histori_pengajuan/buku/<slug>/', views.DetailBerkasBukuView.as_view(), name='detail_berkas_buku'),
    path('histori_pengajuan/haki/<slug>/', views.DetailBerkasHakiView.as_view(), name='detail_berkas_haki'),
    ######### End Detail Berkas #########
    path('histori_pengajuan/jurnal/edit/<pk>/', views.EditBerkasJurnalView.as_view(), name='edit_berkas_jurnal'),
    path('histori_pengajuan/prosiding/edit/<pk>/', views.EditBerkasProsidingView.as_view(), name='edit_berkas_prosiding'),
    path('histori_pengajuan/buku/edit/<pk>/', views.EditBerkasBukuView.as_view(), name='edit_berkas_buku'),
    path('histori_pengajuan/haki/edit/<pk>/', views.EditBerkasHakiView.as_view(), name='edit_berkas_haki'),
    ######### End Edit Berkas #########
    path('histori_pengajuan/jurnal/plagiasi_linieritas/<pk>/', views.PlagiasiLinieritasView.as_view(), name='plagiasi'),
    ######### End Plagiasi #########
    path('histori_pengajuan/jurnal/verifikasi/<pk>/', views.VerifikasiBerkasJurnalView.as_view(), name='verifikasi_berkas_jurnal'),
    path('histori_pengajuan/prosiding/verifikasi/<pk>/', views.VerifikasiBerkasProsidingView.as_view(), name='verifikasi_berkas_prosiding'),
    path('histori_pengajuan/buku/verifikasi/<pk>/', views.VerifikasiBerkasBukuView.as_view(), name='verifikasi_berkas_buku'),
    path('histori_pengajuan/haki/verifikasi/<pk>/', views.VerifikasiBerkasHakiView.as_view(), name='verifikasi_berkas_haki'),
    ######### End Verifikasi Berkas #########
    path('penilaian_jurnal/', views.PenilaianBerkasJurnalView.as_view(), name='penilaian_jurnal'),
    path('penilaian_prosiding/', views.PenilaianBerkasProsidingView.as_view(), name='penilaian_prosiding'),
    path('penilaian_buku/', views.PenilaianBerkasBukuView.as_view(), name='penilaian_buku'),
    path('penilaian_haki/', views.PenilaianBerkasHakiView.as_view(), name='penilaian_haki'),
    ######### End Penilaian #########
    path('rekap_jurnal/<slug>/',views.HasilPenilaianJurnalView.as_view(), name='rekap_jurnal'),
    path('rekap_prosiding/<slug>/',views.HasilPenilaianProsidingView.as_view(), name='rekap_prosiding'),
    path('rekap_buku/<slug>/',views.HasilPenilaianBukuView.as_view(), name='rekap_buku'),
    path('rekap_haki/<slug>/',views.HasilPenilaianHakiView.as_view(), name='rekap_haki'),
    ######### End of Hasil Rekap #########
    path('tambah_penulis/', views.PenulisLainView.as_view(), name='tambah_penulis'),
    # path('data_json/', views.AllView.as_view(), name='data_json')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)