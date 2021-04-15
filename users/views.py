# from django.contrib.auth.forms import PasswordChangeForm
from .forms import EditProfileForm, PasswordChangingForm, SignUpForm
from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class PasswordChangeView(SuccessMessageMixin,PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'users/ubah_password.html'
    success_url = reverse_lazy('home')
    success_message = 'Password Berhasil Diubah!'

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')
    def post(self, request, *args, **kwargs):
        pass
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            user_group = Group.objects.get(name='User')
            user.groups.add(user_group)
            return redirect('login')
        else:
            return render(request, self.template_name, {'form' : form })

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'users/ubah_data_user.html'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user