from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import *
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, Http404, response
from .utils import render_to_pdf
from webfisika.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.text import slugify
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

class ErrorMessage(TemplateView):
    template_name='penilaian/error_message.html'

class EditDataDiriView(UpdateView):
    model = Users
    form_class = EditDataDiriForm
    template_name = 'penilaian/edit_data.html'
    def get_success_url(self):
        return reverse('home')
    
################################################################################################################
class UploadBerkasJurnalView(LoginRequiredMixin, CreateView):
    model = UploadBerkasJurnal
    login_url = '/login/'
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
        pengusul = form.cleaned_data.get('pengusul')
        response = super(UploadBerkasJurnalView, self).form_valid(form)
        pk = form.instance.pk
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/upload_jurnal.txt', 'r')
        message = mes.read().format(nama_jurnal, pengusul, pk)
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return response

    def form_invalid(self, form):
        'form is invalid'
        messages.add_message(self.request,messages.WARNING, f'{form.errors}')
        return redirect('penilaian:upload_berkas_jurnal')

class ListBerkasJurnalView(LoginRequiredMixin,ListView):
    model = UploadBerkasJurnal
    login_url = '/login/'
    paginate_by = 5
    ordering = ['-uploaded']
    template_name = 'penilaian/list_berkas_jurnal.html'
    context_object_name = 'list_berkas_jurnal'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['list_berkas'] = PenilaianBerkasJurnal.objects.all()
        context['list_berkas_2'] = PenilaianBerkasJurnal2.objects.all()
        return context

    def get_queryset(self):
        result = super(ListBerkasJurnalView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = UploadBerkasJurnal.objects.filter(judul_artikel__icontains=query)
            result = postresult
        return result

class DetailBerkasJurnalView(LoginRequiredMixin,DetailView):
    model = UploadBerkasJurnal
    login_url = '/login/'
    template_name = 'penilaian/detail_berkas_jurnal.html'
    context_object_name = 'detail_berkas_jurnal'

class EditBerkasJurnalView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasJurnal
    login_url = '/login/'
    form_class = EditBerkasJurnalForm
    template_name = 'penilaian/edit_berkas_jurnal.html'
    def get_success_url(self):
        return reverse('penilaian:list_berkas_jurnal', kwargs={'page':1})
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasJurnal.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

class PlagiasiLinieritasView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasJurnal
    login_url = '/login/'
    form_class = PlagiasiLinieritasForm
    template_name = 'penilaian/plagiasi_linieritas.html'
    def get_success_url(self):
        return reverse('penilaian:list_berkas_jurnal', kwargs={'page':1})

class EditPlagiasiLinieritasView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasJurnal
    login_url = '/login/'
    form_class = EditPlagiasiLinieritasForm
    template_name = 'penilaian/plagiasi_linieritas.html'
    def get_success_url(self):
        return reverse('penilaian:list_berkas_jurnal', kwargs={'page':1})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasJurnal.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

class VerifikasiBerkasJurnalView(SuperAdminAccess, UpdateView):
    model = UploadBerkasJurnal
    login_url = '/login/'
    form_class = VerifikasiBerkasJurnalForm
    template_name = 'penilaian/verifikasi_berkas_jurnal.html'
    context_object_name = 'verifikasi_jurnal'

    def get_success_url(self):
        return reverse('penilaian:list_berkas_jurnal', kwargs={'page':1})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasJurnal.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

    def form_valid(self, form):
        if form.cleaned_data.get('is_verificated') == True:
            if form.cleaned_data.get('reviewer') != None:
                nama_jurnal = form.cleaned_data.get('judul_artikel')
                reviewer = form.cleaned_data.get('reviewer')
                review = User.objects.get(first_name=reviewer.reviewer)
                # print(review)
                subject = 'Konfirmasi Review Jurnal'
                pengusul = form.cleaned_data.get('pengusul')
                pk = self.kwargs['pk']
                import os
                dir_path = os.path.dirname(os.path.realpath(__file__))
                mes = open(dir_path + '/emailer/reviewer_jurnal.txt', 'r')
                message = mes.read().format(reviewer, nama_jurnal, pengusul, 'R1', pk, reviewer.nip)
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
            if form.cleaned_data.get('reviewer_2') != None:
                nama_jurnal = form.cleaned_data.get('judul_artikel')
                reviewer_2 = form.cleaned_data.get('reviewer_2')
                review_2 = User.objects.get(first_name=reviewer_2.reviewer)
                # print(review)
                subject = 'Konfirmasi Review Jurnal'
                pengusul = form.cleaned_data.get('pengusul')
                pk = self.kwargs['pk']
                import os
                dir_path = os.path.dirname(os.path.realpath(__file__))
                mes = open(dir_path + '/emailer/reviewer_jurnal.txt', 'r')
                message = mes.read().format(reviewer, nama_jurnal, pengusul, 'R2', pk, reviewer.nip)
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review_2.email], fail_silently = False)
        elif form.cleaned_data.get('is_verificated') == False:
            nama_jurnal = form.cleaned_data.get('judul_artikel')
            pengusul = form.cleaned_data.get('pengusul')
            pengusuls = User.objects.get(first_name=pengusul)
            subject = 'Konfirmasi Revisi Upload Jurnal' 
            pk = self.kwargs['pk']
            alasan = self.request.POST['alasan']
            import os
            dir_path = os.path.dirname(os.path.realpath(__file__))
            mes = open(dir_path + '/emailer/revisi_jurnal.txt', 'r')
            message = mes.read().format(pengusul, nama_jurnal, pengusul, alasan, pk)
            # print(message)
            send_mail(subject, message, EMAIL_HOST_USER, [pengusuls.email, 'difa_only@yahoo.com', 'yoni.kuwantoro@unpad.ac.id'], fail_silently = False)
        return super(VerifikasiBerkasJurnalView, self).form_valid(form)

