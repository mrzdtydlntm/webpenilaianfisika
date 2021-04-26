from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import *
from django.shortcuts import render
from django.views.generic import ListView, CreateView, View
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .utils import render_to_pdf
from webfisika.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.

class UserView(ListView):
    model = Users
    template_name = 'penilaian/user_table.html'
    context_object_name = 'list_user'
################################################################################################################
class UploadBerkasJurnalView(LoginRequiredMixin, CreateView):
    model = UploadBerkasJurnal
    form_class = UploadBerkasJurnalForm
    template_name = 'penilaian/upload_berkas_jurnal.html'
    success_url = reverse_lazy('success')
    extra_context = {
        'form':form_class,
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

    def form_valid(self, form):
        nama_jurnal = form.cleaned_data.get('judul_artikel')
        subject = 'Konfirmasi Upload Berkas Jurnal'
        penerima = User.objects.get(pk=1)
        message = f'Terdapat jurnal bernama {nama_jurnal} telah diupload oleh user. Mohon untuk diperiksa. Terimakasih'
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return super(UploadBerkasJurnalView, self).form_valid(form)

class ListBerkasJurnalView(LoginRequiredMixin,ListView):
    model = UploadBerkasJurnal
    template_name = 'penilaian/list_berkas_jurnal.html'
    context_object_name = 'list_berkas_jurnal'
    nama_reviewer = Reviewer.objects.all()
    list_berkas = PenilaianBerkasJurnal.objects.all()
    extra_context = {
        'list_user':nama_reviewer,
        'list_berkas':list_berkas,
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class DetailBerkasJurnalView(LoginRequiredMixin,DetailView):
    model = UploadBerkasJurnal
    template_name = 'penilaian/detail_berkas_jurnal.html'
    context_object_name = 'detail_berkas_jurnal'

class EditBerkasJurnalView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasJurnal
    form_class = EditBerkasJurnalForm
    template_name = 'penilaian/edit_berkas_jurnal.html'
    success_url = reverse_lazy('penilaian:list_berkas_jurnal')

class PlagiasiLinieritasView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasJurnal
    form_class = PlagiasiLinieritasForm
    template_name = 'penilaian/plagiasi_linieritas.html'
    success_url = reverse_lazy('penilaian:list_berkas_jurnal')

class VerifikasiBerkasJurnalView(LoginRequiredMixin,UpdateView):
    model = UploadBerkasJurnal
    form_class = VerifikasiBerkasJurnalForm
    template_name = 'penilaian/verifikasi_berkas_jurnal.html'
    success_url = reverse_lazy('penilaian:list_berkas_jurnal')
    context_object_name = 'verifikasi_jurnal'

    def form_valid(self, form):
        nama_jurnal = form.cleaned_data.get('judul_artikel')
        reviewer = form.cleaned_data.get('reviewer')
        review = User.objects.get(first_name=reviewer)
        subject = 'Konfirmasi Review Jurnal'
        message = f'Terdapat jurnal dengan judul {nama_jurnal} telah diupload. Diharapkan bapak/ibu {reviewer} segera menilainya. Terimakasih'
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
        return super(VerifikasiBerkasJurnalView, self).form_valid(form)

class PenilaianBerkasJurnalView(LoginRequiredMixin,CreateView):
    model = PenilaianBerkasJurnal
    form_class = PenilaianBerkasJurnalForm
    template_name = 'penilaian/penilaian_berkas_jurnal.html'
    success_url = reverse_lazy('home')
    context_object_name = 'penilaian_berkas_jurnal'

class HasilPenilaianJurnalView(DetailView):
    model = PenilaianBerkasJurnal
    template_name = 'penilaian/hasil_rekap_jurnal.html'
    context_object_name = 'rekap_jurnal'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

############# End of Jurnal #############

class UploadBerkasProsidingView(LoginRequiredMixin, CreateView):
    model = UploadBerkasProsiding
    form_class = UploadBerkasProsidingForm
    template_name = 'penilaian/upload_berkas_prosiding.html'
    success_url = reverse_lazy('success')
    extra_context = {
        'form':form_class,
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs) 
    
    def form_valid(self, form):
        nama_prosiding = form.cleaned_data.get('judul_artikel')
        penerima = User.objects.get(pk=1)
        subject = 'Konfirmasi Upload Berkas Prosiding'
        message = f'Terdapat prosiding bernama {nama_prosiding} telah diupload oleh user. Mohon untuk diperiksa. Terimakasih'
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return super(UploadBerkasProsidingView, self).form_valid(form)

class ListBerkasProsidingView(LoginRequiredMixin,ListView):
    model = UploadBerkasProsiding
    template_name = 'penilaian/list_berkas_prosiding.html'
    context_object_name = 'list_berkas_prosiding'
    nama_reviewer = Reviewer.objects.all()
    list_berkas = PenilaianBerkasProsiding.objects.all()
    extra_context = {
        'list_user':nama_reviewer,
        'list_berkas':list_berkas,
    }
    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class DetailBerkasProsidingView(LoginRequiredMixin,DetailView):
    model = UploadBerkasProsiding
    template_name = 'penilaian/detail_berkas_prosiding.html'
    context_object_name = 'detail_berkas_prosiding'

class EditBerkasProsidingView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasProsiding
    form_class = EditBerkasProsidingForm
    template_name = 'penilaian/edit_berkas_prosiding.html'
    success_url = reverse_lazy('penilaian:list_berkas_prosiding')

class VerifikasiBerkasProsidingView(LoginRequiredMixin,UpdateView):
    model = UploadBerkasProsiding
    form_class = VerifikasiBerkasProsidingForm
    template_name = 'penilaian/verifikasi_berkas_prosiding.html'
    success_url = reverse_lazy('penilaian:list_berkas_prosiding')
    context_object_name = 'verifikasi_prosiding'
    
    def form_valid(self, form):
        nama_prosiding = form.cleaned_data.get('judul_artikel')
        reviewer = form.cleaned_data.get('reviewer')
        review = User.objects.get(first_name=reviewer)
        subject = 'Konfirmasi Review Prosiding'
        message = f'Terdapat prosiding dengan judul {nama_prosiding} telah diupload. Diharapkan bapak/ibu {reviewer} segera menilainya. Terimakasih'
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
        return super(VerifikasiBerkasProsidingView, self).form_valid(form)

class PenilaianBerkasProsidingView(LoginRequiredMixin,CreateView):
    model = PenilaianBerkasProsiding
    form_class = PenilaianBerkasProsidingForm
    template_name = 'penilaian/penilaian_berkas_prosiding.html'
    success_url = reverse_lazy('home')
    context_object_name = 'penilaian_berkas_prosiding'

class HasilPenilaianProsidingView(LoginRequiredMixin,DetailView):
    model = PenilaianBerkasProsiding
    template_name = 'penilaian/hasil_rekap_prosiding.html'
    context_object_name = 'rekap_prosiding'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

############# End of Prosiding #############

class UploadBerkasBukuView(LoginRequiredMixin, CreateView):
    model = UploadBerkasBuku
    form_class = UploadBerkasBukuForm
    template_name = 'penilaian/upload_berkas_buku.html'
    success_url = reverse_lazy('success')
    extra_context = {
        'form':form_class,
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)
    
    def form_valid(self, form):
        nama_buku = form.cleaned_data.get('judul_artikel')
        penerima = User.objects.get(pk=1)
        subject = 'Konfirmasi Upload Berkas Buku'
        message = f'Terdapat buku bernama {nama_buku} telah diupload oleh user. Mohon untuk diperiksa. Terimakasih'
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return super(UploadBerkasBukuView, self).form_valid(form)

class ListBerkasBukuView(LoginRequiredMixin,ListView):
    model = UploadBerkasBuku
    template_name = 'penilaian/list_berkas_buku.html'
    context_object_name = 'list_berkas_buku'
    nama_reviewer = Reviewer.objects.all()
    list_berkas = PenilaianBerkasBuku.objects.all()
    extra_context = {
        'list_user':nama_reviewer,
        'list_berkas':list_berkas,
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class DetailBerkasBukuView(LoginRequiredMixin,DetailView):
    model = UploadBerkasBuku
    template_name = 'penilaian/detail_berkas_buku.html'
    context_object_name = 'detail_berkas_buku'

class EditBerkasBukuView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasBuku
    form_class = EditBerkasBukuForm
    template_name = 'penilaian/edit_berkas_buku.html'
    success_url = reverse_lazy('penilaian:list_berkas_buku')

class VerifikasiBerkasBukuView(LoginRequiredMixin,UpdateView):
    model = UploadBerkasBuku
    form_class = VerifikasiBerkasBukuForm
    template_name = 'penilaian/verifikasi_berkas_buku.html'
    success_url = reverse_lazy('penilaian:list_berkas_buku')
    context_object_name = 'verifikasi_buku'

    def form_valid(self, form):
        nama_buku = form.cleaned_data.get('judul')
        reviewer = form.cleaned_data.get('reviewer')
        review = User.objects.get(first_name=reviewer)
        subject = 'Konfirmasi Review Buku'
        message = f'Terdapat buku dengan judul {nama_buku} telah diupload. Diharapkan bapak/ibu {reviewer} segera menilainya. Terimakasih'
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
        return super(VerifikasiBerkasBukuView, self).form_valid(form)

class PenilaianBerkasBukuView(LoginRequiredMixin,CreateView):
    model = PenilaianBerkasBuku
    form_class = PenilaianBerkasBukuForm
    template_name = 'penilaian/penilaian_berkas_buku.html'
    success_url = reverse_lazy('home')
    context_object_name = 'penilaian_berkas_buku'

class HasilPenilaianBukuView(LoginRequiredMixin,DetailView):
    model = PenilaianBerkasBuku
    template_name = 'penilaian/hasil_rekap_buku.html'
    context_object_name = 'rekap_buku'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

############# End of Buku #############

class UploadBerkasHakiView(LoginRequiredMixin, CreateView):
    model = UploadBerkasHaki
    form_class = UploadBerkasHakiForm
    template_name = 'penilaian/upload_berkas_haki.html'
    success_url = reverse_lazy('success')
    extra_context = {
        'form':form_class,
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

    def form_valid(self, form):
        nama_haki = form.cleaned_data.get('judul_artikel')
        penerima = User.objects.get(pk=1)
        subject = 'Konfirmasi Upload Berkas Haki'
        message = f'Terdapat berkas haki bernama {nama_haki} telah diupload oleh user. Mohon untuk diperiksa. Terimakasih'
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return super(UploadBerkasHakiView, self).form_valid(form)

class ListBerkasHakiView(LoginRequiredMixin,ListView):
    model = UploadBerkasHaki
    template_name = 'penilaian/list_berkas_haki.html'
    context_object_name = 'list_berkas_haki'
    nama_reviewer = Reviewer.objects.all()
    list_berkas = PenilaianBerkasHaki.objects.all()
    extra_context = {
        'list_user':nama_reviewer,
        'list_berkas':list_berkas,
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class DetailBerkasHakiView(LoginRequiredMixin,DetailView):
    model = UploadBerkasHaki
    template_name = 'penilaian/detail_berkas_haki.html'
    context_object_name = 'detail_berkas_haki'
    
class EditBerkasHakiView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasHaki
    form_class = EditBerkasHakiForm
    template_name = 'penilaian/edit_berkas_haki.html'
    success_url = reverse_lazy('penilaian:list_berkas_haki')

class VerifikasiBerkasHakiView(LoginRequiredMixin,UpdateView):
    model = UploadBerkasHaki
    form_class = VerifikasiBerkasHakiForm
    template_name = 'penilaian/verifikasi_berkas_haki.html'
    success_url = reverse_lazy('penilaian:list_berkas_haki')
    context_object_name = 'verifikasi_haki'

    def form_valid(self, form):
        nama_haki = form.cleaned_data.get('judul')
        reviewer = form.cleaned_data.get('reviewer')
        review = User.objects.get(first_name=reviewer)
        subject = 'Konfirmasi Review Haki'
        message = f'Terdapat haki dengan judul {nama_haki} telah diupload. Diharapkan bapak/ibu {reviewer} segera menilainya. Terimakasih'
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
        return super(VerifikasiBerkasHakiView, self).form_valid(form)

class PenilaianBerkasHakiView(CreateView):
    model = PenilaianBerkasHaki
    form_class = PenilaianBerkasHakiForm
    template_name = 'penilaian/penilaian_berkas_haki.html'
    success_url = reverse_lazy('home')
    context_object_name = 'penilaian_berkas_haki'

class HasilPenilaianHakiView(DetailView):
    model = PenilaianBerkasHaki
    template_name = 'penilaian/hasil_rekap_haki.html'
    context_object_name = 'rekap_haki'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context
        
    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')
############# End of Haki #############
################################################################################################################
class PenulisLainView(CreateView):
    model = PenulisLain
    form_class = PenulisLainForm
    template_name = 'penilaian/tambah_penulis.html'
    success_url = reverse_lazy('home')

# class AllView(View):
    # def get(self,request):
        # qs_jurnal = UploadBerkasJurnal.objects.all()
        # qs_prosiding = UploadBerkasProsiding.objects.all()
        # qs_buku = UploadBerkasBuku.objects.all()
        # qs_haki = UploadBerkasHaki.objects.all()
        # data_jurnal = serializers.serialize('json', qs_jurnal)
        # data_prosiding = serializers.serialize('json', qs_prosiding)
        # data_buku = serializers.serialize('json', qs_buku)
        # data_haki = serializers.serialize('json', qs_haki)
        # return JsonResponse({'data_jurnal':data_jurnal, 'data_prosiding':data_prosiding, 'data_buku':data_buku, 'data_haki':data_haki}, safe=False)

################################################################################################################