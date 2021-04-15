from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Reviewer(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    nip = models.CharField(max_length=18, verbose_name='Nomor Induk Pegawai', default=None)

    def __str__(self):
        return f"{self.reviewer}"

class Admin(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.admin}"
    

class UploadBerkasJurnal(models.Model):
    pengusul = models.ForeignKey(User, related_name='user_jurnal_pengusul', on_delete=models.CASCADE, default=None)
    judul = models.CharField(max_length=255, verbose_name='Judul Jurnal', unique=True)
    jmlh_penulis = models.PositiveIntegerField(verbose_name='Jumlah Penulis')
    jmlh_penulis_lain = models.PositiveIntegerField(verbose_name='Jumlah Penulis (selain CA dan PU)')
    nomor_issn = models.CharField(max_length=255, verbose_name='Nomor ISSN', null=True, blank=True)
    vol_no_bln_thn = models.CharField(max_length=255, verbose_name='Volume/No/Bulan/Tahun', null=True, blank=True)
    penerbit = models.CharField(max_length=255, verbose_name='Penerbit', null=True, blank=True)
    doi_artikel = models.CharField(max_length=255, verbose_name='DOI Artikel', null=True, blank=True)
    url_jurnal = models.URLField(verbose_name='Link Jurnal', null=True, blank=True)
    indeks_jurnal = models.CharField(max_length=255, verbose_name='Indeks Scopus dan Scimagor', null=True, blank=True)
    kategori = [
        ('Jurnal Ilmiah Internasional Bereputasi','Jurnal Ilmiah Internasional Bereputasi'),
        ('Jurnal Ilmiah Internasional','Jurnal Ilmiah Internasional'),
        ('Jurnal Ilmiah Nasional Terakreditasi','Jurnal Ilmiah Nasional Terakreditasi'),
        ('Jurnal Ilmiah Nasional Tidak Terakreditasi','Jurnal Ilmiah Nasional Tidak Terakreditasi'),
        ('Jurnal Ilmiah Nasional terindeks di DOAJ dll','Jurnal Ilmiah Nasional terindeks di DOAJ dll'),
    ]
    kategori_publikasi = models.CharField(max_length=100, choices=kategori, default=None, verbose_name='Kategori Publikasi')
    upload_jurnal = models.FileField(upload_to='jurnal/isi/', verbose_name='Upload Jurnal (isi)')
    upload_cover = models.FileField(upload_to='jurnal/cover/', verbose_name='Upload Jurnal (cover)', blank=True, null=True)
    corresponding_author = models.ForeignKey(User, related_name='user_jurnal_corresponding_author', on_delete=models.CASCADE, verbose_name='Corresponding Author', default=None)
    penulis_utama = models.ForeignKey(User, related_name='user_jurnal_penulis_utama', on_delete=models.CASCADE, verbose_name='Penulis Utama', default=None)
    penulis_lain = models.ManyToManyField(User, blank=True)
    is_verificated = models.BooleanField(default=False, blank=True, null=True)
    reviewer = models.ForeignKey(Reviewer, related_name='user_jurnal_reviewer', on_delete=models.CASCADE, blank=True, null=True, default=None)
    uploaded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.judul}"
    
    def save(self):
        self.slug = slugify(self.judul)
        super().save()
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:detail_berkas_jurnal', kwargs= url_slug)
        

