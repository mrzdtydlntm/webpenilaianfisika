from django.db import models
from django.contrib.auth.models import User
from django.utils import tree
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Users(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    pangkat = models.CharField(max_length=70, verbose_name='Pangkat/Golongan/Ruang', default=None)
    jabatan = models.CharField(max_length=70, verbose_name='Jabatan Fungsional', default=None)
    unit = models.CharField(max_length=100, verbose_name='Unit Kerja', default=None)

    def __str__(self):
        return f"{self.users}"

class Reviewer(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Reviewer')
    nama_lengkap = models.CharField(max_length=150, verbose_name='Nama Lengkap dan Gelar')
    nip = models.CharField(max_length=18, verbose_name='Nomor Induk Pegawai', default=None)
    unit_kerja = models.CharField(max_length=100, verbose_name='Unit Kerja')
    bidang_ilmu = models.CharField(max_length=100, verbose_name='Bidang Ilmu')
    jabatan_pangkat = models.CharField(max_length=100, verbose_name='Jabatan/Pangkat')
    ttd = models.ImageField(upload_to='ttd/', verbose_name='Upload Tanda Tangan', default=None, blank=True)

    def __str__(self):
        return f"{self.nama_lengkap}"

class Admin(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.admin}"

class PenulisLain(models.Model):
    penulis = models.CharField(max_length=100, verbose_name='Penulis Lain')

    def __str__(self):
        return f"{self.penulis}"

class UploadBerkasJurnal(models.Model):
    pengusul = models.ForeignKey(Users  , related_name='user_pengusul_jurnal', on_delete=models.CASCADE, verbose_name='Pengusul')
    judul_artikel = models.CharField(max_length=255, verbose_name='Judul Artikel', unique=True)
    jmlh_penulis = models.PositiveIntegerField(verbose_name='Jumlah Penulis')
    nama_jurnal = models.CharField(max_length=255, verbose_name='Nama Jurnal')
    nomor_issn = models.CharField(max_length=255, verbose_name='Nomor ISSN', null=True, blank=True)
    vol_no_bln_thn = models.CharField(max_length=255, verbose_name='Volume/No/Bulan/Tahun', null=True, blank=True)
    penerbit = models.CharField(max_length=255, verbose_name='Penerbit', null=True, blank=True)
    doi_artikel = models.CharField(max_length=255, verbose_name='DOI Artikel', null=True, blank=True)
    url_jurnal = models.CharField(max_length=150,verbose_name='Link Jurnal', null=True, blank=True)
    indeks = [
        ('Scopus dan Scimagojr','Scopus dan Scimagojr'),
        ('Scopus atau IEEE','Scopus atau IEEE'),
        ('Google Scholar','Google Scholar'),
        ('Discontinued dan Cancelled','Discontinued dan Cancelled'),
        ('Tidak Terindeks','Tidak Terindeks'),
    ]
    indeks_jurnal = models.CharField(choices=indeks,max_length=100, verbose_name='Indeks Jurnal')
    tingkat_jurnal = models.CharField(max_length=100, verbose_name='Tingkat Jurnal', null=True, blank=True)
    kategori = [
        ('Jurnal Ilmiah Internasional Bereputasi Berdampak','Jurnal Ilmiah Internasional Bereputasi Berdampak'),
        ('Jurnal Ilmiah Internasional Bereputasi','Jurnal Ilmiah Internasional Bereputasi'),
        ('Jurnal Ilmiah Internasional','Jurnal Ilmiah Internasional'),
        ('Jurnal Ilmiah Nasional Terakreditasi','Jurnal Ilmiah Nasional Terakreditasi'),
        ('Jurnal Ilmiah Nasional Berbahasa PBB','Jurnal Ilmiah Nasional Berbahasa PBB'),
        ('Jurnal Ilmiah Nasional Tidak Terakreditasi','Jurnal Ilmiah Nasional Tidak Terakreditasi'),
        ('Jurnal Ilmiah Nasional terindeks di DOAJ dll','Jurnal Ilmiah Nasional terindeks di DOAJ dll'),
    ]
    kategori_publikasi = models.CharField(max_length=100, choices=kategori, default=None, verbose_name='Kategori Publikasi')
    upload_jurnal = models.FileField(upload_to='jurnal/isi/', verbose_name='Upload Jurnal')
    upload_cover = models.FileField(upload_to='jurnal/cover/', verbose_name='Upload Jurnal (cover)', blank=True, null=True)
    penulis_utama = models.ForeignKey(Users, related_name='user_jurnal_penulis_utama', on_delete=models.CASCADE, verbose_name='Penulis Utama', null=True, blank=True)
    penulis_utama_selain = models.ForeignKey(PenulisLain, on_delete=models.CASCADE, related_name='pu_selain', null=True, blank=True, verbose_name='Penulis Utama (selain Dosen)')
    corresponding_author = models.ForeignKey(Users, related_name='user_jurnal_corresponding_author', on_delete=models.CASCADE, verbose_name='Corresponding Author', null=True, blank=True)
    corresponding_author_selain = models.ForeignKey(PenulisLain, on_delete=models.CASCADE, related_name='ca_selain', null=True, blank=True, verbose_name='Corresponding Author (selain Dosen)')
    penulis_lain = models.ManyToManyField(Users, blank=True)
    penulis_selain = models.ManyToManyField(PenulisLain, verbose_name='Penulis Lain Selain Dosen', blank=True)
    plagiasi = models.PositiveIntegerField(verbose_name='Similarity Index', null=True, blank=True)
    bukti_plagiasi = models.FileField(upload_to='plagiasi/', verbose_name='Upload Bukti Plagiasi', blank=True, null=True)
    linier = [
        ('Linier dengan bidang penulis', 'Linier dengan bidang penulis'),
        ('Tidak linier dengan bidang penulis', 'Tidak linier dengan bidang penulis'),
    ]
    linieritas = models.TextField(choices=linier,verbose_name='Linieritas', null=True, blank=True)
    is_verificated = models.BooleanField(default=None, blank=True, null=True)
    reviewer = models.ForeignKey(Reviewer, related_name='user_jurnal_reviewer', on_delete=models.CASCADE, blank=True, null=True, default=None)
    reviewer_2 = models.ForeignKey(Reviewer, related_name='user_jurnal_reviewer2', on_delete=models.CASCADE, blank=True, null=True, default=None)
    uploaded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.judul_artikel}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul_artikel)
        super(UploadBerkasJurnal, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:detail_berkas_jurnal', kwargs=url_slug)
        

class UploadBerkasProsiding(models.Model):
    pengusul = models.ForeignKey(Users  , related_name='user_pengusul_prosiding', on_delete=models.CASCADE, verbose_name='Pengusul')
    judul_artikel = models.CharField(max_length=255, verbose_name='Judul Artikel', unique=True)
    jmlh_penulis = models.PositiveIntegerField(verbose_name='Jumlah Penulis')
    nama_prosiding = models.CharField(max_length=255, verbose_name='Nama Prosiding', null=True, blank=True)
    nomor_isbn = models.CharField(max_length=255, verbose_name='Nomor ISBN', null=True, blank=True)
    tahun_terbit = models.CharField(max_length=255, verbose_name='Tahun Terbit', null=True, blank=True)
    penerbit = models.CharField(max_length=255, verbose_name='Penerbit', null=True, blank=True)
    url_repository = models.CharField(max_length=150,verbose_name='Link Repository', null=True, blank=True)
    indeks = [
        ('Scopus dan Scimagojr','Scopus dan Scimagojr'),
        ('Scopus atau IEEE','Scopus atau IEEE'),
        ('Google Scholar','Google Scholar'),
        ('Discontinued dan Cancelled','Discontinued dan Cancelled'),
        ('Tidak Terindeks','Tidak Terindeks'),
    ]
    indeks_prosiding = models.CharField(choices=indeks, max_length=255, verbose_name='Terindeks di')
    tingkat = [
        ('Internasional','Internasional'),
        ('Nasional','Nasional'),
    ]
    kategori = [
        ('Presentasi Oral dan Dipublikasikan','Presentasi Oral dan Dipublikasikan'),
        ('Poster dan Dipublikasikan dalam Prosiding','Poster dan Dipublikasikan dalam Prosiding'),
        ('Diseminarkan Namun Tidak Terpublikasi','Diseminarkan Namun Tidak Terpublikasi'),
        ('Tidak Diseminarkan Namun Terpublikasi','Tidak Diseminarkan Namun Terpublikasi'),
        ('Terpublikasi dalam Koran/Majalah','Terpublikasi dalam Koran/Majalah'),
    ]
    kategori_publikasi = models.CharField(max_length=100, choices=kategori, default=None, verbose_name='Kategori Publikasi')
    tingkat_publikasi = models.CharField(max_length=100, choices=tingkat, default=None, verbose_name='Tingkat Publikasi')
    upload_prosiding = models.FileField(upload_to='prosiding/isi/', verbose_name='Upload Prosiding (isi)')
    upload_cover = models.FileField(upload_to='prosiding/cover/', verbose_name='Upload Prosiding (cover)', blank=True, null=True)
    penulis_utama = models.ForeignKey(Users, related_name='user_prosiding_penulis_utama', on_delete=models.CASCADE, verbose_name='Penulis Utama', null=True, blank=True)
    penulis_utama_selain = models.ForeignKey(PenulisLain, on_delete=models.CASCADE, related_name='pu_lain_prosiding', verbose_name='Penulis Utama Selain Dosen', blank=True, null=True)
    corresponding_author = models.ForeignKey(Users, related_name='user_prosiding_corresponding_author', on_delete=models.CASCADE, verbose_name='Corresponding Author', default=None, blank=True, null=True)
    corresponding_author_selain = models.ForeignKey(PenulisLain, on_delete=models.CASCADE, related_name='ca_lain_prosiding', verbose_name='Corresponding Author Selain Dosen', blank=True, null=True)
    penulis_lain = models.ManyToManyField(Users, blank=True)
    penulis_selain = models.ManyToManyField(PenulisLain, blank=True, verbose_name='Penulis Lain Selain Dosen',)
    is_verificated = models.BooleanField(default=None, blank=True, null=True)
    reviewer = models.ForeignKey(Reviewer, related_name='user_prosiding_reviewer', on_delete=models.CASCADE, blank=True, null=True, default=None)
    reviewer_2 = models.ForeignKey(Reviewer, related_name='user_prosiding_reviewer2', on_delete=models.CASCADE, blank=True, null=True, default=None)
    uploaded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.judul_artikel}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul_artikel)
        super(UploadBerkasProsiding, self).save(*args, **kwargs)

    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:detail_berkas_prosiding', kwargs=url_slug)

