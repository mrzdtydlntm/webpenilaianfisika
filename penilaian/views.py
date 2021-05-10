from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import *
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .utils import render_to_pdf
from webfisika.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

class ReviewerAccess(UserPassesTestMixin, LoginRequiredMixin):
    def test_func(self):
        for reviewer in Reviewer.objects.all():
            if reviewer.reviewer.id == self.request.user.id or self.request.user.is_superuser:
                return True

class SuperAdminAccess(UserPassesTestMixin, LoginRequiredMixin):
    def test_func(self):
        if self.request.user.is_superuser:
            return True

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
        usr = self.request.user
        message = f'Terdapat jurnal berjudul {nama_jurnal} telah diupload oleh {usr}. Mohon untuk diperiksa. Terimakasih'
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return super(UploadBerkasJurnalView, self).form_valid(form)

    def form_invalid(self, form):
        'form is invalid'
        messages.add_message(self.request,messages.WARNING, f'{form.errors}')
        return redirect('penilaian:upload_berkas_jurnal')

class ListBerkasJurnalView(LoginRequiredMixin,ListView):
    model = UploadBerkasJurnal
    template_name = 'penilaian/list_berkas_jurnal.html'
    context_object_name = 'list_berkas_jurnal'
    list_berkas = PenilaianBerkasJurnal.objects.all()
    extra_context = {
        'list_berkas':list_berkas,
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(ListBerkasJurnalView, self).get_context_data(*args, **kwargs)

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

class VerifikasiBerkasJurnalView(SuperAdminAccess, UpdateView):
    model = UploadBerkasJurnal
    form_class = VerifikasiBerkasJurnalForm
    template_name = 'penilaian/verifikasi_berkas_jurnal.html'
    success_url = reverse_lazy('penilaian:list_berkas_jurnal')
    context_object_name = 'verifikasi_jurnal'

    def form_valid(self, form):
        if form.cleaned_data.get('is_verificated') == True:
            if form.cleaned_data.get('reviewer') != None:
                nama_jurnal = form.cleaned_data.get('judul_artikel')
                reviewer = form.cleaned_data.get('reviewer')
                review = User.objects.get(first_name=reviewer.reviewer)
                # print(review)
                subject = 'Konfirmasi Review Jurnal'
                message = f'Terdapat jurnal dengan judul {nama_jurnal} telah diverifikasi. Diharapkan bapak/ibu {reviewer} segera menilainya. Terimakasih'
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
        elif form.cleaned_data.get('is_verificated') == False:
            nama_jurnal = form.cleaned_data.get('judul_artikel')
            pengusul = form.cleaned_data.get('pengusul')
            pengusuls = User.objects.get(first_name=pengusul)
            # print(pengusuls.email)
            subject = 'Konfirmasi Revisi Upload Jurnal'
            message = f'Jurnal dengan judul {nama_jurnal} perlu revisi dikarenakan masih terdapat informasi ataupun berkas yang kurang. Mohon secepatnya ditanggapi. Terimakasih'
            # print(message)
            send_mail(subject, message, EMAIL_HOST_USER, [pengusuls.email, 'difa_only@yahoo.com', 'yoni.kuwantoro@unpad.ac.id'], fail_silently = False)
        return super(VerifikasiBerkasJurnalView, self).form_valid(form)

class PenilaianBerkasJurnalView(ReviewerAccess, CreateView):
    model = PenilaianBerkasJurnal
    form_class = PenilaianBerkasJurnalForm
    template_name = 'penilaian/penilaian_berkas_jurnal.html'
    success_url = reverse_lazy('penilaian:list_penilaian_jurnal')
    context_object_name = 'penilaian_berkas_jurnal'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasJurnal.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

    def form_valid(self, form):
        jurnal = form.cleaned_data.get('jurnal')
        pengusul = User.objects.get(first_name=jurnal.pengusul)
        subject = 'Konfirmasi Penilaian Jurnal'
        message = f'Jurnal dengan judul {jurnal} telah selesai dinilai oleh Reviewer ke 1. Bapak/Ibu {pengusul} dipersilakan untuk mendownload berkas penilaian. Jika terdapat kesalahan, dapat menghubungi Kepala Departemen Fisika. Terimakasih'
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasJurnalView, self).form_valid(form)