class PenilaianBerkasJurnalView(ReviewerAccess, CreateView):
    model = PenilaianBerkasJurnal
    login_url = '/login/'
    form_class = PenilaianBerkasJurnalForm
    template_name = 'penilaian/penilaian_berkas_jurnal.html'
    context_object_name = 'penilaian_berkas_jurnal'
    def get_success_url(self):
        return reverse('penilaian:list_penilaian_jurnal', kwargs={'page':1})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasJurnal.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

    def form_valid(self, form):
        jurnal = form.cleaned_data.get('jurnal')
        pengusul = User.objects.get(first_name=jurnal.pengusul)
        subject = 'Konfirmasi Penilaian Jurnal'
        slug = slugify(UploadBerkasJurnal.objects.get(slug=jurnal.slug))
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/penilaian_jurnal.txt', 'r')
        message = mes.read().format(pengusul, jurnal, pengusul, '1', 'R1', slug)
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasJurnalView, self).form_valid(form)

class PenilaianBerkasJurnal2View(ReviewerAccess, CreateView):
    model = PenilaianBerkasJurnal2
    login_url = '/login/'
    form_class = PenilaianBerkasJurnal2Form
    template_name = 'penilaian/penilaian_berkas_jurnal2.html'
    context_object_name = 'penilaian_berkas_jurnal2'
    def get_success_url(self):
        return reverse('penilaian:list_penilaian_jurnal', kwargs={'page':1})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasJurnal.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

    def form_valid(self, form):
        jurnal = form.cleaned_data.get('jurnal')
        pengusul = User.objects.get(first_name=jurnal.pengusul)
        subject = 'Konfirmasi Penilaian Jurnal'
        slug = slugify(UploadBerkasJurnal.objects.get(slug=jurnal.slug))
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/penilaian_jurnal.txt', 'r')
        message = mes.read().format(pengusul, jurnal, pengusul, '2', 'R2', slug)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasJurnal2View, self).form_valid(form)

class PenilaianBerkasJurnalEditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasJurnal
    login_url = '/login/'
    form_class = PenilaianBerkasJurnalEditForm
    template_name = 'penilaian/edit_penilaian_jurnal.html'

    def get_success_url(self):
        return reverse('penilaian:list_penilaian_jurnal', kwargs={'page':1})

class PenilaianBerkasJurnal2EditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasJurnal2
    login_url = '/login/'
    form_class = PenilaianBerkasJurnal2EditForm
    template_name = 'penilaian/edit_penilaian_jurnal2.html'

    def get_success_url(self):
        return reverse('penilaian:list_penilaian_jurnal', kwargs={'page':1})

class HasilPenilaianJurnalView(LoginRequiredMixin, DetailView):
    model = PenilaianBerkasJurnal
    login_url = '/login/'
    template_name = 'penilaian/hasil_rekap_jurnal.html'
    context_object_name = 'rekap_jurnal'
    
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return redirect('penilaian:error_message')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

class HasilPenilaianJurnal2View(LoginRequiredMixin, DetailView):
    model = PenilaianBerkasJurnal2
    login_url = '/login/'
    template_name = 'penilaian/hasil_rekap_jurnal2.html'
    context_object_name = 'rekap_jurnal'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return redirect('penilaian:error_message')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

class HasilPenilaianBerkasJurnalGabunganView(LoginRequiredMixin, TemplateView):
    template_name = 'penilaian/hasil_rekap_gabungan_jurnal.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HasilPenilaianBerkasJurnalGabunganView, self).get_context_data(*args, **kwargs)
        berkas = PenilaianBerkasJurnal.objects.get(slug = self.kwargs['slug'])
        berkas_2 = PenilaianBerkasJurnal2.objects.get(slug = self.kwargs['slug'])
        context['berkas'] = berkas
        context['berkas_2'] = berkas_2
        context['usrlogin'] = self.request.user
        if berkas.nilai_pu != 0:
            context['nilaitotal_pu'] = ((berkas.nilai_pu + berkas_2.nilai_pu)/2)
        if berkas.nilai_ca != None:
            context['nilaitotal_ca'] = ((berkas.nilai_ca + berkas_2.nilai_ca)/2)
        if berkas.nilai_pl != None:
            context['nilaitotal_pl'] = ((berkas.nilai_pl + berkas_2.nilai_pl)/2)
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

