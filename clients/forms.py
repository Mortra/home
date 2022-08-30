from django import forms
from .models import Order, Client
from django.forms import ModelForm
from django.views.generic import DeleteView, UpdateView

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["name", "address", "contacts", "descriptions"]



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "last_name", "contacts", "address", "is_active"]


class ClientUpdateView(UpdateView):
    model = Client
    success_url = "/clients/"
    template_name = "corr/client_create.html"

    fields = ["name", "last_name", "contacts", "address"]


class DeleteUpdateView(DeleteView):
    model = Client
    success_url = "/clients/"
    template_name = "corr/delete.html"