class UploadBerkasBuku(models.Model):
    pengusul = models.ForeignKey(Users  , related_name='user_pengusul_buku', on_delete=models.CASCADE, verbose_name='Pengusul')
    judul = models.CharField(max_length=255, verbose_name='Judul Buku')
    jmlh_penulis = models.PositiveIntegerField(verbose_name='Jumlah Penulis')
    nomor_isbn = models.CharField(max_length=255, verbose_name='Nomor ISBN', unique=True)
    edisi = models.CharField(max_length=255, verbose_name='Edisi', null=True, blank=True)
    tahun_terbit = models.CharField(max_length=255, verbose_name='Tahun Terbit', null=True, blank=True)
    penerbit = models.CharField(max_length=255, verbose_name='Penerbit', null=True, blank=True)
    jumlah_halaman = models.CharField(max_length=255, verbose_name='Jumlah Halaman', null=True, blank=True)
    kategori = [
        ('Buku Referensi','Buku Referensi'),
        ('Buku Monograf','Buku Monograf'),
        ('Book Chapter Internasional','Book Chapter Internasional'),
        ('Book Chapter Nasional','Book Chapter Nasional'),
    ]
    kategori_publikasi = models.CharField(max_length=100, choices=kategori, default=None, verbose_name='Kategori Publikasi')
    upload_buku = models.FileField(upload_to='buku/isi/', verbose_name='Upload Buku')
    penulis_utama = models.ForeignKey(Users, related_name='user_buku_penulis_utama', on_delete=models.CASCADE, verbose_name='Penulis Utama', default=None, blank=True, null=True)
    penulis_utama_selain = models.ForeignKey(PenulisLain, verbose_name='Penulis Utama Selain Dosen', related_name='pu_lain_buku', null=True, blank=True, on_delete=models.CASCADE)
    penulis_lain = models.ManyToManyField(Users, blank=True)
    penulis_lain_selain = models.ManyToManyField(PenulisLain, verbose_name='Penulis Lain Selain Dosen', blank=True)
    is_verificated = models.BooleanField(default=None, blank=True, null=True)
    reviewer = models.ForeignKey(Reviewer, related_name='user_buku_reviewer', on_delete=models.CASCADE, blank=True, null=True, default=None)
    reviewer_2 = models.ForeignKey(Reviewer, related_name='user_buku_reviewer2', on_delete=models.CASCADE, blank=True, null=True, default=None)
    uploaded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.judul}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul)
        super(UploadBerkasBuku, self).save(*args, **kwargs)

    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:detail_berkas_buku', kwargs=url_slug)