############# End of Jurnal #############

class UploadBerkasProsidingView(LoginRequiredMixin, CreateView):
    model = UploadBerkasProsiding
    login_url = '/login/'
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
        pengusul = form.cleaned_data.get('pengusul')
        response = super(UploadBerkasProsidingView, self).form_valid(form)
        pk = form.instance.pk
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/upload_prosiding.txt', 'r')
        message = mes.read().format(nama_prosiding, pengusul, pk)
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return response

    def form_invalid(self, form):
        'form is invalid'
        messages.add_message(self.request,messages.WARNING, f'{form.errors}')
        return redirect('penilaian:upload_berkas_prosiding')

class ListBerkasProsidingView(LoginRequiredMixin,ListView):
    model = UploadBerkasProsiding
    login_url = '/login/'
    paginate_by = 5
    ordering = ['-uploaded']
    template_name = 'penilaian/list_berkas_prosiding.html'
    context_object_name = 'list_berkas_prosiding'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['list_berkas'] = PenilaianBerkasProsiding.objects.all()
        context['list_berkas_2'] = PenilaianBerkasProsiding2.objects.all()
        return context
    
    def get_queryset(self):
        result = super(ListBerkasProsidingView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = UploadBerkasProsiding.objects.filter(judul_artikel__icontains=query)
            result = postresult
        return result

class PlagiasiLinieritasProsidingView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasProsiding
    login_url = '/login/'
    form_class = PlagiasiLinieritasProsidingForm
    template_name = 'penilaian/plagiasi_linieritas_prosiding.html'
    def get_success_url(self):
        return reverse('penilaian:list_berkas_prosiding', kwargs={'page':1})

class EditPlagiasiLinieritasProsidingView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasProsiding
    login_url = '/login/'
    form_class = EditPlagiasiLinieritasForm
    template_name = 'penilaian/plagiasi_linieritas_prosiding.html'
    def get_success_url(self):
        return reverse('penilaian:list_berkas_prosiding', kwargs={'page':1})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasProsiding.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

class DetailBerkasProsidingView(LoginRequiredMixin,DetailView):
    model = UploadBerkasProsiding
    login_url = '/login/'
    template_name = 'penilaian/detail_berkas_prosiding.html'
    context_object_name = 'detail_berkas_prosiding'

class EditBerkasProsidingView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasProsiding
    login_url = '/login/'
    form_class = EditBerkasProsidingForm
    template_name = 'penilaian/edit_berkas_prosiding.html'
    def get_success_url(self):
        return reverse('penilaian:list_berkas_prosiding', kwargs={'page':1})
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasProsiding.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

class VerifikasiBerkasProsidingView(SuperAdminAccess, UpdateView):
    model = UploadBerkasProsiding
    login_url = '/login/'
    form_class = VerifikasiBerkasProsidingForm
    template_name = 'penilaian/verifikasi_berkas_prosiding.html'
    context_object_name = 'verifikasi_prosiding'
    def get_success_url(self):
        return reverse('penilaian:list_berkas_prosiding', kwargs={'page':1})
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasProsiding.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context
    
    def form_valid(self, form):
        if form.cleaned_data.get('is_verificated') == True:
            if form.cleaned_data.get('reviewer') != None:
                nama_prosiding = form.cleaned_data.get('judul_artikel')
                reviewer = form.cleaned_data.get('reviewer')
                review = User.objects.get(first_name=reviewer.reviewer)
                subject = 'Konfirmasi Review Prosiding'
                pengusul = form.cleaned_data.get('pengusul')
                pk = self.kwargs['pk']
                import os
                dir_path = os.path.dirname(os.path.realpath(__file__))
                mes = open(dir_path + '/emailer/reviewer_prosiding.txt', 'r')
                message = mes.read().format(reviewer, nama_prosiding, pengusul, 'R1', pk, reviewer.nip)
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
            if form.cleaned_data.get('reviewer_2') != None:
                nama_prosiding = form.cleaned_data.get('judul_artikel')
                reviewer_2 = form.cleaned_data.get('reviewer_2')
                review_2 = User.objects.get(first_name=reviewer_2.reviewer)
                subject = 'Konfirmasi Review Prosiding'
                pengusul = form.cleaned_data.get('pengusul')
                pk = self.kwargs['pk']
                import os
                dir_path = os.path.dirname(os.path.realpath(__file__))
                mes = open(dir_path + '/emailer/reviewer_prosiding.txt', 'r')
                message = mes.read().format(reviewer, nama_prosiding, pengusul, 'R2', pk, reviewer.nip)
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review_2.email], fail_silently = False)
        elif form.cleaned_data.get('is_verificated') == False:
            nama_prosiding = form.cleaned_data.get('judul_artikel')
            pengusul = form.cleaned_data.get('pengusul')
            pengusuls = User.objects.get(first_name=pengusul)
            subject = 'Konfirmasi Revisi Upload Prosiding'
            pk = self.kwargs['pk']
            alasan = self.request.POST['alasan']
            import os 
            dir_path = os.path.dirname(os.path.realpath(__file__))
            mes = open(dir_path + '/emailer/revisi_prosiding.txt', 'r')
            message = mes.read().format(pengusul, nama_prosiding, pengusul, alasan, pk)
            # print(message)
            send_mail(subject, message, EMAIL_HOST_USER, [pengusuls.email, 'difa_only@yahoo.com', 'yoni.kuwantoro@unpad.ac.id'], fail_silently = False)
        return super(VerifikasiBerkasProsidingView, self).form_valid(form)

