# Generated by Django 3.1.7 on 2021-04-20 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(default=None, max_length=18, verbose_name='Nomor Induk Pegawai')),
                ('reviewer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadBerkasProsiding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_artikel', models.CharField(max_length=255, unique=True, verbose_name='Judul Artikel')),
                ('jmlh_penulis', models.PositiveIntegerField(verbose_name='Jumlah Penulis')),
                ('nama_prosiding', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nama Prosiding')),
                ('nomor_isbn', models.CharField(max_length=255, verbose_name='Nomor ISBN')),
                ('tahun_terbit', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tahun Terbit')),
                ('penerbit', models.CharField(blank=True, max_length=255, null=True, verbose_name='Penerbit')),
                ('url_repository', models.CharField(blank=True, max_length=150, null=True, verbose_name='Link Repository')),
                ('indeks_prosiding', models.CharField(blank=True, max_length=255, null=True, verbose_name='Terindeks di')),
                ('kategori_publikasi', models.CharField(choices=[('Presentasi Oral dan Dipublikasikan', 'Presentasi Oral dan Dipublikasikan'), ('Poster dan Dipublikasikan dalam Prosiding', 'Poster dan Dipublikasikan dalam Prosiding'), ('Diseminarkan Namun Tidak Terpublikasi', 'Diseminarkan Namun Tidak Terpublikasi'), ('Tidak Diseminarkan Namun Terpublikasi', 'Tidak Diseminarkan Namun Terpublikasi'), ('Terpublikasi dalam Koran/Majalah', 'Terpublikasi dalam Koran/Majalah')], default=None, max_length=100, verbose_name='Kategori Publikasi')),
                ('tingkat_publikasi', models.CharField(blank=True, choices=[('Internasional Terindeks Scimagojr & Scopus', 'Internasional Terindeks Scimagojr & Scopus'), ('Internasional Terindeks Scopus / IEEE', 'Internasional Terindeks Scopus / IEEE'), ('Internasional', 'Internasional'), ('Nasional', 'Nasional')], default=None, max_length=100, null=True, verbose_name='Tingkat Publikasi')),
                ('upload_prosiding', models.FileField(upload_to='prosiding/isi/', verbose_name='Upload Prosiding (isi)')),
                ('upload_cover', models.FileField(blank=True, null=True, upload_to='prosiding/cover/', verbose_name='Upload Prosiding (cover)')),
                ('is_verificated', models.BooleanField(blank=True, default=False, null=True)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('corresponding_author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_prosiding_corresponding_author', to=settings.AUTH_USER_MODEL, verbose_name='Corresponding Author')),
                ('penulis_lain', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('penulis_utama', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_prosiding_penulis_utama', to=settings.AUTH_USER_MODEL, verbose_name='Penulis Utama')),
                ('reviewer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_prosiding_reviewer', to='penilaian.reviewer')),
            ],
        ),
        migrations.CreateModel(
            name='UploadBerkasJurnal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_artikel', models.CharField(max_length=255, unique=True, verbose_name='Judul Artikel')),
                ('jmlh_penulis', models.PositiveIntegerField(verbose_name='Jumlah Penulis')),
                ('nama_jurnal', models.CharField(max_length=255, verbose_name='Nama Jurnal')),
                ('nomor_issn', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nomor ISSN')),
                ('vol_no_bln_thn', models.CharField(blank=True, max_length=255, null=True, verbose_name='Volume/No/Bulan/Tahun')),
                ('penerbit', models.CharField(blank=True, max_length=255, null=True, verbose_name='Penerbit')),
                ('doi_artikel', models.CharField(blank=True, max_length=255, null=True, verbose_name='DOI Artikel')),
                ('url_jurnal', models.CharField(blank=True, max_length=150, null=True, verbose_name='Link Jurnal')),
                ('indeks_jurnal', models.CharField(blank=True, max_length=255, null=True, verbose_name='Indeks Jurnal')),
                ('kategori_publikasi', models.CharField(choices=[('Jurnal Ilmiah Internasional Bereputasi Berdampak', 'Jurnal Ilmiah Internasional Bereputasi Berdampak'), ('Jurnal Ilmiah Internasional Bereputasi', 'Jurnal Ilmiah Internasional Bereputasi'), ('Jurnal Ilmiah Internasional', 'Jurnal Ilmiah Internasional'), ('Jurnal Ilmiah Nasional Terakreditasi', 'Jurnal Ilmiah Nasional Terakreditasi'), ('Jurnal Ilmiah Nasional Berbahasa PBB', 'Jurnal Ilmiah Nasional Berbahasa PBB'), ('Jurnal Ilmiah Nasional Tidak Terakreditasi', 'Jurnal Ilmiah Nasional Tidak Terakreditasi'), ('Jurnal Ilmiah Nasional terindeks di DOAJ dll', 'Jurnal Ilmiah Nasional terindeks di DOAJ dll')], default=None, max_length=100, verbose_name='Kategori Publikasi')),
                ('upload_jurnal', models.FileField(upload_to='jurnal/isi/', verbose_name='Upload Jurnal (isi)')),
                ('upload_cover', models.FileField(blank=True, null=True, upload_to='jurnal/cover/', verbose_name='Upload Jurnal (cover)')),
                ('is_verificated', models.BooleanField(blank=True, default=False, null=True)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('corresponding_author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_jurnal_corresponding_author', to=settings.AUTH_USER_MODEL, verbose_name='Corresponding Author')),
                ('penulis_lain', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('penulis_utama', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_jurnal_penulis_utama', to=settings.AUTH_USER_MODEL, verbose_name='Penulis Utama')),
                ('reviewer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_jurnal_reviewer', to='penilaian.reviewer')),
            ],
        ),
        migrations.CreateModel(
            name='UploadBerkasHaki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255, unique=True, verbose_name='Nama Berkas')),
                ('jmlh_penulis', models.PositiveIntegerField(verbose_name='Jumlah Pemegang Berkas')),
                ('kategori_publikasi', models.CharField(choices=[('Internasional (sudah diimplementasikan di industri)', 'Internasional (sudah diimplementasikan di industri)'), ('Internasional', 'Internasional'), ('Nasional (sudah diimplementasikan di industri)', 'Nasional (sudah diimplementasikan di industri)'), ('Nasional', 'Nasional'), ('Nasional (paten dari Dirjen Kekayaan Intelektual)', 'Nasional (paten dari Dirjen Kekayaan Intelektual)'), ('Karya cipta bersertifikat Dirjen', 'Karya cipta bersertifikat Dirjen'), ('Karya cipta bahan ajar', 'Karya cipta bahan ajar')], default=None, max_length=100, verbose_name='Kategori Publikasi')),
                ('upload_berkas', models.FileField(upload_to='haki/isi/', verbose_name='Upload Berkas')),
                ('is_verificated', models.BooleanField(blank=True, default=False, null=True)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('pemegang_berkas_utama', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_pemegang_berkas_utama', to=settings.AUTH_USER_MODEL, verbose_name='Pemegang Berkas Utama')),
                ('penulis_lain', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_haki_reviewer', to='penilaian.reviewer')),
            ],
        ),
        migrations.CreateModel(
            name='UploadBerkasBuku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255, verbose_name='Judul Buku')),
                ('jmlh_penulis', models.PositiveIntegerField(verbose_name='Jumlah Penulis')),
                ('nomor_isbn', models.CharField(max_length=255, unique=True, verbose_name='Nomor ISBN')),
                ('edisi', models.CharField(blank=True, max_length=255, null=True, verbose_name='Edisi')),
                ('tahun_terbit', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tahun Terbit')),
                ('penerbit', models.CharField(blank=True, max_length=255, null=True, verbose_name='Penerbit')),
                ('jumlah_halaman', models.CharField(blank=True, max_length=255, null=True, verbose_name='Jumlah Halaman')),
                ('kategori_publikasi', models.CharField(choices=[('Buku Referensi', 'Buku Referensi'), ('Buku Monograf', 'Buku Monograf'), ('Book Chapter Internasional', 'Book Chapter Internasional'), ('Book Chapter Nasional', 'Book Chapter Nasional')], default=None, max_length=100, verbose_name='Kategori Publikasi')),
                ('upload_buku', models.FileField(upload_to='buku/isi/', verbose_name='Upload Buku (isi)')),
                ('is_verificated', models.BooleanField(blank=True, default=False, null=True)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('penulis_lain', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('penulis_utama', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_buku_penulis_utama', to=settings.AUTH_USER_MODEL, verbose_name='Penulis Utama')),
                ('reviewer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_buku_reviewer', to='penilaian.reviewer')),
            ],
        ),
        migrations.CreateModel(
            name='PlagiasiLinieritas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plagiasi', models.PositiveIntegerField(verbose_name='Similarity Index')),
                ('linieritas', models.TextField(choices=[('Linier dengan bidang kerja', 'Linier dengan bidang kerja'), ('Tidak linier dengan bidang kerja', 'Tidak linier dengan bidang kerja')], verbose_name='Linieritas')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('jurnal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plagiasi_linieritas', to='penilaian.uploadberkasjurnal')),
            ],
        ),
        migrations.CreateModel(
            name='PenilaianBerkasProsiding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unsur_isi', models.FloatField(verbose_name='Kelengkapan dan Kesesuaian unsur isi prosiding')),
                ('cmnt_unsur_isi', models.TextField(verbose_name='Komentar Kelengkapan dan Kesesuaian unsur isi prosiding')),
                ('pembahasan', models.FloatField(verbose_name='Ruang lingkup dan kedalaman pembahasan')),
                ('cmnt_pembahasan', models.TextField(verbose_name='Komentar Ruang lingkup dan kedalaman pembahasan')),
                ('informasi', models.FloatField(verbose_name='Kecukupan dan kemutahiran data/informasi dan metodologi')),
                ('cmnt_informasi', models.TextField(verbose_name='Komentar Kecukupan dan kemutahiran data/informasi dan metodologi')),
                ('kualitas_penerbit', models.FloatField(verbose_name='Kelengkapan unsur dan kualitas penerbit')),
                ('cmnt_kualitas_penerbit', models.TextField(verbose_name='Komentar Kelengkapan unsur dan kualitas penerbit')),
                ('total', models.FloatField(blank=True, null=True, verbose_name='Total Nilai')),
                ('nilai_ca', models.FloatField(blank=True, null=True, verbose_name='Nilai Corresponding Author')),
                ('nilai_pu', models.FloatField(blank=True, null=True, verbose_name='Nilai Penulis Utama')),
                ('nilai_pl', models.FloatField(blank=True, null=True, verbose_name='Nilai Penulis Lainnya')),
                ('jmlh_penulis_lain', models.PositiveIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('prosiding', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='penilaian.uploadberkasprosiding')),
            ],
        ),
        migrations.CreateModel(
            name='PenilaianBerkasJurnal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unsur_isi', models.FloatField(verbose_name='Kelengkapan dan Kesesuaian unsur isi jurnal')),
                ('cmnt_unsur_isi', models.TextField(verbose_name='Komentar Kelengkapan dan Kesesuaian unsur isi jurnal')),
                ('pembahasan', models.FloatField(verbose_name='Ruang lingkup dan kedalaman pembahasan')),
                ('cmnt_pembahasan', models.TextField(verbose_name='Komentar Ruang lingkup dan kedalaman pembahasan')),
                ('informasi', models.FloatField(verbose_name='Kecukupan dan kemutahiran data/informasi dan metodologi')),
                ('cmnt_informasi', models.TextField(verbose_name='Komentar Kecukupan dan kemutahiran data/informasi dan metodologi')),
                ('kualitas_penerbit', models.FloatField(verbose_name='Kelengkapan unsur dan kualitas penerbit')),
                ('cmnt_kualitas_penerbit', models.TextField(verbose_name='Komentar Kelengkapan unsur dan kualitas penerbit')),
                ('total', models.FloatField(blank=True, null=True, verbose_name='Total Nilai')),
                ('nilai_ca', models.FloatField(blank=True, null=True, verbose_name='Nilai Corresponding Author')),
                ('nilai_pu', models.FloatField(blank=True, null=True, verbose_name='Nilai Penulis Utama')),
                ('nilai_pl', models.FloatField(blank=True, null=True, verbose_name='Nilai Penulis Lainnya')),
                ('jmlh_penulis_lain', models.PositiveIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('jurnal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='penilaian.uploadberkasjurnal')),
            ],
        ),
        migrations.CreateModel(
            name='PenilaianBerkasHaki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unsur_isi', models.FloatField(verbose_name='Kelengkapan Unsur Isi Deskripsi')),
                ('cmnt_unsur_isi', models.TextField(verbose_name='Komentar Kelengkapan Unsur Isi Deskripsi')),
                ('pembahasan', models.FloatField(verbose_name='Ruang Lingkup dan Kedalaman Pembahasan')),
                ('cmnt_pembahasan', models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')),
                ('informasi', models.FloatField(verbose_name='Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')),
                ('cmnt_informasi', models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')),
                ('kualitas_penerbit', models.FloatField(verbose_name='Kelengkapan Unsur dan Kualitas Penerbit')),
                ('cmnt_kualitas_penerbit', models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')),
                ('total', models.FloatField(blank=True, null=True, verbose_name='Total Nilai')),
                ('nilai_pu', models.FloatField(blank=True, null=True, verbose_name='Nilai Pemegang Berkas Utama')),
                ('nilai_pl', models.FloatField(blank=True, null=True, verbose_name='Nilai Pemegang Berkas Lainnya')),
                ('jmlh_penulis_lain', models.PositiveIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('berkas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='penilaian.uploadberkashaki')),
            ],
        ),
        migrations.CreateModel(
            name='PenilaianBerkasBuku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unsur_isi', models.FloatField(verbose_name='Kelengkapan Unsur Isi Buku')),
                ('cmnt_unsur_isi', models.TextField(verbose_name='Komentar Kelengkapan Unsur Isi Buku')),
                ('pembahasan', models.FloatField(verbose_name='Ruang Lingkup dan Kedalaman Pembahasan')),
                ('cmnt_pembahasan', models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')),
                ('informasi', models.FloatField(verbose_name='Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')),
                ('cmnt_informasi', models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')),
                ('kualitas_penerbit', models.FloatField(verbose_name='Kelengkapan Unsur dan Kualitas Penerbit')),
                ('cmnt_kualitas_penerbit', models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')),
                ('total', models.FloatField(blank=True, null=True, verbose_name='Total Nilai')),
                ('nilai_pu', models.FloatField(blank=True, null=True, verbose_name='Nilai Penulis Utama')),
                ('nilai_pl', models.FloatField(blank=True, null=True, verbose_name='Nilai Penulis Lainnya')),
                ('jmlh_penulis_lain', models.PositiveIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('buku', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='penilaian.uploadberkasbuku')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