class UploadBerkasProsiding(models.Model):
    pengusul = models.ForeignKey(User, related_name='user_prosiding_pengusul', on_delete=models.CASCADE, default=None)
    judul = models.CharField(max_length=255, verbose_name='Judul Jurnal', unique=True)
    jmlh_penulis = models.PositiveIntegerField(verbose_name='Jumlah Penulis')
    jmlh_penulis_lain = models.PositiveIntegerField(verbose_name='Jumlah Penulis (selain CA dan PU)')
    nomor_isbn = models.CharField(max_length=255, verbose_name='Nomor ISBN', null=True, blank=True)
    tahun_terbit = models.CharField(max_length=255, verbose_name='Tahun Terbit', null=True, blank=True)
    penerbit = models.CharField(max_length=255, verbose_name='Penerbit', null=True, blank=True)
    url_repository = models.URLField(verbose_name='Link Repository', null=True, blank=True)
    indeks_prosiding = models.CharField(max_length=255, verbose_name='Terindeks di', null=True, blank=True)
    kategori = [
        ('Prosiding Forum Ilmiah Internasional','Prosiding Forum Ilmiah Internasional'),
        ('Prosiding Forum Ilmiah Nasional','Prosiding Forum Ilmiah Nasional'),
    ]
    kategori_publikasi = models.CharField(max_length=100, choices=kategori, default=None, verbose_name='Kategori Publikasi')
    upload_prosiding = models.FileField(upload_to='prosiding/isi/', verbose_name='Upload Prosiding (isi)')
    upload_cover = models.FileField(upload_to='prosiding/cover/', verbose_name='Upload Prosiding (cover)', blank=True, null=True)
    corresponding_author = models.ForeignKey(User, related_name='user_prosiding_corresponding_author', on_delete=models.CASCADE, verbose_name='Corresponding Author', default=None)
    penulis_utama = models.ForeignKey(User, related_name='user_prosiding_penulis_utama', on_delete=models.CASCADE, verbose_name='Penulis Utama', default=None)
    penulis_lain = models.ManyToManyField(User, blank=True)
    is_verificated = models.BooleanField(default=False, blank=True, null=True)
    reviewer = models.ForeignKey(Reviewer, related_name='user_prosiding_reviewer', on_delete=models.CASCADE, blank=True, null=True, default=None)
    uploaded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.judul}"
    
    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:detail_berkas_prosiding', kwargs= url_slug)

class UploadBerkasBuku(models.Model):
    pengusul = models.ForeignKey(User, related_name='user_buku_pengusul', on_delete=models.CASCADE, default=None)
    judul = models.CharField(max_length=255, verbose_name='Judul Buku', unique=True)
    jmlh_penulis = models.PositiveIntegerField(verbose_name='Jumlah Penulis')
    jmlh_penulis_lain = models.PositiveIntegerField(verbose_name='Jumlah Penulis (selain penulis utama)')
    nomor_isbn = models.CharField(max_length=255, verbose_name='Nomor ISBN', null=True, blank=True)
    edisi = models.CharField(max_length=255, verbose_name='Edisi', null=True, blank=True)
    tahun_terbit = models.CharField(max_length=255, verbose_name='Tahun Terbit', null=True, blank=True)
    penerbit = models.CharField(max_length=255, verbose_name='Penerbit', null=True, blank=True)
    jumlah_halaman = models.CharField(max_length=255, verbose_name='Jumlah Halaman', null=True, blank=True)
    kategori = [
        ('Buku Referensi','Buku Referensi'),
        ('Buku Monograf','Buku Monograf'),
    ]
    kategori_publikasi = models.CharField(max_length=100, choices=kategori, default=None, verbose_name='Kategori Publikasi')
    upload_buku = models.FileField(upload_to='buku/isi/', verbose_name='Upload Buku (isi)')
    penulis_utama = models.ForeignKey(User, related_name='user_buku_penulis_utama', on_delete=models.CASCADE, verbose_name='Penulis Utama', default=None)
    penulis_lain = models.ManyToManyField(User, blank=True)
    is_verificated = models.BooleanField(default=False, blank=True, null=True)
    reviewer = models.ForeignKey(Reviewer, related_name='user_buku_reviewer', on_delete=models.CASCADE, blank=True, null=True, default=None)
    uploaded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.judul}"
    
    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:detail_berkas_buku', kwargs= url_slug)