class PenilaianBerkasProsidingView(ReviewerAccess, CreateView):
    model = PenilaianBerkasProsiding
    login_url = '/login/'
    form_class = PenilaianBerkasProsidingForm
    template_name = 'penilaian/penilaian_berkas_prosiding.html'
    context_object_name = 'penilaian_berkas_prosiding'
    def get_success_url(self):
        return reverse('penilaian:list_penilaian_prosiding', kwargs={'page':1})

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
        slug = slugify(UploadBerkasProsiding.objects.get(slug=prosiding.slug))
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/penilaian_prosiding.txt', 'r')
        message = mes.read().format(pengusul, prosiding, pengusul, '1', 'R1', slug)
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasProsidingView, self).form_valid(form)

class PenilaianBerkasProsiding2View(ReviewerAccess, CreateView):
    model = PenilaianBerkasProsiding2
    login_url = '/login/'
    form_class = PenilaianBerkasProsiding2Form
    template_name = 'penilaian/penilaian_berkas_prosiding2.html'
    context_object_name = 'penilaian_berkas_prosiding'
    def get_success_url(self):
        return reverse('penilaian:list_penilaian_prosiding', kwargs={'page':1})

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
        slug = slugify(UploadBerkasProsiding.objects.get(slug=prosiding.slug))
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/penilaian_prosiding.txt', 'r')
        message = mes.read().format(pengusul, prosiding, pengusul, '2', 'R2', slug)
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasProsiding2View, self).form_valid(form)

class PenilaianBerkasProsidingEditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasProsiding
    login_url = '/login/'
    form_class = PenilaianBerkasProsidingEditForm
    template_name = 'penilaian/edit_penilaian_prosiding.html'
    def get_success_url(self):
        return reverse('penilaian:list_penilaian_prosiding', kwargs={'page':1})

class PenilaianBerkasProsiding2EditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasProsiding2
    login_url = '/login/'
    form_class = PenilaianBerkasProsiding2EditForm
    template_name = 'penilaian/edit_penilaian_prosiding2.html'
    def get_success_url(self):
        return reverse('penilaian:list_penilaian_prosiding', kwargs={'page':1})

class HasilPenilaianProsidingView(LoginRequiredMixin,DetailView):
    model = PenilaianBerkasProsiding
    login_url = '/login/'
    template_name = 'penilaian/hasil_rekap_prosiding.html'
    context_object_name = 'rekap_prosiding'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return redirect('penilaian:error_message')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

class HasilPenilaianProsiding2View(LoginRequiredMixin,DetailView):
    model = PenilaianBerkasProsiding2
    login_url = '/login/'
    template_name = 'penilaian/hasil_rekap_prosiding2.html'
    context_object_name = 'rekap_prosiding'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return redirect('penilaian:error_message')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

class HasilPenilaianBerkasProsidingGabunganView(LoginRequiredMixin, TemplateView):
    template_name = 'penilaian/hasil_rekap_gabungan_prosiding.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HasilPenilaianBerkasProsidingGabunganView, self).get_context_data(*args, **kwargs)
        berkas = PenilaianBerkasProsiding.objects.get(slug = self.kwargs['slug'])
        berkas_2 = PenilaianBerkasProsiding2.objects.get(slug = self.kwargs['slug'])
        context['berkas'] = berkas
        context['berkas_2'] = berkas_2
        context['usrlogin'] = self.request.user
        if berkas.nilai_pu != 0:
            context['nilaitotal_pu'] = ((berkas.nilai_pu + berkas_2.nilai_pu)/2)
        if berkas.nilai_ca != None:
            context['nilaitotal_ca'] = ((berkas.nilai_ca + berkas_2.nilai_ca)/2)
        if berkas.nilai_pl != None:
            context['nilaitotal_pl'] = ((berkas.nilai_pl + berkas_2.nilai_pl)/2)
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

############# End of Prosiding #############

