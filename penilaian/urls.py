from django.views.static import serve
from django.urls import path
from . import views
from webfisika import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload_berkas_jurnal/', views.UploadBerkasJurnalView.as_view(), name='upload_berkas_jurnal'),
    path('upload_berkas_prosiding/', views.UploadBerkasProsidingView.as_view(), name='upload_berkas_prosiding'),
    path('upload_berkas_buku/', views.UploadBerkasBukuView.as_view(), name='upload_berkas_buku'),
    path('upload_berkas_haki/', views.UploadBerkasHakiView.as_view(), name='upload_berkas_haki'),
    ######### End Upload #########
    path('histori_pengajuan/jurnal/<page>/', views.ListBerkasJurnalView.as_view(), name='list_berkas_jurnal'),
    path('histori_pengajuan/prosiding/<page>/', views.ListBerkasProsidingView.as_view(), name='list_berkas_prosiding'),
    path('histori_pengajuan/buku/<page>/', views.ListBerkasBukuView.as_view(), name='list_berkas_buku'),
    path('histori_pengajuan/haki/<page>/', views.ListBerkasHakiView.as_view(), name='list_berkas_haki'),
    ######### End List Pengajuan #########
    path('histori_pengajuan/jurnal/detail/<pk>/', views.DetailBerkasJurnalView.as_view(), name='detail_berkas_jurnal'),
    path('histori_pengajuan/prosiding/detail/<pk>/', views.DetailBerkasProsidingView.as_view(), name='detail_berkas_prosiding'),
    path('histori_pengajuan/buku/detail/<pk>/', views.DetailBerkasBukuView.as_view(), name='detail_berkas_buku'),
    path('histori_pengajuan/haki/detail/<pk>/', views.DetailBerkasHakiView.as_view(), name='detail_berkas_haki'),
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
    # R1 #
    path('penilaian_jurnal/R1/<pk>/', views.PenilaianBerkasJurnalView.as_view(), name='penilaian_jurnal'),
    path('penilaian_prosiding/R1/<pk>/', views.PenilaianBerkasProsidingView.as_view(), name='penilaian_prosiding'),
    path('penilaian_buku/R1/<pk>/', views.PenilaianBerkasBukuView.as_view(), name='penilaian_buku'),
    path('penilaian_haki/R1/<pk>/', views.PenilaianBerkasHakiView.as_view(), name='penilaian_haki'),
    # R2 #
    path('penilaian_jurnal/R2/<pk>/', views.PenilaianBerkasJurnal2View.as_view(), name='penilaian_jurnal2'),
    path('penilaian_prosiding/R2/<pk>/', views.PenilaianBerkasProsiding2View.as_view(), name='penilaian_prosiding2'),
    path('penilaian_buku/R2/<pk>/', views.PenilaianBerkasBuku2View.as_view(), name='penilaian_buku2'),
    path('penilaian_haki/R2/<pk>/', views.PenilaianBerkasHaki2View.as_view(), name='penilaian_haki2'),
    ######### End Penilaian #########
    # R1 #
    path('rekap_jurnal/R1/<slug>/',views.HasilPenilaianJurnalView.as_view(), name='rekap_jurnal'),
    path('rekap_prosiding/R1/<slug>/',views.HasilPenilaianProsidingView.as_view(), name='rekap_prosiding'),
    path('rekap_buku/R1/<slug>/',views.HasilPenilaianBukuView.as_view(), name='rekap_buku'),
    path('rekap_haki/R1/<slug>/',views.HasilPenilaianHakiView.as_view(), name='rekap_haki'),
    # R2 #
    path('rekap_jurnal/R2/<slug>/',views.HasilPenilaianJurnal2View.as_view(), name='rekap_jurnal2'),
    path('rekap_prosiding/R2/<slug>/',views.HasilPenilaianProsiding2View.as_view(), name='rekap_prosiding2'),
    path('rekap_buku/R2/<slug>/',views.HasilPenilaianBuku2View.as_view(), name='rekap_buku2'),
    path('rekap_haki/R2/<slug>/',views.HasilPenilaianHaki2View.as_view(), name='rekap_haki2'),
    ######### End of Hasil Rekap #########
    path('tambah_penulis/', views.PenulisLainView.as_view(), name='tambah_penulis'),
    ######### End of Tambah Penulis #########
    path('list_penilaian_jurnal/<page>/', views.ListReviewerJurnalView.as_view(), name='list_penilaian_jurnal'),
    path('list_penilaian_prosiding/<page>/', views.ListReviewerProsidingView.as_view(), name='list_penilaian_prosiding'),
    path('list_penilaian_buku/<page>/', views.ListReviewerBukuView.as_view(), name='list_penilaian_buku'),
    path('list_penilaian_haki/<page>/', views.ListReviewerHakiView.as_view(), name='list_penilaian_haki'),
    ######### End of Tabel Penilaian #########
    # R1 #
    path('penilaian_jurnal/edit/R1/<slug>/', views.PenilaianBerkasJurnalEditView.as_view(), name='edit_penilaian_jurnal'),
    path('penilaian_prosiding/edit/R1/<slug>/', views.PenilaianBerkasProsidingEditView.as_view(), name='edit_penilaian_prosiding'),
    path('penilaian_buku/edit/R1/<slug>/', views.PenilaianBerkasBukuEditView.as_view(), name='edit_penilaian_buku'),
    path('penilaian_haki/edit/R1/<slug>/', views.PenilaianBerkasHakiEditView.as_view(), name='edit_penilaian_haki'),
    # R2 #
    path('penilaian_jurnal/edit/R2/<slug>/', views.PenilaianBerkasJurnal2EditView.as_view(), name='edit_penilaian_jurnal2'),
    path('penilaian_prosiding/edit/R2/<slug>/', views.PenilaianBerkasProsiding2EditView.as_view(), name='edit_penilaian_prosiding2'),
    path('penilaian_buku/edit/R2/<slug>/', views.PenilaianBerkasBuku2EditView.as_view(), name='edit_penilaian_buku2'),
    path('penilaian_haki/edit/R2/<slug>/', views.PenilaianBerkasHaki2EditView.as_view(), name='edit_penilaian_haki2'),
    ######### End of Edit Penilaian #########
    path('error/penilaian_belum_ada', views.ErrorMessage.as_view(), name='error_message'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)