class UploadBerkasHaki(models.Model):
    pengusul = models.ForeignKey(User, related_name='user_pengusul', on_delete=models.CASCADE, default=None)
    judul = models.CharField(max_length=255, verbose_name='Nama Berkas', unique=True)
    jmlh_penulis = models.PositiveIntegerField(verbose_name='Jumlah Pemegang Berkas')
    jmlh_penulis_lain = models.PositiveIntegerField(verbose_name='Jumlah Pemegang Berkas Lain (selain pemegang berkas utama)')
    kategori = [
        ('Internasional (sudah diimplementasikan di industri)','Internasional (sudah diimplementasikan di industri)'),
        ('Internasional','Internasional'),
        ('Nasional (sudah diimplementasikan di industri)','Nasional (sudah diimplementasikan di industri)'),
        ('Nasional','Nasional'),
        ('Nasional (paten dari Dirjen Kekayaan Intelektual)','Nasional (paten dari Dirjen Kekayaan Intelektual)'),
        ('Karya cipta bersertifikat Dirjen','Karya cipta bersertifikat Dirjen'),
        ('Karya cipta bahan ajar','Karya cipta bahan ajar'),
    ]
    kategori_publikasi = models.CharField(max_length=100, choices=kategori, default=None, verbose_name='Kategori Publikasi')
    upload_berkas = models.FileField(upload_to='haki/isi/', verbose_name='Upload Berkas')
    pemegang_berkas_utama = models.ForeignKey(User, related_name='user_pemegang_berkas_utama', on_delete=models.CASCADE, verbose_name='Pemegang Paten Utama', default=None)
    penulis_lain = models.ManyToManyField(User, blank=True)
    is_verificated = models.BooleanField(default=False, blank=True, null=True)
    reviewer = models.ForeignKey(Reviewer, related_name='user_haki_reviewer', on_delete=models.CASCADE, blank=True, null=True, default=None)
    uploaded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.judul}"
    
    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:detail_berkas_haki', kwargs= url_slug)