class UploadBerkasBukuView(LoginRequiredMixin, CreateView):
    model = UploadBerkasBuku
    login_url = '/login/'
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
        pengusul = form.cleaned_data.get('pengusul')
        response = super(UploadBerkasBukuView, self).form_valid(form)
        pk = form.instance.pk
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/upload_buku.txt', 'r')
        message = mes.read().format(nama_buku, pengusul, pk)
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return response
    
    def form_invalid(self, form):
        'form is invalid'
        messages.add_message(self.request,messages.WARNING, f'{form.errors}')
        return redirect('penilaian:upload_berkas_buku')

class ListBerkasBukuView(LoginRequiredMixin,ListView):
    model = UploadBerkasBuku
    login_url = '/login/'
    paginate_by = 5
    ordering = ['-uploaded']
    template_name = 'penilaian/list_berkas_buku.html'
    context_object_name = 'list_berkas_buku'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['list_berkas'] = PenilaianBerkasBuku.objects.all()
        context['list_berkas_2'] = PenilaianBerkasBuku2.objects.all()
        return context

    def get_queryset(self):
        result = super(ListBerkasBukuView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = UploadBerkasBuku.objects.filter(judul__icontains=query)
            result = postresult
        return result

class DetailBerkasBukuView(LoginRequiredMixin,DetailView):
    model = UploadBerkasBuku
    login_url = '/login/'
    template_name = 'penilaian/detail_berkas_buku.html'
    context_object_name = 'detail_berkas_buku'

class EditBerkasBukuView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasBuku
    login_url = '/login/'
    form_class = EditBerkasBukuForm
    template_name = 'penilaian/edit_berkas_buku.html'
    def get_success_url(self):
        return reverse('penilaian:list_berkas_buku', kwargs={'page':1})
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasBuku.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

class VerifikasiBerkasBukuView(SuperAdminAccess, UpdateView):
    model = UploadBerkasBuku
    login_url = '/login/'
    form_class = VerifikasiBerkasBukuForm
    template_name = 'penilaian/verifikasi_berkas_buku.html'
    context_object_name = 'verifikasi_buku'
    def get_success_url(self):
        return reverse('penilaian:list_berkas_buku', kwargs={'page':1})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasBuku.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

    def form_valid(self, form):
        if form.cleaned_data.get('is_verificated') == True:
            if form.cleaned_data.get('reviewer') != None:
                nama_buku = form.cleaned_data.get('judul')
                reviewer = form.cleaned_data.get('reviewer')
                review = User.objects.get(first_name=reviewer.reviewer)
                subject = 'Konfirmasi Review Buku'
                pengusul = form.cleaned_data.get('pengusul')
                pk = self.kwargs['pk']
                import os
                dir_path = os.path.dirname(os.path.realpath(__file__))
                mes = open(dir_path + '/emailer/reviewer_buku.txt', 'r')
                message = mes.read().format(reviewer, nama_buku, pengusul, 'R1', pk, reviewer.nip)
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
            if form.cleaned_data.get('reviewer_2') != None:
                nama_buku = form.cleaned_data.get('judul')
                reviewer_2 = form.cleaned_data.get('reviewer_2')
                review_2 = User.objects.get(first_name=reviewer_2.reviewer)
                subject = 'Konfirmasi Review Buku'
                pengusul = form.cleaned_data.get('pengusul')
                pk = self.kwargs['pk']
                import os
                dir_path = os.path.dirname(os.path.realpath(__file__))
                mes = open(dir_path + '/emailer/reviewer_buku.txt', 'r')
                message = mes.read().format(reviewer, nama_buku, pengusul, 'R2', pk, reviewer.nip)
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review_2.email], fail_silently = False)
        elif form.cleaned_data.get('is_verificated') == False:
            nama_buku = form.cleaned_data.get('judul')
            pengusul = form.cleaned_data.get('pengusul')
            pengusuls = User.objects.get(first_name=pengusul)
            # print(pengusuls.email)
            subject = 'Konfirmasi Revisi Upload Buku'
            pk = self.kwargs['pk']
            alasan = self.request.POST['alasan']
            import os
            dir_path = os.path.dirname(os.path.realpath(__file__))
            mes = open(dir_path + '/emailer/revisi_buku.txt', 'r')
            message = mes.read().format(pengusul, nama_buku, pengusul, alasan, pk)
            # print(message)
            send_mail(subject, message, EMAIL_HOST_USER, [pengusuls.email, 'difa_only@yahoo.com', 'yoni.kuwantoro@unpad.ac.id'], fail_silently = False)
        return super(VerifikasiBerkasBukuView, self).form_valid(form)

class PenilaianBerkasBukuView(ReviewerAccess, CreateView):
    model = PenilaianBerkasBuku
    login_url = '/login/'
    form_class = PenilaianBerkasBukuForm
    template_name = 'penilaian/penilaian_berkas_buku.html'
    context_object_name = 'penilaian_berkas_buku'
    def get_success_url(self):
        return reverse('penilaian:list_penilaian_buku', kwargs={'page':1})

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
        slug = slugify(UploadBerkasBuku.objects.get(slug=buku.slug))
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/penilaian_buku.txt', 'r')
        message = mes.read().format(pengusul, buku, pengusul, '1', 'R1', slug)
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasBukuView, self).form_valid(form)