class UploadBerkasHaki(models.Model):
    pengusul = models.ForeignKey(Users  , related_name='user_pengusul_haki', on_delete=models.CASCADE, verbose_name='Pengusul')
    judul = models.CharField(max_length=255, verbose_name='Nama Berkas', unique=True)
    jmlh_penulis = models.PositiveIntegerField(verbose_name='Jumlah Pemegang Berkas')
    jenis = [
        ('Merek','Merek'),
        ('Paten','Paten'),
        ('Hak Cipta','Hak Cipta'),
        ('Desain Industri','Desain Industri'),
        ('Indikasi Geografis','Indikasi Geografis'),
        ('DTLST','DTLST'),
        ('Rahasia Dagang','Rahasia Dagang'),
    ]
    jenis_haki = models.CharField(max_length=50, choices=jenis, verbose_name='Jenis HaKI')
    nomor_paten = models.CharField(max_length=20, verbose_name='Nomor Paten', blank=True, null=True)
    tanggal = models.CharField(max_length=50, verbose_name='Tanggal Berkas', blank=True, null=True)
    penerbit = models.CharField(max_length=100, verbose_name='Penerbit', blank=True, null=True)
    status_paten = models.CharField(max_length=100, verbose_name='Status Paten', blank=True, null=True)
    url_repository = models.CharField(max_length=100, verbose_name='Alamat Repository', blank=True, null=True)
    kategori = [
        ('Internasional (sudah diimplementasikan di industri)','Internasional (sudah diimplementasikan di industri)'),
        ('Internasional','Internasional'),
        ('Nasional (sudah diimplementasikan di industri)','Nasional (sudah diimplementasikan di industri)'),
        ('Nasional','Nasional'),
        ('Karya cipta bersertifikat Dirjen','Karya cipta bersertifikat Dirjen'),
        ('Karya cipta bahan ajar','Karya cipta bahan ajar'),
    ]
    kategori_publikasi = models.CharField(max_length=100, choices=kategori, default=None, verbose_name='Kategori Publikasi')
    upload_berkas = models.FileField(upload_to='haki/isi/', verbose_name='Upload Berkas')
    pemegang_berkas_utama = models.ForeignKey(Users, related_name='user_pemegang_berkas_utama', on_delete=models.CASCADE, verbose_name='Pemegang Berkas Utama', default=None, blank=True, null=True)
    pemegang_berkas_utama_selain = models.ForeignKey(PenulisLain, verbose_name='Pemegang Berkas Utama Selain Dosen', related_name='pb_lain_haki', null=True, blank=True, on_delete=models.CASCADE)
    penulis_lain = models.ManyToManyField(Users, blank=True, verbose_name='Pemegang Berkas Lain')
    pemegang_berkas_selain = models.ManyToManyField(PenulisLain, verbose_name='Pemegang Berkas Selain Dosen', blank=True)
    is_verificated = models.BooleanField(default=None, blank=True, null=True)
    reviewer = models.ForeignKey(Reviewer, related_name='user_haki_reviewer', on_delete=models.CASCADE, blank=True, null=True, default=None)
    reviewer_2 = models.ForeignKey(Reviewer, related_name='user_haki_reviewer2', on_delete=models.CASCADE, blank=True, null=True, default=None)
    uploaded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.judul}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul)
        super(UploadBerkasHaki, self).save(*args, **kwargs)

    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:detail_berkas_haki', kwargs=url_slug)