class PenilaianBerkasJurnal2View(ReviewerAccess, CreateView):
    model = PenilaianBerkasJurnal2
    form_class = PenilaianBerkasJurnal2Form
    template_name = 'penilaian/penilaian_berkas_jurnal2.html'
    success_url = reverse_lazy('penilaian:list_penilaian_jurnal')
    context_object_name = 'penilaian_berkas_jurnal2'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasJurnal.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

    def form_valid(self, form):
        jurnal = form.cleaned_data.get('jurnal')
        pengusul = User.objects.get(first_name=jurnal.pengusul)
        subject = 'Konfirmasi Penilaian Jurnal'
        message = f'Jurnal dengan judul {jurnal} telah selesai dinilai oleh Reviewer ke 2. Bapak/Ibu {pengusul} dipersilakan untuk mendownload berkas penilaian. Jika terdapat kesalahan, dapat menghubungi Kepala Departemen Fisika. Terimakasih'
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasJurnal2View, self).form_valid(form)

class PenilaianBerkasJurnalEditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasJurnal
    form_class = PenilaianBerkasJurnalEditForm
    template_name = 'penilaian/edit_penilaian_jurnal.html'
    success_url = reverse_lazy('penilaian:list_penilaian_jurnal')
    penilaian = PenilaianBerkasJurnal.objects.all()
    extra_context = {
        'penilaian':penilaian
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class PenilaianBerkasJurnal2EditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasJurnal2
    form_class = PenilaianBerkasJurnal2EditForm
    template_name = 'penilaian/edit_penilaian_jurnal2.html'
    success_url = reverse_lazy('penilaian:list_penilaian_jurnal')
    penilaian = PenilaianBerkasJurnal2.objects.all()
    extra_context = {
        'penilaian':penilaian
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

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

class HasilPenilaianJurnal2View(DetailView):
    model = PenilaianBerkasJurnal2
    template_name = 'penilaian/hasil_rekap_jurnal2.html'
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
        usr = self.request.user
        message = f'Terdapat prosiding berjudul {nama_prosiding} telah diupload oleh {usr}. Mohon untuk diperiksa. Terimakasih'
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return super(UploadBerkasProsidingView, self).form_valid(form)

    def form_invalid(self, form):
        'form is invalid'
        messages.add_message(self.request,messages.WARNING, f'{form.errors}')
        return redirect('penilaian:upload_berkas_prosiding')

class ListBerkasProsidingView(LoginRequiredMixin,ListView):
    model = UploadBerkasProsiding
    template_name = 'penilaian/list_berkas_prosiding.html'
    context_object_name = 'list_berkas_prosiding'
    list_berkas = PenilaianBerkasProsiding.objects.all()
    extra_context = {
        'list_berkas':list_berkas,
    }
    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(ListBerkasProsidingView,self).get_context_data(*args, **kwargs)

class DetailBerkasProsidingView(LoginRequiredMixin,DetailView):
    model = UploadBerkasProsiding
    template_name = 'penilaian/detail_berkas_prosiding.html'
    context_object_name = 'detail_berkas_prosiding'

class EditBerkasProsidingView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasProsiding
    form_class = EditBerkasProsidingForm
    template_name = 'penilaian/edit_berkas_prosiding.html'
    success_url = reverse_lazy('penilaian:list_berkas_prosiding')

class VerifikasiBerkasProsidingView(SuperAdminAccess, UpdateView):
    model = UploadBerkasProsiding
    form_class = VerifikasiBerkasProsidingForm
    template_name = 'penilaian/verifikasi_berkas_prosiding.html'
    success_url = reverse_lazy('penilaian:list_berkas_prosiding')
    context_object_name = 'verifikasi_prosiding'
    
    def form_valid(self, form):
        if form.cleaned_data.get('is_verificated') == True:
            if form.cleaned_data.get('reviewer') != None:
                nama_prosiding = form.cleaned_data.get('judul_artikel')
                reviewer = form.cleaned_data.get('reviewer')
                review = User.objects.get(first_name=reviewer.reviewer)
                subject = 'Konfirmasi Review Prosiding'
                message = f'Terdapat prosiding dengan judul {nama_prosiding} telah diverifikasi. Diharapkan bapak/ibu {reviewer} segera menilainya. Terimakasih'
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
        elif form.cleaned_data.get('is_verificated') == False:
            nama_prosiding = form.cleaned_data.get('judul_artikel')
            pengusul = form.cleaned_data.get('pengusul')
            pengusuls = User.objects.get(first_name=pengusul)
            # print(pengusuls.email)
            subject = 'Konfirmasi Revisi Upload Prosiding'
            message = f'Prosiding dengan judul {nama_prosiding} perlu revisi dikarenakan masih terdapat informasi ataupun berkas yang kurang. Mohon secepatnya ditanggapi. Terimakasih'
            # print(message)
            send_mail(subject, message, EMAIL_HOST_USER, [pengusuls.email, 'difa_only@yahoo.com', 'yoni.kuwantoro@unpad.ac.id'], fail_silently = False)
        return super(VerifikasiBerkasProsidingView, self).form_valid(form)

class PenilaianBerkasProsidingView(ReviewerAccess, CreateView):
    model = PenilaianBerkasProsiding
    form_class = PenilaianBerkasProsidingForm
    template_name = 'penilaian/penilaian_berkas_prosiding.html'
    success_url = reverse_lazy('penilaian:list_penilaian_prosiding')
    context_object_name = 'penilaian_berkas_prosiding'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasProsiding.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

    def form_valid(self, form):
        prosiding = form.cleaned_data.get('prosiding')
        # print(prosiding)
        pengusul = User.objects.get(first_name=prosiding.pengusul)
        # print(pengusul.email)
        subject = 'Konfirmasi Penilaian Prosiding'
        message = f'Prosiding dengan judul {prosiding} telah selesai dinilai oleh Reviewer 1. Bapak/Ibu {pengusul} dipersilakan untuk mendownload berkas penilaian. Jika terdapat kesalahan, dapat menghubungi Kepala Departemen Fisika. Terimakasih'
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasProsidingView, self).form_valid(form)

class PenilaianBerkasProsiding2View(ReviewerAccess, CreateView):
    model = PenilaianBerkasProsiding2
    form_class = PenilaianBerkasProsiding2Form
    template_name = 'penilaian/penilaian_berkas_prosiding2.html'
    success_url = reverse_lazy('penilaian:list_penilaian_prosiding')
    context_object_name = 'penilaian_berkas_prosiding'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasProsiding.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

    def form_valid(self, form):
        prosiding = form.cleaned_data.get('prosiding')
        # print(prosiding)
        pengusul = User.objects.get(first_name=prosiding.pengusul)
        # print(pengusul.email)
        subject = 'Konfirmasi Penilaian Prosiding'
        message = f'Prosiding dengan judul {prosiding} telah selesai dinilai oleh Reviewer 2. Bapak/Ibu {pengusul} dipersilakan untuk mendownload berkas penilaian. Jika terdapat kesalahan, dapat menghubungi Kepala Departemen Fisika. Terimakasih'
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasProsiding2View, self).form_valid(form)

class PenilaianBerkasProsidingEditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasProsiding
    form_class = PenilaianBerkasProsidingEditForm
    template_name = 'penilaian/edit_penilaian_prosiding.html'
    success_url = reverse_lazy('penilaian:list_penilaian_prosiding')
    penilaian = PenilaianBerkasProsiding.objects.all()
    extra_context = {
        'penilaian':penilaian
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class PenilaianBerkasProsiding2EditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasProsiding2
    form_class = PenilaianBerkasProsiding2EditForm
    template_name = 'penilaian/edit_penilaian_prosiding2.html'
    success_url = reverse_lazy('penilaian:list_penilaian_prosiding')
    penilaian = PenilaianBerkasProsiding2.objects.all()
    extra_context = {
        'penilaian':penilaian
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

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

class HasilPenilaianProsiding2View(LoginRequiredMixin,DetailView):
    model = PenilaianBerkasProsiding2
    template_name = 'penilaian/hasil_rekap_prosiding2.html'
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
        nama_buku = form.cleaned_data.get('judul')
        penerima = User.objects.get(pk=1)
        subject = 'Konfirmasi Upload Berkas Buku'
        usr = self.request.user
        message = f'Terdapat buku berjudul {nama_buku} telah diupload oleh {usr}. Mohon untuk diperiksa. Terimakasih'
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return super(UploadBerkasBukuView, self).form_valid(form)
    
    def form_invalid(self, form):
        'form is invalid'
        messages.add_message(self.request,messages.WARNING, f'{form.errors}')
        return redirect('penilaian:upload_berkas_buku')

class ListBerkasBukuView(LoginRequiredMixin,ListView):
    model = UploadBerkasBuku
    template_name = 'penilaian/list_berkas_buku.html'
    context_object_name = 'list_berkas_buku'
    list_berkas = PenilaianBerkasBuku.objects.all()
    extra_context = {
        'list_berkas':list_berkas,
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(ListBerkasBukuView, self).get_context_data(*args, **kwargs)

class DetailBerkasBukuView(LoginRequiredMixin,DetailView):
    model = UploadBerkasBuku
    template_name = 'penilaian/detail_berkas_buku.html'
    context_object_name = 'detail_berkas_buku'

class EditBerkasBukuView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasBuku
    form_class = EditBerkasBukuForm
    template_name = 'penilaian/edit_berkas_buku.html'
    success_url = reverse_lazy('penilaian:list_berkas_buku')

class VerifikasiBerkasBukuView(SuperAdminAccess, UpdateView):
    model = UploadBerkasBuku
    form_class = VerifikasiBerkasBukuForm
    template_name = 'penilaian/verifikasi_berkas_buku.html'
    success_url = reverse_lazy('penilaian:list_berkas_buku')
    context_object_name = 'verifikasi_buku'

    def form_valid(self, form):
        if form.cleaned_data.get('is_verificated') == True:
            if form.cleaned_data.get('reviewer') != None:
                nama_buku = form.cleaned_data.get('judul')
                reviewer = form.cleaned_data.get('reviewer')
                review = User.objects.get(first_name=reviewer.reviewer)
                subject = 'Konfirmasi Review Buku'
                message = f'Terdapat buku dengan judul {nama_buku} telah diverifikasi. Diharapkan bapak/ibu {reviewer} segera menilainya. Terimakasih'
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
        elif form.cleaned_data.get('is_verificated') == False:
            nama_buku = form.cleaned_data.get('judul')
            pengusul = form.cleaned_data.get('pengusul')
            pengusuls = User.objects.get(first_name=pengusul)
            # print(pengusuls.email)
            subject = 'Konfirmasi Revisi Upload Buku'
            message = f'Buku dengan judul {nama_buku} perlu revisi dikarenakan masih terdapat informasi ataupun berkas yang kurang. Mohon secepatnya ditanggapi. Terimakasih'
            # print(message)
            send_mail(subject, message, EMAIL_HOST_USER, [pengusuls.email, 'difa_only@yahoo.com', 'yoni.kuwantoro@unpad.ac.id'], fail_silently = False)
        return super(VerifikasiBerkasBukuView, self).form_valid(form)

class PenilaianBerkasBukuView(ReviewerAccess, CreateView):
    model = PenilaianBerkasBuku
    form_class = PenilaianBerkasBukuForm
    template_name = 'penilaian/penilaian_berkas_buku.html'
    success_url = reverse_lazy('penilaian:list_penilaian_buku')
    context_object_name = 'penilaian_berkas_buku'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasBuku.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context
    
    def form_valid(self, form):
        buku = form.cleaned_data.get('buku')
        # print(buku)
        pengusul = User.objects.get(first_name=buku.pengusul)
        # print(pengusul.email)
        subject = 'Konfirmasi Penilaian Buku'
        message = f'Buku dengan judul {buku} telah selesai dinilai oleh Reviewer 1. Bapak/Ibu {pengusul} dipersilakan untuk mendownload berkas penilaian. Jika terdapat kesalahan, dapat menghubungi Kepala Departemen Fisika. Terimakasih'
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasBukuView, self).form_valid(form)

class PenilaianBerkasBuku2View(ReviewerAccess, CreateView):
    model = PenilaianBerkasBuku2
    form_class = PenilaianBerkasBuku2Form
    template_name = 'penilaian/penilaian_berkas_buku2.html'
    success_url = reverse_lazy('penilaian:list_penilaian_buku')
    context_object_name = 'penilaian_berkas_buku'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasBuku.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context
    
    def form_valid(self, form):
        buku = form.cleaned_data.get('buku')
        # print(buku)
        pengusul = User.objects.get(first_name=buku.pengusul)
        # print(pengusul.email)
        subject = 'Konfirmasi Penilaian Buku'
        message = f'Buku dengan judul {buku} telah selesai dinilai Reviewer 2. Bapak/Ibu {pengusul} dipersilakan untuk mendownload berkas penilaian. Jika terdapat kesalahan, dapat menghubungi Kepala Departemen Fisika. Terimakasih'
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasBuku2View, self).form_valid(form)

class PenilaianBerkasBukuEditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasBuku
    form_class = PenilaianBerkasBukuEditForm
    template_name = 'penilaian/edit_penilaian_buku.html'
    success_url = reverse_lazy('penilaian:list_penilaian_buku')
    penilaian = PenilaianBerkasBuku.objects.all()
    extra_context = {
        'penilaian':penilaian
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class PenilaianBerkasBuku2EditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasBuku2
    form_class = PenilaianBerkasBuku2EditForm
    template_name = 'penilaian/edit_penilaian_buku2.html'
    success_url = reverse_lazy('penilaian:list_penilaian_buku')
    penilaian = PenilaianBerkasBuku2.objects.all()
    extra_context = {
        'penilaian':penilaian
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

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

class HasilPenilaianBuku2View(LoginRequiredMixin,DetailView):
    model = PenilaianBerkasBuku2
    template_name = 'penilaian/hasil_rekap_buku2.html'
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
        nama_haki = form.cleaned_data.get('judul')
        penerima = User.objects.get(pk=1)
        subject = 'Konfirmasi Upload Berkas Haki'
        usr = self.request.user
        message = f'Terdapat berkas haki berjudul {nama_haki} telah diupload oleh {usr}. Mohon untuk diperiksa. Terimakasih'
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return super(UploadBerkasHakiView, self).form_valid(form)
    
    def form_invalid(self, form):
        'form is invalid'
        messages.add_message(self.request,messages.WARNING, f'{form.errors}')
        return redirect('penilaian:upload_berkas_haki')

class ListBerkasHakiView(LoginRequiredMixin,ListView):
    model = UploadBerkasHaki
    template_name = 'penilaian/list_berkas_haki.html'
    context_object_name = 'list_berkas_haki'
    list_berkas = PenilaianBerkasHaki.objects.all()
    extra_context = {
        'list_berkas':list_berkas,
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(ListBerkasHakiView, self).get_context_data(*args, **kwargs)

class DetailBerkasHakiView(LoginRequiredMixin,DetailView):
    model = UploadBerkasHaki
    template_name = 'penilaian/detail_berkas_haki.html'
    context_object_name = 'detail_berkas_haki'
    
class EditBerkasHakiView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasHaki
    form_class = EditBerkasHakiForm
    template_name = 'penilaian/edit_berkas_haki.html'
    success_url = reverse_lazy('penilaian:list_berkas_haki')

class VerifikasiBerkasHakiView(SuperAdminAccess, UpdateView):
    model = UploadBerkasHaki
    form_class = VerifikasiBerkasHakiForm
    template_name = 'penilaian/verifikasi_berkas_haki.html'
    success_url = reverse_lazy('penilaian:list_berkas_haki')
    context_object_name = 'verifikasi_haki'

    def form_valid(self, form):
        if form.cleaned_data.get('is_verificated') == True:
            if form.cleaned_data.get('reviewer') != None:
                nama_haki = form.cleaned_data.get('judul')
                reviewer = form.cleaned_data.get('reviewer')
                review = User.objects.get(first_name=reviewer.reviewer)
                subject = 'Konfirmasi Review Haki'
                message = f'Terdapat haki dengan judul {nama_haki} telah diupload. Diharapkan bapak/ibu {reviewer} segera menilainya. Terimakasih'
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
        elif form.cleaned_data.get('is_verificated') == False:
            nama_haki = form.cleaned_data.get('judul')
            pengusul = form.cleaned_data.get('pengusul')
            pengusuls = User.objects.get(first_name=pengusul)
            # print(pengusuls.email)
            subject = 'Konfirmasi Revisi Upload Haki'
            message = f'Haki dengan judul {nama_haki} perlu revisi dikarenakan masih terdapat informasi ataupun berkas yang kurang. Mohon secepatnya ditanggapi. Terimakasih'
            # print(message)
            send_mail(subject, message, EMAIL_HOST_USER, [pengusuls.email, 'difa_only@yahoo.com', 'yoni.kuwantoro@unpad.ac.id'], fail_silently = False)
        return super(VerifikasiBerkasHakiView, self).form_valid(form)

class PenilaianBerkasHakiView(ReviewerAccess, CreateView):
    model = PenilaianBerkasHaki
    form_class = PenilaianBerkasHakiForm
    template_name = 'penilaian/penilaian_berkas_haki.html'
    success_url = reverse_lazy('penilaian:list_penilaian_haki')
    context_object_name = 'penilaian_berkas_haki'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasHaki.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

    def form_valid(self, form):
        berkas = form.cleaned_data.get('berkas')
        # print(berkas)
        pengusul = User.objects.get(first_name=berkas.pengusul)
        # print(pengusul.email)
        subject = 'Konfirmasi Penilaian Haki'
        message = f'Haki dengan judul {berkas} telah selesai dinilai oleh Reviewer 1. Bapak/Ibu {pengusul} dipersilakan untuk mendownload berkas penilaian. Jika terdapat kesalahan, dapat menghubungi Kepala Departemen Fisika. Terimakasih'
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasHakiView, self).form_valid(form)

class PenilaianBerkasHaki2View(ReviewerAccess, CreateView):
    model = PenilaianBerkasHaki2
    form_class = PenilaianBerkasHaki2Form
    template_name = 'penilaian/penilaian_berkas_haki2.html'
    success_url = reverse_lazy('penilaian:list_penilaian_haki')
    context_object_name = 'penilaian_berkas_haki'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasHaki.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

    def form_valid(self, form):
        berkas = form.cleaned_data.get('berkas')
        # print(berkas)
        pengusul = User.objects.get(first_name=berkas.pengusul)
        # print(pengusul.email)
        subject = 'Konfirmasi Penilaian Haki'
        message = f'Haki dengan judul {berkas} telah selesai dinilai oleh Reviewer 2. Bapak/Ibu {pengusul} dipersilakan untuk mendownload berkas penilaian. Jika terdapat kesalahan, dapat menghubungi Kepala Departemen Fisika. Terimakasih'
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasHaki2View, self).form_valid(form)

class PenilaianBerkasHakiEditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasHaki
    form_class = PenilaianBerkasHakiEditForm
    template_name = 'penilaian/edit_penilaian_haki.html'
    success_url = reverse_lazy('penilaian:list_penilaian_haki')
    penilaian = PenilaianBerkasHaki.objects.all()
    extra_context = {
        'penilaian':penilaian
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class PenilaianBerkasHaki2EditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasHaki2
    form_class = PenilaianBerkasHaki2EditForm
    template_name = 'penilaian/edit_penilaian_haki2.html'
    success_url = reverse_lazy('penilaian:list_penilaian_haki')
    penilaian = PenilaianBerkasHaki2.objects.all()
    extra_context = {
        'penilaian':penilaian
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class HasilPenilaianHakiView(LoginRequiredMixin, DetailView):
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

class HasilPenilaianHaki2View(LoginRequiredMixin, DetailView):
    model = PenilaianBerkasHaki2
    template_name = 'penilaian/hasil_rekap_haki2.html'
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

################################################################################################################
############# List khusus reviewer #############

class ListReviewerJurnalView(ReviewerAccess,ListView):
    model = UploadBerkasJurnal
    template_name = 'penilaian/list_reviewer_jurnal.html'
    context_object_name = 'list_reviewer_jurnal'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ListReviewerJurnalView, self).get_context_data(*args, **kwargs)
        list_berkas = PenilaianBerkasJurnal.objects.all()
        list_berkas_2 = PenilaianBerkasJurnal2.objects.all()
        context['list_berkas'] = list_berkas
        context['list_berkas_2'] = list_berkas_2
        return context

class ListReviewerProsidingView(ReviewerAccess,ListView):
    model = UploadBerkasProsiding
    template_name = 'penilaian/list_reviewer_prosiding.html'
    context_object_name = 'list_reviewer_prosiding'

    def get_context_data(self, *args, **kwargs):
        context = super(ListReviewerProsidingView, self).get_context_data(*args, **kwargs)
        list_berkas = PenilaianBerkasProsiding.objects.all()
        list_berkas_2 = PenilaianBerkasProsiding2.objects.all()
        context['list_berkas'] = list_berkas
        context['list_berkas_2'] = list_berkas_2
        return context

class ListReviewerBukuView(ReviewerAccess,ListView):
    model = UploadBerkasBuku
    template_name = 'penilaian/list_reviewer_buku.html'
    context_object_name = 'list_reviewer_buku'

    def get_context_data(self, *args, **kwargs):
        context = super(ListReviewerBukuView, self).get_context_data(*args, **kwargs)
        list_berkas = PenilaianBerkasBuku.objects.all()
        list_berkas_2 = PenilaianBerkasBuku2.objects.all()
        context['list_berkas'] = list_berkas
        context['list_berkas_2'] = list_berkas_2
        return context

class ListReviewerHakiView(ReviewerAccess,ListView):
    model = UploadBerkasHaki
    template_name = 'penilaian/list_reviewer_haki.html'
    context_object_name = 'list_reviewer_haki'

    def get_context_data(self, *args, **kwargs):
        context = super(ListReviewerHakiView, self).get_context_data(*args, **kwargs)
        list_berkas = PenilaianBerkasHaki.objects.all()
        list_berkas_2 = PenilaianBerkasHaki2.objects.all()
        context['list_berkas'] = list_berkas
        context['list_berkas_2'] = list_berkas_2
        return context

############# END List khusus reviewer #############
################################################################################################################