class PenilaianBerkasBuku2View(ReviewerAccess, CreateView):
    model = PenilaianBerkasBuku2
    login_url = '/login/'
    form_class = PenilaianBerkasBuku2Form
    template_name = 'penilaian/penilaian_berkas_buku2.html'
    context_object_name = 'penilaian_berkas_buku'
    def get_success_url(self):
        return reverse('penilaian:list_penilaian_buku', kwargs={'page':1})

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
        slug = slugify(UploadBerkasBuku.objects.get(slug=buku.slug))
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/penilaian_buku.txt', 'r')
        message = mes.read().format(pengusul, buku, pengusul, '2', 'R2', slug)
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasBuku2View, self).form_valid(form)

class PenilaianBerkasBukuEditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasBuku
    login_url = '/login/'
    form_class = PenilaianBerkasBukuEditForm
    template_name = 'penilaian/edit_penilaian_buku.html'
    
    def get_success_url(self):
        return reverse('penilaian:list_penilaian_buku', kwargs={'page':1})

class PenilaianBerkasBuku2EditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasBuku2
    login_url = '/login/'
    form_class = PenilaianBerkasBuku2EditForm
    template_name = 'penilaian/edit_penilaian_buku2.html'

    def get_success_url(self):
        return reverse('penilaian:list_penilaian_buku', kwargs={'page':1})

class HasilPenilaianBukuView(LoginRequiredMixin,DetailView):
    model = PenilaianBerkasBuku
    login_url = '/login/'
    template_name = 'penilaian/hasil_rekap_buku.html'
    context_object_name = 'rekap_buku'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return redirect('penilaian:error_message')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

class HasilPenilaianBuku2View(LoginRequiredMixin,DetailView):
    model = PenilaianBerkasBuku2
    login_url = '/login/'
    template_name = 'penilaian/hasil_rekap_buku2.html'
    context_object_name = 'rekap_buku'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return redirect('penilaian:error_message')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

class HasilPenilaianBerkasBukuGabunganView(LoginRequiredMixin, TemplateView):
    template_name = 'penilaian/hasil_rekap_gabungan_buku.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HasilPenilaianBerkasBukuGabunganView, self).get_context_data(*args, **kwargs)
        berkas = PenilaianBerkasBuku.objects.get(slug = self.kwargs['slug'])
        berkas_2 = PenilaianBerkasBuku2.objects.get(slug = self.kwargs['slug'])
        context['berkas'] = berkas
        context['berkas_2'] = berkas_2
        context['usrlogin'] = self.request.user
        if berkas.nilai_pu != 0:
            context['nilaitotal_pu'] = ((berkas.nilai_pu + berkas_2.nilai_pu)/2)
        if berkas.nilai_pl != 0:
            context['nilaitotal_pl'] = ((berkas.nilai_pl + berkas_2.nilai_pl)/2)
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

############# End of Buku #############

class UploadBerkasHakiView(LoginRequiredMixin, CreateView):
    model = UploadBerkasHaki
    login_url = '/login/'
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
        pengusul = form.cleaned_data.get('pengusul')
        response = super(UploadBerkasHakiView, self).form_valid(form)
        pk = form.instance.pk
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/upload_haki.txt', 'r')
        message = mes.read().format(nama_haki, pengusul, pk)
        send_mail(subject, message, EMAIL_HOST_USER, [penerima.email], fail_silently = False)
        return response
    
    def form_invalid(self, form):
        'form is invalid'
        messages.add_message(self.request,messages.WARNING, f'{form.errors}')
        return redirect('penilaian:upload_berkas_haki')