class PenilaianBerkasJurnal(models.Model):
    jurnal = models.OneToOneField(UploadBerkasJurnal, on_delete=models.CASCADE)
    unsur_isi = models.FloatField(verbose_name='Nilai Kelengkapan dan Kesesuaian Unsur Isi Jurnal')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan dan Kesesuaian Unsur Isi Jurnal')
    pembahasan = models.FloatField(verbose_name='Nilai Ruang Lingkup dan Kedalaman Pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')
    informasi = models.FloatField(verbose_name='Nilai Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    kualitas_penerbit = models.FloatField(verbose_name='Nilai Kelengkapan Unsur dan Kualitas Penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')
    total = models.FloatField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_ca = models.FloatField(verbose_name='Nilai Corresponding Author', blank=True, null=True)
    nilai_pu = models.FloatField(verbose_name='Nilai Penulis Utama', blank=True, null=True)
    nilai_pl = models.FloatField(verbose_name='Nilai Penulis Lainnya', blank=True, null=True)
    jmlh_penulis_lain = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.jurnal}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.jurnal)
        if self.jurnal.penulis_lain.exists() or self.jurnal.penulis_selain.exists():
            if self.jurnal.corresponding_author == None and self.jurnal.corresponding_author_selain == None:
                self.jmlh_penulis_lain = self.jurnal.jmlh_penulis - 1
            else:
                self.jmlh_penulis_lain = self.jurnal.jmlh_penulis - 2
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.jurnal.corresponding_author != None or self.jurnal.corresponding_author_selain != None: #CA != PU
            if self.jmlh_penulis_lain == None:
                self.nilai_ca = self.total * 0.5
                self.nilai_pu = self.total * 0.5
            else:
                self.nilai_ca = self.total * 0.4
                self.nilai_pu = self.total * 0.4
                self.nilai_pl = self.total * 0.2 / self.jmlh_penulis_lain
        else: #CA = PU
            if self.jmlh_penulis_lain == None:
                self.nilai_pu = self.total
            else:
                self.nilai_pu = self.total * 0.6
                self.nilai_pl = self.total * 0.4 / self.jmlh_penulis_lain
        super(PenilaianBerkasJurnal, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_jurnal', kwargs=url_slug)

class PenilaianBerkasJurnal2(models.Model):
    jurnal = models.OneToOneField(UploadBerkasJurnal, on_delete=models.CASCADE)
    unsur_isi = models.FloatField(verbose_name='Nilai Kelengkapan dan Kesesuaian Unsur Isi Jurnal')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan dan Kesesuaian Unsur Isi Jurnal')
    pembahasan = models.FloatField(verbose_name='Nilai Ruang Lingkup dan Kedalaman Pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')
    informasi = models.FloatField(verbose_name='Nilai Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    kualitas_penerbit = models.FloatField(verbose_name='Nilai Kelengkapan Unsur dan Kualitas Penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')
    total = models.FloatField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_ca = models.FloatField(verbose_name='Nilai Corresponding Author', blank=True, null=True)
    nilai_pu = models.FloatField(verbose_name='Nilai Penulis Utama', blank=True, null=True)
    nilai_pl = models.FloatField(verbose_name='Nilai Penulis Lainnya', blank=True, null=True)
    jmlh_penulis_lain = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.jurnal}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.jurnal)
        if self.jurnal.penulis_lain.exists() or self.jurnal.penulis_selain.exists():
            if self.jurnal.corresponding_author == None and self.jurnal.corresponding_author_selain == None:
                self.jmlh_penulis_lain = self.jurnal.jmlh_penulis - 1
            else:
                self.jmlh_penulis_lain = self.jurnal.jmlh_penulis - 2
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.jurnal.corresponding_author != None or self.jurnal.corresponding_author_selain != None: #CA != PU
            if self.jmlh_penulis_lain == None:
                self.nilai_ca = self.total * 0.5
                self.nilai_pu = self.total * 0.5
            else:
                self.nilai_ca = self.total * 0.4
                self.nilai_pu = self.total * 0.4
                self.nilai_pl = self.total * 0.2 / self.jmlh_penulis_lain
        else: #CA = PU
            if self.jmlh_penulis_lain == None:
                self.nilai_pu = self.total
            else:
                self.nilai_pu = self.total * 0.6
                self.nilai_pl = self.total * 0.4 / self.jmlh_penulis_lain
        super(PenilaianBerkasJurnal2, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_jurnal', kwargs=url_slug)

class GabunganPenilaianBerkasJurnal(models.Model):
    nilai_1 = models.OneToOneField(PenilaianBerkasJurnal, on_delete=models.CASCADE)
    nilai_2 = models.OneToOneField(PenilaianBerkasJurnal2, on_delete=models.CASCADE)
    nilai_total_pu = models.FloatField(verbose_name='Nilai Total Penulis Utama')
    nilai_total_ca = models.FloatField(verbose_name='Nilai Total Penulis Korespondensi')
    nilai_total_pl = models.FloatField(verbose_name='Nilai Total Penulis Lainnya')

    def save(self, *args, **kwargs):
        self.nilai_total_pu = self.nilai_1.nilai_pu + self.nilai_2.nilai_pu
        self.nilai_total_ca = self.nilai_1.nilai_ca + self.nilai_2.nilai_ca
        self.nilai_total_pl = self.nilai_1.nilai_pl + self.nilai_2.nilai_pl
        super(GabunganPenilaianBerkasJurnal, self).save(*args, **kwargs)

class PenilaianBerkasProsiding(models.Model):
    prosiding = models.OneToOneField(UploadBerkasProsiding, on_delete=models.CASCADE)
    unsur_isi = models.FloatField(verbose_name='Nilai Kelengkapan dan Kesesuaian unsur isi prosiding')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan dan Kesesuaian unsur isi prosiding')
    pembahasan = models.FloatField(verbose_name='Nilai Ruang Lingkup dan Kedalaman Pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')
    informasi = models.FloatField(verbose_name='Nilai Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    kualitas_penerbit = models.FloatField(verbose_name='Nilai Kelengkapan Unsur dan Kualitas Penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')
    total = models.FloatField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_ca = models.FloatField(verbose_name='Nilai Corresponding Author', blank=True, null=True)
    nilai_pu = models.FloatField(verbose_name='Nilai Penulis Utama', blank=True, null=True)
    nilai_pl = models.FloatField(verbose_name='Nilai Penulis Lainnya', blank=True, null=True)
    jmlh_penulis_lain = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.prosiding}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.prosiding)
        if self.prosiding.penulis_lain.exists() or self.prosiding.penulis_selain.exists():
            if self.prosiding.corresponding_author == None and self.prosiding.corresponding_author_selain == None:
                self.jmlh_penulis_lain = self.prosiding.jmlh_penulis - 1
            else:
                self.jmlh_penulis_lain = self.prosiding.jmlh_penulis - 2
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.prosiding.corresponding_author != None: #CA != PU
            if self.jmlh_penulis_lain == None:
                self.nilai_ca = self.total * 0.5
                self.nilai_pu = self.total * 0.5
            else:
                self.nilai_ca = self.total * 0.4
                self.nilai_pu = self.total * 0.4
                self.nilai_pl = self.total * 0.2 / self.jmlh_penulis_lain
        else: #CA = PU
            if self.jmlh_penulis_lain == None:
                self.nilai_pu = self.total
            else:
                self.nilai_pu = self.total * 0.6
                self.nilai_pl = self.total * 0.4 / self.jmlh_penulis_lain
        super(PenilaianBerkasProsiding, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_prosiding', kwargs=url_slug)

class PenilaianBerkasProsiding2(models.Model):
    prosiding = models.OneToOneField(UploadBerkasProsiding, on_delete=models.CASCADE)
    unsur_isi = models.FloatField(verbose_name='Nilai Kelengkapan dan Kesesuaian unsur isi prosiding')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan dan Kesesuaian unsur isi prosiding')
    pembahasan = models.FloatField(verbose_name='Nilai Ruang Lingkup dan Kedalaman Pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')
    informasi = models.FloatField(verbose_name='Nilai Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    kualitas_penerbit = models.FloatField(verbose_name='Nilai Kelengkapan Unsur dan Kualitas Penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')
    total = models.FloatField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_ca = models.FloatField(verbose_name='Nilai Corresponding Author', blank=True, null=True)
    nilai_pu = models.FloatField(verbose_name='Nilai Penulis Utama', blank=True, null=True)
    nilai_pl = models.FloatField(verbose_name='Nilai Penulis Lainnya', blank=True, null=True)
    jmlh_penulis_lain = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.prosiding}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.prosiding)
        if self.prosiding.penulis_lain.exists() or self.prosiding.penulis_selain.exists():
            if self.prosiding.corresponding_author == None and self.prosiding.corresponding_author_selain == None:
                self.jmlh_penulis_lain = self.prosiding.jmlh_penulis - 1
            else:
                self.jmlh_penulis_lain = self.prosiding.jmlh_penulis - 2
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.prosiding.corresponding_author != None: #CA != PU
            if self.jmlh_penulis_lain == None:
                self.nilai_ca = self.total * 0.5
                self.nilai_pu = self.total * 0.5
            else:
                self.nilai_ca = self.total * 0.4
                self.nilai_pu = self.total * 0.4
                self.nilai_pl = self.total * 0.2 / self.jmlh_penulis_lain
        else: #CA = PU
            if self.jmlh_penulis_lain == None:
                self.nilai_pu = self.total
            else:
                self.nilai_pu = self.total * 0.6
                self.nilai_pl = self.total * 0.4 / self.jmlh_penulis_lain
        super(PenilaianBerkasProsiding2, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_prosiding', kwargs=url_slug)

class PenilaianBerkasBuku(models.Model):
    buku = models.OneToOneField(UploadBerkasBuku, on_delete=models.CASCADE)
    unsur_isi = models.FloatField(verbose_name='Nilai Kelengkapan Unsur Isi Buku')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan Unsur Isi Buku')
    pembahasan = models.FloatField(verbose_name='Nilai Ruang Lingkup dan Kedalaman Pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')
    informasi = models.FloatField(verbose_name='Nilai Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    kualitas_penerbit = models.FloatField(verbose_name='Nilai Kelengkapan Unsur dan Kualitas Penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')
    total = models.FloatField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_pu = models.FloatField(verbose_name='Nilai Penulis Utama', blank=True, null=True)
    nilai_pl = models.FloatField(verbose_name='Nilai Penulis Lainnya', blank=True, null=True)
    jmlh_penulis_lain = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.buku}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.buku)
        if self.buku.jmlh_penulis != 1:
            self.jmlh_penulis_lain = self.buku.jmlh_penulis - 1
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.jmlh_penulis_lain == None:
            self.nilai_pu = self.total
        else:
            self.nilai_pu = self.total * 0.8
            self.nilai_pl = self.total * 0.2 / self.jmlh_penulis_lain
        super(PenilaianBerkasBuku, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_buku', kwargs=url_slug)

class PenilaianBerkasBuku2(models.Model):
    buku = models.OneToOneField(UploadBerkasBuku, on_delete=models.CASCADE)
    unsur_isi = models.FloatField(verbose_name='Nilai Kelengkapan Unsur Isi Buku')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan Unsur Isi Buku')
    pembahasan = models.FloatField(verbose_name='Nilai Ruang Lingkup dan Kedalaman Pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')
    informasi = models.FloatField(verbose_name='Nilai Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    kualitas_penerbit = models.FloatField(verbose_name='Nilai Kelengkapan Unsur dan Kualitas Penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')
    total = models.FloatField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_pu = models.FloatField(verbose_name='Nilai Penulis Utama', blank=True, null=True)
    nilai_pl = models.FloatField(verbose_name='Nilai Penulis Lainnya', blank=True, null=True)
    jmlh_penulis_lain = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.buku}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.buku)
        if self.buku.jmlh_penulis != 1:
            self.jmlh_penulis_lain = self.buku.jmlh_penulis - 1
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.jmlh_penulis_lain == None:
            self.nilai_pu = self.total
        else:
            self.nilai_pu = self.total * 0.8
            self.nilai_pl = self.total * 0.2 / self.jmlh_penulis_lain
        super(PenilaianBerkasBuku2, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_buku')

class PenilaianBerkasHaki(models.Model):
    berkas = models.OneToOneField(UploadBerkasHaki, on_delete=models.CASCADE)
    unsur_isi = models.FloatField(verbose_name='Nilai Kelengkapan Unsur Isi Deskripsi')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan Unsur Isi Deskripsi')
    pembahasan = models.FloatField(verbose_name='Nilai Ruang Lingkup dan Kedalaman Pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')
    informasi = models.FloatField(verbose_name='Nilai Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    kualitas_penerbit = models.FloatField(verbose_name='Nilai Kelengkapan Unsur dan Kualitas Penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')
    total = models.FloatField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_pu = models.FloatField(verbose_name='Nilai Pemegang Berkas Utama', blank=True, null=True)
    nilai_pl = models.FloatField(verbose_name='Nilai Pemegang Berkas Lainnya', blank=True, null=True)
    jmlh_penulis_lain = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.berkas}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.berkas)
        if self.berkas.jmlh_penulis != 1:
            self.jmlh_penulis_lain = self.berkas.jmlh_penulis - 1
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.jmlh_penulis_lain == None:
            self.nilai_pu = self.total
        else:
            self.nilai_pu = self.total * 0.8
            self.nilai_pl = self.total * 0.2 / self.jmlh_penulis_lain
        super(PenilaianBerkasHaki, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_haki', kwargs=url_slug)

class PenilaianBerkasHaki2(models.Model):
    berkas = models.OneToOneField(UploadBerkasHaki, on_delete=models.CASCADE)
    unsur_isi = models.FloatField(verbose_name='Nilai Kelengkapan Unsur Isi Deskripsi')
    cmnt_unsur_isi = models.TextField(verbose_name='Komentar Kelengkapan Unsur Isi Deskripsi')
    pembahasan = models.FloatField(verbose_name='Nilai Ruang Lingkup dan Kedalaman Pembahasan')
    cmnt_pembahasan = models.TextField(verbose_name='Komentar Ruang Lingkup dan Kedalaman Pembahasan')
    informasi = models.FloatField(verbose_name='Nilai Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    cmnt_informasi = models.TextField(verbose_name='Komentar Kecukupan dan Kemutahiran Data/Informasi dan Metodologi')
    kualitas_penerbit = models.FloatField(verbose_name='Nilai Kelengkapan Unsur dan Kualitas Penerbit')
    cmnt_kualitas_penerbit = models.TextField(verbose_name='Komentar Kelengkapan Unsur dan Kualitas Penerbit')
    total = models.FloatField(verbose_name='Total Nilai', blank=True, null=True)
    nilai_pu = models.FloatField(verbose_name='Nilai Pemegang Berkas Utama', blank=True, null=True)
    nilai_pl = models.FloatField(verbose_name='Nilai Pemegang Berkas Lainnya', blank=True, null=True)
    jmlh_penulis_lain = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, unique=True)

    def __str__(self):
        return f"{self.berkas}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.berkas)
        if self.berkas.jmlh_penulis != 1:
            self.jmlh_penulis_lain = self.berkas.jmlh_penulis - 1
        self.total = self.unsur_isi + self.pembahasan + self.informasi + self.kualitas_penerbit
        if self.jmlh_penulis_lain == None:
            self.nilai_pu = self.total
        else:
            self.nilai_pu = self.total * 0.8
            self.nilai_pl = self.total * 0.2 / self.jmlh_penulis_lain
        super(PenilaianBerkasHaki2, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('penilaian:rekap_haki', kwargs=url_slug)

    
######################################################################################################3
def get_name(self):
    return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_name)

