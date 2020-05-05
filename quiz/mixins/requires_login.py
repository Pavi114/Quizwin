from django.contrib.auth.mixins import LoginRequiredMixin as LRMixin

class LoginRequiredMixin(LRMixin):
    login_url = '/accounts/login'
    redirect_field_name = 'next'