class ListBerkasHakiView(LoginRequiredMixin,ListView):
    model = UploadBerkasHaki
    login_url = '/login/'
    paginate_by = 5
    ordering = ['-uploaded']
    template_name = 'penilaian/list_berkas_haki.html'
    context_object_name = 'list_berkas_haki'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['list_berkas'] = PenilaianBerkasHaki.objects.all()
        context['list_berkas_2'] = PenilaianBerkasHaki2.objects.all()
        return context

    def get_queryset(self):
        result = super(ListBerkasHakiView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = UploadBerkasHaki.objects.filter(judul__icontains=query)
            result = postresult
        return result

class DetailBerkasHakiView(LoginRequiredMixin,DetailView):
    model = UploadBerkasHaki
    login_url = '/login/'
    template_name = 'penilaian/detail_berkas_haki.html'
    context_object_name = 'detail_berkas_haki'
    
class EditBerkasHakiView(LoginRequiredMixin, UpdateView):
    model = UploadBerkasHaki
    login_url = '/login/'
    form_class = EditBerkasHakiForm
    template_name = 'penilaian/edit_berkas_haki.html'
    def get_success_url(self):
        return reverse('penilaian:list_berkas_haki', kwargs={'page':1})
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasHaki.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

class VerifikasiBerkasHakiView(SuperAdminAccess, UpdateView):
    model = UploadBerkasHaki
    login_url = '/login/'
    form_class = VerifikasiBerkasHakiForm
    template_name = 'penilaian/verifikasi_berkas_haki.html'
    context_object_name = 'verifikasi_haki'
    def get_success_url(self):
        return reverse('penilaian:list_berkas_haki', kwargs={'page':1})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        upload = UploadBerkasHaki.objects.get(pk = self.kwargs['pk'])
        context['upload'] = upload
        return context

    def form_valid(self, form):
        if form.cleaned_data.get('is_verificated') == True:
            if form.cleaned_data.get('reviewer') != None:
                nama_haki = form.cleaned_data.get('judul')
                reviewer = form.cleaned_data.get('reviewer')
                review = User.objects.get(first_name=reviewer.reviewer)
                subject = 'Konfirmasi Review Haki'
                pengusul = form.cleaned_data.get('pengusul')
                pk = self.kwargs['pk']
                import os
                dir_path = os.path.dirname(os.path.realpath(__file__))
                mes = open(dir_path + '/emailer/reviewer_haki.txt', 'r')
                message = mes.read().format(reviewer, nama_haki, pengusul, 'R1', pk, reviewer.nip)
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review.email], fail_silently = False)
            if form.cleaned_data.get('reviewer_2') != None:
                nama_haki = form.cleaned_data.get('judul')
                reviewer_2 = form.cleaned_data.get('reviewer_2')
                review_2 = User.objects.get(first_name=reviewer_2.reviewer)
                subject = 'Konfirmasi Review Haki'
                pengusul = form.cleaned_data.get('pengusul')
                pk = self.kwargs['pk']
                import os
                dir_path = os.path.dirname(os.path.realpath(__file__))
                mes = open(dir_path + '/emailer/reviewer_haki.txt', 'r')
                message = mes.read().format(reviewer, nama_haki, pengusul, 'R2', pk, reviewer.nip)
                # print(message)
                send_mail(subject, message, EMAIL_HOST_USER, [review_2.email], fail_silently = False)
        elif form.cleaned_data.get('is_verificated') == False:
            nama_haki = form.cleaned_data.get('judul')
            pengusul = form.cleaned_data.get('pengusul')
            pengusuls = User.objects.get(first_name=pengusul)
            # print(pengusuls.email)
            subject = 'Konfirmasi Revisi Upload Haki'
            pk = self.kwargs['pk']
            alasan = self.request.POST['alasan']
            import os 
            dir_path = os.path.dirname(os.path.realpath(__file__))
            mes = open(dir_path + '/emailer/revisi_haki.txt', 'r')
            message = mes.read().format(pengusul, nama_haki, pengusul, alasan, pk)
            # print(message)
            send_mail(subject, message, EMAIL_HOST_USER, [pengusuls.email, 'difa_only@yahoo.com', 'yoni.kuwantoro@unpad.ac.id'], fail_silently = False)
        return super(VerifikasiBerkasHakiView, self).form_valid(form)

class PenilaianBerkasHakiView(ReviewerAccess, CreateView):
    model = PenilaianBerkasHaki
    login_url = '/login/'
    form_class = PenilaianBerkasHakiForm
    template_name = 'penilaian/penilaian_berkas_haki.html'
    context_object_name = 'penilaian_berkas_haki'
    def get_success_url(self):
        return reverse('penilaian:list_penilaian_haki', kwargs={'page':1})

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
        slug = slugify(UploadBerkasHaki.objects.get(slug=berkas.slug))
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/penilaian_haki.txt', 'r')
        message = mes.read().format(pengusul, berkas, pengusul, '1', 'R1', slug)
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasHakiView, self).form_valid(form)

class PenilaianBerkasHaki2View(ReviewerAccess, CreateView):
    model = PenilaianBerkasHaki2
    login_url = '/login/'
    form_class = PenilaianBerkasHaki2Form
    template_name = 'penilaian/penilaian_berkas_haki2.html'
    context_object_name = 'penilaian_berkas_haki'
    def get_success_url(self):
        return reverse('penilaian:list_penilaian_haki', kwargs={'page':1})

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
        slug = slugify(UploadBerkasHaki.objects.get(slug=berkas.slug))
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mes = open(dir_path + '/emailer/penilaian_haki.txt', 'r')
        message = mes.read().format(pengusul, berkas, pengusul, '2', 'R2', slug)
        # print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [pengusul.email], fail_silently = False)
        return super(PenilaianBerkasHaki2View, self).form_valid(form)

class PenilaianBerkasHakiEditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasHaki
    login_url = '/login/'
    form_class = PenilaianBerkasHakiEditForm
    template_name = 'penilaian/edit_penilaian_haki.html'

    def get_success_url(self):
        return reverse('penilaian:list_penilaian_haki', kwargs={'page':1})

