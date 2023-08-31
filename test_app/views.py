from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DeleteView
from test_app.models import Order
from django.contrib import messages
from datetime import datetime

# Create your views here.


class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    queryset = Order.objects.all()
    login_url = 'login/'


class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'
    form_class = AuthenticationForm


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = '/'


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    success_url = '/'
    queryset = Order.objects.all()

    def form_valid(self, form):
        if self.object:
            messages.success(
                self.request,
                f'Задача №{self.object.id}-{self.object.task_id} '
                f' під назвою {self.object.name} '
                f'була опрацьована {self.object.employee.first_name + " " + self.object.employee.position} '
                f'у {datetime.now()}.'
            )

        return super().form_valid(form=form)
