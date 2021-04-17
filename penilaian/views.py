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
    model = User
    template_name = 'penilaian/user_table.html'
    context_object_name = 'list_user'
################################################################################################################
class UploadBerkasJurnalView(LoginRequiredMixin, CreateView):
    model = UploadBerkasJurnal
    form_class = UploadBerkasJurnalForm
    template_name = 'penilaian/upload_berkas_jurnal.html'
    success_url = reverse_lazy('success')
    nama = User.objects.all()
    extra_context = {
        'form':form_class,
        'list_user':nama
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

    # def post(self,request, *args, **kwargs):
        # subject = 'Konfirmasi Upload Berkas Jurnal'
        # message = 'Terimakasih telah mensubmit berkas jurnal anda. Berkas akan kami proses dan secepatnya akan dinilai.'
        # send_mail(subject, message, EMAIL_HOST_USER, [request.user.email], fail_silently = False)
        # return super().post(request, *args, **kwargs)

class ListBerkasJurnalView(LoginRequiredMixin,ListView):
    model = UploadBerkasJurnal
    template_name = 'penilaian/list_berkas_jurnal.html'
    context_object_name = 'list_berkas_jurnal'
    nama_reviewer = Reviewer.objects.all()
    extra_context = {
        'list_user':nama_reviewer
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class DetailBerkasJurnalView(LoginRequiredMixin,DetailView):
    model = UploadBerkasJurnal
    template_name = 'penilaian/detail_berkas_jurnal.html'
    context_object_name = 'detail_berkas_jurnal'

class VerifikasiBerkasJurnalView(LoginRequiredMixin,UpdateView):
    model = UploadBerkasJurnal
    form_class = VerifikasiBerkasJurnalForm
    template_name = 'penilaian/verifikasi_berkas_jurnal.html'
    success_url = reverse_lazy('penilaian:list_berkas_jurnal')
    context_object_name = 'verifikasi_jurnal'
    nama = User.objects.all()
    extra_context = {
        'list_user':nama
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class PlagiasiLinieritasView(LoginRequiredMixin,CreateView):
    model = PlagiasiLinieritas
    form_class = PlagiasiLinieritasForm
    template_name = 'penilaian/penilaian_plagiasi_linieritas.html'
    success_url = reverse_lazy('home')

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
    rev = User.objects.all()
    plaglin = PlagiasiLinieritas.objects.all()
    extra_context = {
        'list_rev':rev,
        'plaglin':plaglin
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)
    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

############# End of Jurnal #############

class UploadBerkasProsidingView(LoginRequiredMixin, CreateView):
    model = UploadBerkasProsiding
    form_class = UploadBerkasProsidingForm
    template_name = 'penilaian/upload_berkas_prosiding.html'
    success_url = reverse_lazy('success')
    nama = User.objects.all()
    extra_context = {
        'form':form_class,
        'list_user':nama
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs) 
    
    def post(self,request, *args, **kwargs):
        subject = 'Konfirmasi Upload Berkas Prosiding'
        message = 'Terimakasih telah mensubmit berkas prosiding anda. Berkas akan kami proses dan secepatnya akan dinilai.'
        send_mail(subject, message, EMAIL_HOST_USER, [request.user.email], fail_silently = False)
        return super().post(request, *args, **kwargs)

class ListBerkasProsidingView(LoginRequiredMixin,ListView):
    model = UploadBerkasProsiding
    template_name = 'penilaian/list_berkas_prosiding.html'
    context_object_name = 'list_berkas_prosiding'
    nama_reviewer = Reviewer.objects.all()
    extra_context = {
        'list_user':nama_reviewer
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class DetailBerkasProsidingView(LoginRequiredMixin,DetailView):
    model = UploadBerkasProsiding
    template_name = 'penilaian/detail_berkas_prosiding.html'
    context_object_name = 'detail_berkas_prosiding'

class VerifikasiBerkasProsidingView(LoginRequiredMixin,UpdateView):
    model = UploadBerkasProsiding
    form_class = VerifikasiBerkasProsidingForm
    template_name = 'penilaian/verifikasi_berkas_prosiding.html'
    success_url = reverse_lazy('penilaian:list_berkas_prosiding')
    context_object_name = 'verifikasi_prosiding'
    nama = User.objects.all()
    extra_context = {
        'list_user':nama
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

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
    rev = User.objects.all()
    extra_context = {
        'list_rev':rev
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)
    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

############# End of Prosiding #############

class UploadBerkasBukuView(LoginRequiredMixin, CreateView):
    model = UploadBerkasBuku
    form_class = UploadBerkasBukuForm
    template_name = 'penilaian/upload_berkas_buku.html'
    success_url = reverse_lazy('success')
    nama = User.objects.all()
    extra_context = {
        'form':form_class,
        'list_user':nama
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        subject = 'Konfirmasi Upload Berkas Buku'
        message = 'Terimakasih telah mensubmit berkas buku anda. Berkas akan kami proses dan secepatnya akan dinilai.'
        send_mail(subject, message, EMAIL_HOST_USER, [request.user.email], fail_silently = False)
        return super().post(request, *args, **kwargs)

class ListBerkasBukuView(LoginRequiredMixin,ListView):
    model = UploadBerkasBuku
    template_name = 'penilaian/list_berkas_buku.html'
    context_object_name = 'list_berkas_buku'
    nama_reviewer = Reviewer.objects.all()
    extra_context = {
        'list_user':nama_reviewer
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class DetailBerkasBukuView(LoginRequiredMixin,DetailView):
    model = UploadBerkasBuku
    template_name = 'penilaian/detail_berkas_buku.html'
    context_object_name = 'detail_berkas_buku'

class VerifikasiBerkasBukuView(LoginRequiredMixin,UpdateView):
    model = UploadBerkasBuku
    form_class = VerifikasiBerkasBukuForm
    template_name = 'penilaian/verifikasi_berkas_buku.html'
    success_url = reverse_lazy('penilaian:list_berkas_buku')
    context_object_name = 'verifikasi_buku'
    nama = User.objects.all()
    extra_context = {
        'list_user':nama
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

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
    rev = User.objects.all()
    extra_context = {
        'list_rev':rev
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)
    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

############# End of Buku #############

class UploadBerkasHakiView(LoginRequiredMixin, CreateView):
    model = UploadBerkasHaki
    form_class = UploadBerkasHakiForm
    template_name = 'penilaian/upload_berkas_haki.html'
    success_url = reverse_lazy('success')
    nama = User.objects.all()
    extra_context = {
        'form':form_class,
        'list_user':nama
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

    def post(self,request, *args, **kwargs):
        subject = 'Konfirmasi Upload Berkas Haki'
        message = 'Terimakasih telah mensubmit berkas Haki anda. Berkas akan kami proses dan secepatnya akan dinilai.'
        send_mail(subject, message, EMAIL_HOST_USER, [request.user.email], fail_silently = False)
        return super().post(request, *args, **kwargs)

class ListBerkasHakiView(LoginRequiredMixin,ListView):
    model = UploadBerkasHaki
    template_name = 'penilaian/list_berkas_haki.html'
    context_object_name = 'list_berkas_haki'
    nama_reviewer = Reviewer.objects.all()
    extra_context = {
        'list_user':nama_reviewer
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class DetailBerkasHakiView(LoginRequiredMixin,DetailView):
    model = UploadBerkasHaki
    template_name = 'penilaian/detail_berkas_haki.html'
    context_object_name = 'detail_berkas_haki'

class VerifikasiBerkasHakiView(LoginRequiredMixin,UpdateView):
    model = UploadBerkasHaki
    form_class = VerifikasiBerkasHakiForm
    template_name = 'penilaian/verifikasi_berkas_haki.html'
    success_url = reverse_lazy('penilaian:list_berkas_haki')
    context_object_name = 'verifikasi_haki'
    nama = User.objects.all()
    extra_context = {
        'list_user':nama
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

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
    rev = User.objects.all()
    extra_context = {
        'list_rev':rev
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)
    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')
############# End of Haki #############
################################################################################################################
class AllView(View):
    def get(self,request):
        qs_jurnal = UploadBerkasJurnal.objects.all()
        qs_prosiding = UploadBerkasProsiding.objects.all()
        qs_buku = UploadBerkasBuku.objects.all()
        qs_haki = UploadBerkasHaki.objects.all()
        data_jurnal = serializers.serialize('json', qs_jurnal)
        data_prosiding = serializers.serialize('json', qs_prosiding)
        data_buku = serializers.serialize('json', qs_buku)
        data_haki = serializers.serialize('json', qs_haki)
        return JsonResponse({'data_jurnal':data_jurnal, 'data_prosiding':data_prosiding, 'data_buku':data_buku, 'data_haki':data_haki}, safe=False)

################################################################################################################