class PenilaianBerkasHaki2EditView(ReviewerAccess, UpdateView):
    model = PenilaianBerkasHaki2
    login_url = '/login/'
    form_class = PenilaianBerkasHaki2EditForm
    template_name = 'penilaian/edit_penilaian_haki2.html'

    def get_success_url(self):
        return reverse('penilaian:list_penilaian_haki', kwargs={'page':1})

class HasilPenilaianHakiView(LoginRequiredMixin, DetailView):
    model = PenilaianBerkasHaki
    login_url = '/login/'
    template_name = 'penilaian/hasil_rekap_haki.html'
    context_object_name = 'rekap_haki'
    
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return redirect('penilaian:error_message')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context
        
    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

class HasilPenilaianHaki2View(LoginRequiredMixin, DetailView):
    model = PenilaianBerkasHaki2
    login_url = '/login/'
    template_name = 'penilaian/hasil_rekap_haki2.html'
    context_object_name = 'rekap_haki'
    
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return redirect('penilaian:error_message')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['usrlogin'] = self.request.user
        return context
        
    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

class HasilPenilaianBerkasHakiGabunganView(LoginRequiredMixin, TemplateView):
    template_name = 'penilaian/hasil_rekap_gabungan_haki.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HasilPenilaianBerkasHakiGabunganView, self).get_context_data(*args, **kwargs)
        berkas = PenilaianBerkasHaki.objects.get(slug = self.kwargs['slug'])
        berkas_2 = PenilaianBerkasHaki2.objects.get(slug = self.kwargs['slug'])
        context['berkas'] = berkas
        context['berkas_2'] = berkas_2
        context['usrlogin'] = self.request.user
        if berkas.nilai_pu != 0:
            context['nilaitotal_pu'] = ((berkas.nilai_pu + berkas_2.nilai_pu)/2)
        if berkas.nilai_pl != 0:
            context['nilaitotal_pl'] = ((berkas.nilai_pl + berkas_2.nilai_pl)/2)
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
    login_url = '/login/'
    template_name = 'penilaian/list_reviewer_jurnal.html'
    context_object_name = 'list_reviewer_jurnal'
    # paginate_by = 5
    ordering = ['-uploaded']
    
    def get_context_data(self, *args, **kwargs):
        context = super(ListReviewerJurnalView, self).get_context_data(*args, **kwargs)
        context['list_berkas'] = PenilaianBerkasJurnal.objects.all()
        context['list_berkas_2'] = PenilaianBerkasJurnal2.objects.all()
        return context
    
    def get_queryset(self):
        result = super(ListReviewerJurnalView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = UploadBerkasJurnal.objects.filter(judul_artikel__icontains=query)
            result = postresult
        return result

class ListReviewerProsidingView(ReviewerAccess,ListView):
    model = UploadBerkasProsiding
    login_url = '/login/'
    template_name = 'penilaian/list_reviewer_prosiding.html'
    context_object_name = 'list_reviewer_prosiding'
    # paginate_by = 5
    ordering = ['-uploaded']

    def get_context_data(self, *args, **kwargs):
        context = super(ListReviewerProsidingView, self).get_context_data(*args, **kwargs)
        context['list_berkas'] = PenilaianBerkasProsiding.objects.all()
        context['list_berkas_2'] = PenilaianBerkasProsiding2.objects.all()
        return context
    
    def get_queryset(self):
        result = super(ListReviewerProsidingView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = UploadBerkasProsiding.objects.filter(judul_artikel__icontains=query)
            result = postresult
        return result

class ListReviewerBukuView(ReviewerAccess,ListView):
    model = UploadBerkasBuku
    login_url = '/login/'
    template_name = 'penilaian/list_reviewer_buku.html'
    context_object_name = 'list_reviewer_buku'
    # paginate_by = 5
    ordering = ['-uploaded']

    def get_context_data(self, *args, **kwargs):
        context = super(ListReviewerBukuView, self).get_context_data(*args, **kwargs)
        context['list_berkas'] = PenilaianBerkasBuku.objects.all()
        context['list_berkas_2'] = PenilaianBerkasBuku2.objects.all()
        return context

    def get_queryset(self):
        result = super(ListReviewerBukuView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = UploadBerkasBuku.objects.filter(judul__icontains=query)
            result = postresult
        return result

class ListReviewerHakiView(ReviewerAccess,ListView):
    model = UploadBerkasHaki
    login_url = '/login/'
    template_name = 'penilaian/list_reviewer_haki.html'
    context_object_name = 'list_reviewer_haki'
    # paginate_by = 5
    ordering = ['-uploaded']

    def get_context_data(self, *args, **kwargs):
        context = super(ListReviewerHakiView, self).get_context_data(*args, **kwargs)
        context['list_berkas'] = PenilaianBerkasHaki.objects.all()
        context['list_berkas_2'] = PenilaianBerkasHaki2.objects.all()
        return context

    def get_queryset(self):
        result = super(ListReviewerHakiView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = UploadBerkasHaki.objects.filter(judul__icontains=query)
            result = postresult
        return result
############# END List khusus reviewer #############
################################################################################################################