class PenilaianBerkasJurnal(models.Model):
    jurnal = models.OneToOneField(UploadBerkasJurnal, on_delete=models.CASCADE)
    unsur_isi = models.PositiveIntegerField(verbose_name='Kelengkapan dan Kesesuaian unsur isi jurnal')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan dan Kesesuaian unsur isi jurnal')
    pembahasan = models.PositiveIntegerField(verbose_name='Ruang lingkup dan kedalaman pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang lingkup dan kedalaman pembahasan')
    informasi = models.PositiveIntegerField(verbose_name='Kecukupan dan kemutahiran data/informasi dan metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan kemutahiran data/informasi dan metodologi')
    kualitas_penerbit = models.PositiveIntegerField(verbose_name='Kelengkapan unsur dan kualitas penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan unsur dan kualitas penerbit')
    total = models.PositiveIntegerField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_ca = models.PositiveIntegerField(verbose_name='Nilai Corresponding Author', blank=True, null=True)
    nilai_pu = models.PositiveIntegerField(verbose_name='Nilai Penulis Utama', blank=True, null=True)
    nilai_pl = models.PositiveIntegerField(verbose_name='Nilai Penulis Lainnya', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.jurnal}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.jurnal)
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.jurnal.penulis_lain.all().exists() == False:
            self.nilai_ca = self.total * 0.5
            self.nilai_pu = self.total * 0.5
        else:
            self.nilai_ca = self.total * 0.4
            self.nilai_pu = self.total * 0.4
            self.nilai_pl = self.total * 0.2 / self.jurnal.jmlh_penulis_lain
        super(PenilaianBerkasJurnal, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_jurnal', kwargs= url_slug)

class PenilaianBerkasProsiding(models.Model):
    prosiding = models.OneToOneField(UploadBerkasProsiding, on_delete=models.CASCADE)
    unsur_isi = models.PositiveIntegerField(verbose_name='Kelengkapan dan Kesesuaian unsur isi prosiding')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan dan Kesesuaian unsur isi prosiding')
    pembahasan = models.PositiveIntegerField(verbose_name='Ruang lingkup dan kedalaman pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang lingkup dan kedalaman pembahasan')
    informasi = models.PositiveIntegerField(verbose_name='Kecukupan dan kemutahiran data/informasi dan metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan kemutahiran data/informasi dan metodologi')
    kualitas_penerbit = models.PositiveIntegerField(verbose_name='Kelengkapan unsur dan kualitas penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan unsur dan kualitas penerbit')
    total = models.PositiveIntegerField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_ca = models.PositiveIntegerField(verbose_name='Nilai Corresponding Author', blank=True, null=True)
    nilai_pu = models.PositiveIntegerField(verbose_name='Nilai Penulis Utama', blank=True, null=True)
    nilai_pl = models.PositiveIntegerField(verbose_name='Nilai Penulis Lainnya', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.prosiding}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.prosiding)
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.prosiding.penulis_lain.all().exists() == False:
            self.nilai_ca = self.total * 0.5
            self.nilai_pu = self.total * 0.5
        else:
            self.nilai_ca = self.total * 0.4
            self.nilai_pu = self.total * 0.4
            self.nilai_pl = self.total * 0.2 / self.prosiding.jmlh_penulis_lain
        super(PenilaianBerkasProsiding, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_prosiding', kwargs= url_slug)

class PenilaianBerkasBuku(models.Model):
    buku = models.OneToOneField(UploadBerkasBuku, on_delete=models.CASCADE)
    unsur_isi = models.PositiveIntegerField(verbose_name='Kelengkapan Unsur Isi Buku')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan Unsur Isi Buku')
    pembahasan = models.PositiveIntegerField(verbose_name='Ruang Lingkup dan Kedalaman Pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')
    informasi = models.PositiveIntegerField(verbose_name='Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    kualitas_penerbit = models.PositiveIntegerField(verbose_name='Kelengkapan Unsur dan Kualitas Penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')
    total = models.PositiveIntegerField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_pu = models.PositiveIntegerField(verbose_name='Nilai Penulis Utama', blank=True, null=True)
    nilai_pl = models.PositiveIntegerField(verbose_name='Nilai Penulis Lainnya', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.buku}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.buku)
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.buku.penulis_lain.all().exists() == False:
            self.nilai_pu = self.total
        else:
            self.nilai_pu = self.total * 0.8
            self.nilai_pl = self.total * 0.2 / self.buku.jmlh_penulis_lain
        super(PenilaianBerkasBuku, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_buku', kwargs= url_slug)

class PenilaianBerkasHaki(models.Model):
    berkas = models.OneToOneField(UploadBerkasHaki, on_delete=models.CASCADE)
    unsur_isi = models.PositiveIntegerField(verbose_name='Kelengkapan Unsur Isi Buku')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan Unsur Isi Buku')
    pembahasan = models.PositiveIntegerField(verbose_name='Ruang Lingkup dan Kedalaman Pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')
    informasi = models.PositiveIntegerField(verbose_name='Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    kualitas_penerbit = models.PositiveIntegerField(verbose_name='Kelengkapan Unsur dan Kualitas Penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')
    total = models.PositiveIntegerField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_pu = models.PositiveIntegerField(verbose_name='Nilai Pemegang Berkas Utama', blank=True, null=True)
    nilai_pl = models.PositiveIntegerField(verbose_name='Nilai Pemegang Berkas Lainnya', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.berkas}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.berkas)
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.berkas.penulis_lain.all().exists() == False:
            self.nilai_pu = self.total
        else:
            self.nilai_pu = self.total * 0.8
            self.nilai_pl = self.total * 0.2 / self.berkas.jmlh_penulis_lain
        super(PenilaianBerkasHaki, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_haki', kwargs= url_slug)

class PlagiasiLinieritas(models.Model):
    jurnal = models.OneToOneField(UploadBerkasJurnal, on_delete=models.CASCADE, related_name='plagiasi_linieritas')
    plagiasi = models.TextField(verbose_name='Komentar Plagiasi')
    linieritas = models.TextField(verbose_name='Komentar Linieritas')
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.jurnal}"

    def save(self):
        self.slug = slugify(self.jurnal)
        super().save()

    def get_absolute_url(self):
        url_slug = {'slug':self.jurnal}
        return reverse('penilaian:rekap_jurnal', kwargs= url_slug)

    
######################################################################################################3
def get_name(self):
    return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_name)

