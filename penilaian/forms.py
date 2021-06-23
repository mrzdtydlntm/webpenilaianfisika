from django import forms
from django.forms import fields, widgets
from .models import *

class EditDataDiriForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            'pangkat',
            'jabatan',
            'unit',
        ]
        widgets = {
            'pangkat':forms.TextInput(attrs={'class':'form-control'}),
            'jabatan':forms.TextInput(attrs={'class':'form-control'}),
            'unit':forms.TextInput(attrs={'class':'form-control'}),
        }

class UploadBerkasJurnalForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasJurnal
        fields = [
            'pengusul',
            'judul_artikel',
            'jmlh_penulis',
            'nama_jurnal',
            'nomor_issn',
            'vol_no_bln_thn',
            'penerbit',
            'doi_artikel',
            'url_jurnal',
            'indeks_jurnal',
            'tingkat_jurnal',
            'kategori_publikasi',
            'upload_jurnal',
            'upload_cover',
            'penulis_utama',
            'penulis_utama_selain',
            'corresponding_author',
            'corresponding_author_selain',
            'penulis_lain',
            'penulis_selain',
        ]
        widgets = {
            'pengusul':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'judul_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nama_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_issn':forms.TextInput(attrs={'class':'form-control'}),
            'vol_no_bln_thn':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'doi_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'url_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_jurnal':forms.Select(attrs={'class':'form-control'}),
            'tingkat_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'corresponding_author':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'corresponding_author_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class EditBerkasJurnalForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasJurnal
        fields = [
            'judul_artikel',
            'jmlh_penulis',
            'nama_jurnal',
            'nomor_issn',
            'vol_no_bln_thn',
            'penerbit',
            'doi_artikel',
            'url_jurnal',
            'indeks_jurnal',
            'tingkat_jurnal',
            'kategori_publikasi',
            'upload_jurnal',
            'upload_cover',
            'penulis_utama',
            'penulis_utama_selain',
            'corresponding_author',
            'corresponding_author_selain',
            'penulis_lain',
            'penulis_selain'
        ]
        widgets = {
            'judul_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nama_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_issn':forms.TextInput(attrs={'class':'form-control'}),
            'vol_no_bln_thn':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'doi_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'url_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_jurnal':forms.Select(attrs={'class':'form-control'}),
            'tingkat_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'corresponding_author':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'corresponding_author_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class PlagiasiLinieritasForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasJurnal
        fields = [
            'judul_artikel',
            'plagiasi',
            'linieritas',
            'bukti_plagiasi',
        ]
        widgets = {
            'judul_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'plagiasi':forms.TextInput(attrs={'class':'form-control'}),
            'linieritas':forms.Select(attrs={'class':'form-control mh'}),
        }

class VerifikasiBerkasJurnalForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasJurnal
        fields = [
            'pengusul',
            'judul_artikel',
            'jmlh_penulis',
            'nama_jurnal',
            'nomor_issn',
            'vol_no_bln_thn',
            'penerbit',
            'doi_artikel',
            'url_jurnal',
            'indeks_jurnal',
            'tingkat_jurnal',
            'kategori_publikasi',
            'upload_jurnal',
            'upload_cover',
            'penulis_utama',
            'penulis_utama_selain',
            'corresponding_author',
            'corresponding_author_selain',
            'penulis_lain',
            'penulis_selain',
            'is_verificated',
            'reviewer',
            'reviewer_2'
        ]
        widgets = {
            'pengusul':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'judul_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nama_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_issn':forms.TextInput(attrs={'class':'form-control'}),
            'vol_no_bln_thn':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'doi_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'url_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_jurnal':forms.Select(attrs={'class':'form-control'}),
            'tingkat_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'corresponding_author':forms.Select(attrs={'class':'form-control mh'}),
            'corresponding_author_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh'}),
            'penulis_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'reviewer':forms.Select(attrs={'class':'form-control mh'}),
            'reviewer_2':forms.Select(attrs={'class':'form-control mh'}),
        }

class PenilaianBerkasJurnalForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasJurnal
        fields = [
            'jurnal',
            'plagiasi',
            'linieritas',
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
            'jurnal':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'plagiasi':forms.TextInput(attrs={'class':'form-control'}),
            'linieritas':forms.TextInput(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':4}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasJurnal2Form(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasJurnal2
        fields = [
            'jurnal',
            'plagiasi',
            'linieritas',
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
            'jurnal':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'plagiasi':forms.TextInput(attrs={'class':'form-control'}),
            'linieritas':forms.TextInput(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':4}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasJurnalEditForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasJurnal
        fields = [
            'jurnal',
            'plagiasi',
            'linieritas',
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
            'jurnal':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'plagiasi':forms.TextInput(attrs={'class':'form-control'}),
            'linieritas':forms.TextInput(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':4}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasJurnal2EditForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasJurnal2
        fields = [
            'jurnal',
            'plagiasi',
            'linieritas',
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
            'jurnal':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'plagiasi':forms.TextInput(attrs={'class':'form-control'}),
            'linieritas':forms.TextInput(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':4}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

################### End of Jurnal ######################
        
class UploadBerkasProsidingForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasProsiding
        fields = [
            'pengusul',
            'judul_artikel',
            'jmlh_penulis',
            'nama_prosiding',
            'nomor_isbn',
            'tahun_terbit',
            'penerbit',
            'url_repository',
            'indeks_prosiding',
            'kategori_publikasi',
            'tingkat_publikasi',
            'upload_prosiding',
            'upload_cover',
            'penulis_utama',
            'penulis_utama_selain',
            'corresponding_author',
            'corresponding_author_selain',
            'penulis_lain',
            'penulis_selain',
        ]
        widgets = {
            'pengusul':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'judul_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nama_prosiding':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_isbn':forms.TextInput(attrs={'class':'form-control'}),
            'tahun_terbit':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'url_repository':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_prosiding':forms.Select(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'tingkat_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'corresponding_author':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'corresponding_author_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class EditBerkasProsidingForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasProsiding
        fields = [
            'judul_artikel',
            'jmlh_penulis',
            'nama_prosiding',
            'nomor_isbn',
            'tahun_terbit',
            'penerbit',
            'url_repository',
            'indeks_prosiding',
            'kategori_publikasi',
            'tingkat_publikasi',
            'upload_prosiding',
            'upload_cover',
            'penulis_utama',
            'penulis_utama_selain',
            'corresponding_author',
            'corresponding_author_selain',
            'penulis_lain',
            'penulis_selain',
        ]
        widgets = {
            'judul_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nama_prosiding':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_isbn':forms.TextInput(attrs={'class':'form-control'}),
            'tahun_terbit':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'url_repository':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_prosiding':forms.Select(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'tingkat_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'corresponding_author':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'corresponding_author_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class PlagiasiLinieritasProsidingForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasProsiding
        fields = [
            'judul_artikel',
            'plagiasi',
            'bukti_plagiasi',
        ]
        widgets = {
            'judul_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'plagiasi':forms.TextInput(attrs={'class':'form-control'}),
        }

class VerifikasiBerkasProsidingForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasProsiding
        fields = [
            'pengusul',
            'judul_artikel',
            'jmlh_penulis',
            'nama_prosiding',
            'nomor_isbn',
            'tahun_terbit',
            'penerbit',
            'url_repository',
            'indeks_prosiding',
            'kategori_publikasi',
            'tingkat_publikasi',
            'upload_prosiding',
            'upload_cover',
            'penulis_utama',
            'penulis_utama_selain',
            'corresponding_author',
            'corresponding_author_selain',
            'penulis_lain',
            'penulis_selain',
            'is_verificated',
            'reviewer',
            'reviewer_2'
        ]
        widgets = {
            'pengusul':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'judul_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nama_prosiding':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_isbn':forms.TextInput(attrs={'class':'form-control'}),
            'tahun_terbit':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'url_repository':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_prosiding':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'tingkat_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'corresponding_author':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'corresponding_author_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'reviewer':forms.Select(attrs={'class':'form-control mh'}),
            'reviewer_2':forms.Select(attrs={'class':'form-control mh'}),
        }

class PenilaianBerkasProsidingForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasProsiding
        fields = [
            'prosiding',
            'plagiasi',
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
            'prosiding':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'plagiasi':forms.TextInput(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':3}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasProsiding2Form(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasProsiding2
        fields = [
            'prosiding',
            'plagiasi',
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
            'prosiding':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'plagiasi':forms.TextInput(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':3}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasProsidingEditForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasProsiding
        fields = [
            'prosiding',
            'plagiasi',
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
            'prosiding':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'plagiasi':forms.TextInput(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':3}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasProsiding2EditForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasProsiding2
        fields = [
            'prosiding',
            'plagiasi',
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
            'prosiding':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'plagiasi':forms.TextInput(attrs={'class':'form-control'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':3}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':9}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

################### End of Prosiding ######################

class UploadBerkasBukuForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasBuku
        fields = [
            'pengusul',
            'judul',
            'jmlh_penulis',
            'nomor_isbn',
            'edisi',
            'volume',
            'tahun_terbit',
            'penerbit',
            'jumlah_halaman',
            'kategori_publikasi',
            'upload_buku',
            'penulis_utama',
            'penulis_utama_selain',
            'penulis_lain',
            'penulis_lain_selain',
        ]
        widgets = {
            'pengusul':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_isbn':forms.TextInput(attrs={'class':'form-control'}),
            'edisi':forms.TextInput(attrs={'class':'form-control'}),
            'volume':forms.TextInput(attrs={'class':'form-control'}),
            'tahun_terbit':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_issn':forms.TextInput(attrs={'class':'form-control'}),
            'vol_no_bln_thn':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'doi_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'url_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_jurnal':forms.Select(attrs={'class':'form-control'}),
            'jumlah_halaman':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class EditBerkasBukuForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasBuku
        fields = [
            'judul',
            'jmlh_penulis',
            'nomor_isbn',
            'edisi',
            'volume',
            'tahun_terbit',
            'penerbit',
            'jumlah_halaman',
            'kategori_publikasi',
            'upload_buku',
            'penulis_utama',
            'penulis_utama_selain',
            'penulis_lain',
            'penulis_lain_selain',
        ]
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_isbn':forms.TextInput(attrs={'class':'form-control'}),
            'edisi':forms.TextInput(attrs={'class':'form-control'}),
            'volume':forms.TextInput(attrs={'class':'form-control'}),
            'tahun_terbit':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_issn':forms.TextInput(attrs={'class':'form-control'}),
            'vol_no_bln_thn':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'doi_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'url_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_jurnal':forms.Select(attrs={'class':'form-control'}),
            'jumlah_halaman':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class VerifikasiBerkasBukuForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasBuku
        fields = [
            'pengusul',
            'judul',
            'jmlh_penulis',
            'nomor_isbn',
            'edisi',
            'volume',
            'tahun_terbit',
            'penerbit',
            'jumlah_halaman',
            'kategori_publikasi',
            'upload_buku',
            'penulis_utama',
            'penulis_utama_selain',
            'penulis_lain',
            'penulis_lain_selain',
            'is_verificated',
            'reviewer',
            'reviewer_2'
        ]
        widgets = {
            'pengusul':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_isbn':forms.TextInput(attrs={'class':'form-control'}),
            'edisi':forms.TextInput(attrs={'class':'form-control'}),
            'volume':forms.TextInput(attrs={'class':'form-control'}),
            'tahun_terbit':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_issn':forms.TextInput(attrs={'class':'form-control'}),
            'vol_no_bln_thn':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'doi_artikel':forms.TextInput(attrs={'class':'form-control'}),
            'url_jurnal':forms.TextInput(attrs={'class':'form-control'}),
            'indeks_jurnal':forms.Select(attrs={'class':'form-control'}),
            'jumlah_halaman':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'penulis_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'reviewer':forms.Select(attrs={'class':'form-control mh'}),
            'reviewer_2':forms.Select(attrs={'class':'form-control mh'}),
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
            'buku':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':4}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasBuku2Form(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasBuku2
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
            'buku':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':4}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasBukuEditForm(forms.ModelForm):
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
            'buku':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':4}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasBuku2EditForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasBuku2
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
            'buku':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':4}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':12}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

################### End of Buku ######################

class UploadBerkasHakiForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasHaki
        fields = [
            'pengusul',
            'judul',
            'jmlh_penulis',
            'jenis_haki',
            'nomor_paten',
            'tanggal',
            'penerbit',
            'status_paten',
            'url_repository',
            'kategori_publikasi',
            'upload_berkas',
            'pemegang_berkas_utama',
            'pemegang_berkas_utama_selain',
            'penulis_lain',
            'pemegang_berkas_selain',
        ]
        widgets = {
            'pengusul':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'jenis_haki':forms.Select(attrs={'class':'form-control'}),
            'nomor_paten':forms.TextInput(attrs={'class':'form-control'}),
            'tanggal':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'status_paten':forms.TextInput(attrs={'class':'form-control'}),
            'url_repository':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'pemegang_berkas_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'pemegang_berkas_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'pemegang_berkas_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class EditBerkasHakiForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasHaki
        fields = [
            'judul',
            'jmlh_penulis',
            'jenis_haki',
            'nomor_paten',
            'tanggal',
            'penerbit',
            'status_paten',
            'url_repository',
            'kategori_publikasi',
            'upload_berkas',
            'pemegang_berkas_utama',
            'pemegang_berkas_utama_selain',
            'penulis_lain',
            'pemegang_berkas_selain',
        ]
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'jenis_haki':forms.Select(attrs={'class':'form-control'}),
            'nomor_paten':forms.TextInput(attrs={'class':'form-control'}),
            'tanggal':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'status_paten':forms.TextInput(attrs={'class':'form-control'}),
            'url_repository':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'pemegang_berkas_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'pemegang_berkas_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'pemegang_berkas_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
        }

class VerifikasiBerkasHakiForm(forms.ModelForm):
    class Meta:
        model = UploadBerkasHaki
        fields = [
            'pengusul',
            'judul',
            'jmlh_penulis',
            'jenis_haki',
            'nomor_paten',
            'tanggal',
            'penerbit',
            'status_paten',
            'url_repository',
            'kategori_publikasi',
            'upload_berkas',
            'pemegang_berkas_utama',
            'pemegang_berkas_utama_selain',
            'penulis_lain',
            'pemegang_berkas_selain',
            'is_verificated',
            'reviewer',
            'reviewer_2'
        ]
        widgets = {
            'pengusul':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'jmlh_penulis':forms.TextInput(attrs={'class':'form-control'}),
            'jenis_haki':forms.Select(attrs={'class':'form-control'}),
            'nomor_paten':forms.TextInput(attrs={'class':'form-control'}),
            'tanggal':forms.TextInput(attrs={'class':'form-control'}),
            'penerbit':forms.TextInput(attrs={'class':'form-control'}),
            'status_paten':forms.TextInput(attrs={'class':'form-control'}),
            'url_repository':forms.TextInput(attrs={'class':'form-control'}),
            'kategori_publikasi':forms.Select(attrs={'class':'form-control mh'}),
            'pemegang_berkas_utama':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'pemegang_berkas_utama_selain':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'penulis_lain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'pemegang_berkas_selain':forms.SelectMultiple(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'reviewer':forms.Select(attrs={'class':'form-control mh'}),
            'reviewer_2':forms.Select(attrs={'class':'form-control mh'}),
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
            'berkas':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':6}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasHaki2Form(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasHaki2
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
            'berkas':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':6}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasHakiEditForm(forms.ModelForm):
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
            'berkas':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':6}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }

class PenilaianBerkasHaki2EditForm(forms.ModelForm):
    class Meta:
        model = PenilaianBerkasHaki2
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
            'berkas':forms.Select(attrs={'class':'form-control selectpicker border rounded mh', 'data-live-search':'True'}),
            'unsur_isi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 10% dari nilai maks', 'min':0, 'max':6}),
            'cmnt_unsur_isi':forms.Textarea(attrs={'class':'form-control'}),
            'pembahasan':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_pembahasan':forms.Textarea(attrs={'class':'form-control'}),
            'informasi':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_informasi':forms.Textarea(attrs={'class':'form-control'}),
            'kualitas_penerbit':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bobot 30% dari nilai maks', 'min':0, 'max':18}),
            'cmnt_kualitas_penerbit':forms.Textarea(attrs={'class':'form-control'}),
        }
    
################### End of Haki ######################

class PenulisLainForm(forms.ModelForm):
    class Meta:
        model = PenulisLain
        fields = [
            'penulis'
        ]
        widgets = {
            'penulis':forms.TextInput(attrs={'class':'form-control'})
        }
