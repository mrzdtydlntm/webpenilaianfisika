from django import forms
from .models import *

class UploadBerkasJurnalForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasJurnal
        fields = [
            'judul',
            'jmlh_penulis',
            'nomor_issn',
            'vol_no_bln_thn',
            'penerbit',
            'doi_artikel',
            'url_jurnal',
            'indeks_jurnal',
            'kategori_publikasi',
            'upload_jurnal',
            'upload_cover',
            'corresponding_author',
            'penulis_utama',
            'penulis_lain',
        ]
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_issn':forms.TextInput(attrs={'class':'form-control'}),
            'vol_no_bln_thn':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'doi_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'url_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'corresponding_author':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class VerifikasiBerkasJurnalForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasJurnal
        fields = [
            'judul',
            'jmlh_penulis',
            'nomor_issn',
            'vol_no_bln_thn',
            'penerbit',
            'doi_artikel',
            'url_jurnal',
            'indeks_jurnal',
            'kategori_publikasi',
            'upload_jurnal',
            'upload_cover',
            'corresponding_author',
            'penulis_utama',
            'penulis_lain',
            'is_verificated',
            'reviewer'
        ]
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_issn':forms.TextInput(attrs={'class':'form-control'}),
            'vol_no_bln_thn':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'doi_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'url_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'corresponding_author':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh'}),
            'reviewer':forms.Select(attrs={'class':'form-control mh'})
        }

class PlagiasiLinieritasForm(forms.ModelForm):
    class Meta:
        model = PlagiasiLinieritas
        fields = [
            'jurnal',
            'plagiasi',
            'linieritas',
        ]
        widgets = {
            'jurnal':forms.Select(attrs={'class':'form-control'}),
            'plagiasi':forms.Textarea(attrs={'class':'form-control'}),
            'linieritas':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasJurnalForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasJurnal
        fields = [
            'jurnal',
            'unsur_isi',
            'cmnt_unsur_isi',
            'pembahasan',
            'cmnt_pembahasan',
            'informasi',
            'cmnt_informasi',
            'kualitas_penerbit',
            'cmnt_kualitas_penerbit',
        ]
        widgets = {
            'jurnal':forms.Select(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks'}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

################### End of Jurnal ######################
        
class UploadBerkasProsidingForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasProsiding
        fields = [
            'judul',
            'jmlh_penulis',
            'nomor_isbn',
            'tahun_terbit',
            'penerbit',
            'url_repository',
            'indeks_prosiding',
            'kategori_publikasi',
            'tingkat_publikasi',
            'upload_prosiding',
            'upload_cover',
            'corresponding_author',
            'penulis_utama',
            'penulis_lain',
        ]
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_isbn':forms.TextInput(attrs={'class':'form-control'}),
            'tahun_terbit':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'url_repository':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_prosiding':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'tingkat_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'corresponding_author':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class VerifikasiBerkasProsidingForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasProsiding
        fields = [
            'judul',
            'jmlh_penulis',

            'nomor_isbn',
            'tahun_terbit',
            'penerbit',
            'url_repository',
            'indeks_prosiding',
            'kategori_publikasi',
            'tingkat_publikasi',
            'upload_prosiding',
            'upload_cover',
            'corresponding_author',
            'penulis_utama',
            'penulis_lain',
            'is_verificated',
            'reviewer'
        ]
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_isbn':forms.TextInput(attrs={'class':'form-control'}),
            'tahun_terbit':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'url_repository':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_prosiding':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'tingkat_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'corresponding_author':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh'}),
            'reviewer':forms.Select(attrs={'class':'form-control mh'})
        }

class PenilaianBerkasProsidingForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasProsiding
        fields = [
            'prosiding',
            'unsur_isi',
            'cmnt_unsur_isi',
            'pembahasan',
            'cmnt_pembahasan',
            'informasi',
            'cmnt_informasi',
            'kualitas_penerbit',
            'cmnt_kualitas_penerbit',
        ]
        widgets = {
            'prosiding':forms.Select(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks'}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

################### End of Prosiding ######################

class UploadBerkasBukuForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasBuku
        fields = [
            'judul',
            'jmlh_penulis',
            'nomor_isbn',
            'edisi',
            'tahun_terbit',
            'penerbit',
            'jumlah_halaman',
            'kategori_publikasi',
            'upload_buku',
            'penulis_utama',
            'penulis_lain',
        ]
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_isbn':forms.TextInput(attrs={'class':'form-control'}),
            'edisi':forms.TextInput(attrs={'class':'form-control'}),
            'tahun_terbit':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'jumlah_halaman':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class VerifikasiBerkasBukuForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasBuku
        fields = [
            'judul',
            'jmlh_penulis',

            'nomor_isbn',
            'edisi',
            'tahun_terbit',
            'penerbit',
            'jumlah_halaman',
            'kategori_publikasi',
            'upload_buku',
            'penulis_utama',
            'penulis_lain',
            'is_verificated',
            'reviewer'
        ]
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_issn':forms.TextInput(attrs={'class':'form-control'}),
            'vol_no_bln_thn':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'doi_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'url_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'corresponding_author':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh'}),
            'reviewer':forms.Select(attrs={'class':'form-control mh'})
        }

class PenilaianBerkasBukuForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasBuku
        fields = [
            'buku',
            'unsur_isi',
            'cmnt_unsur_isi',
            'pembahasan',
            'cmnt_pembahasan',
            'informasi',
            'cmnt_informasi',
            'kualitas_penerbit',
            'cmnt_kualitas_penerbit',
        ]
        widgets = {
            'buku':forms.Select(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks'}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

################### End of Buku ######################

class UploadBerkasHakiForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasHaki
        fields = [
            'judul',
            'jmlh_penulis',
            'kategori_publikasi',
            'upload_berkas',
            'pemegang_berkas_utama',
            'penulis_lain',
        ]
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'pemegang_berkas_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class VerifikasiBerkasHakiForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasHaki
        fields = [
            'judul',
            'jmlh_penulis',

            'kategori_publikasi',
            'upload_berkas',
            'pemegang_berkas_utama',
            'penulis_lain',
            'is_verificated',
            'reviewer'
        ]
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'pemegang_berkas_utama':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh'}),
            'reviewer':forms.Select(attrs={'class':'form-control mh'})
        }

class PenilaianBerkasHakiForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasHaki
        fields = [
            'berkas',
            'unsur_isi',
            'cmnt_unsur_isi',
            'pembahasan',
            'cmnt_pembahasan',
            'informasi',
            'cmnt_informasi',
            'kualitas_penerbit',
            'cmnt_kualitas_penerbit',
        ]
        widgets = {
            'berkas':forms.Select(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks'}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks'}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }
    
################### End of Haki ######################

