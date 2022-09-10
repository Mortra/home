
from django.shortcuts import render, HttpResponse, redirect


from .models import Client, Order
from .forms import OrderForm, ClientForm
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView, FormView
from django.views import View
#создаем views


# def clients_list(request):
#     context = {}
#     context["clients"] = Client.objects.all()
#     return render(request, 'clients.html', context)
class ClientsListView(ListView):
    model = Client
    template_name = 'clients.html'



# def client_detail(request, id):
#     contex = {
#         "client": Client.objects.get(id=id)
#         #SELECT * FROM Client WHERE id+id:
#     }
#     return render(request, "client_info.html", contex)
class ClientDetailView(DetailView):
    model = Client
    template_name = "client_info.html"



# def order_list(request):
#     context = {}
#     context["clients"] = Order.objects.all()
#     return render(request, 'orders.html', context)
class OrderlistView(ListView):
    model = Order
    template_name = "orders.html"



# def order_detail(request, id):
#     context = {
#         "order": Order.objects.get(id=id)
#         #SELECT * FROM Clients WHERE id+id
#     }
#     return render(request, "order_info.html", context)
class OrderDetailViews(DetailView):
    model = Order
    template_name = "order_info.html"



def client_update(request, id):
    contex = {}
    client_object = Client.objects.get(id=id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client_object)
        if form.is_valid():
            client_object = form.save()

    contex["form"] = ClientForm(instance=client_object)
    return render(request, 'client_update.html', contex)



# def create_order(request):
#     if request.method == "POST":
#         data = request.POST
#         order = Order()
#         order.name = data["name"]
#         order.contacts = data["contacts"]
#         order.descriptions = data["description"]
#         order.save()
#         return HttpResponse("Форма обработана")
#     return render(request, 'core/order_form.html')
class CreateOrderView(View):
    def post(self, request):
        data = request.POST
        order = Order()
        order.name = data["name"]
        order.address = data["address"]
        order.contacts = data["contacts"]
        order.descriptions = data["description"]
        order.save()
        return HttpResponse("Форма обработана",)

    def get(self, request):
        return render(request, 'core/order_form.html')




# def order_djangoform(request):
#     context = {}
#     if request.method =="POST":
#         order_form = OrderForm(request.POST)
#         if order_form.is_valid():
#             order_form.save()
#             return HttpResponse("Форма обработана")
#         return HttpResponse("Данные не валидны")
#     context["order_form"] = OrderForm()
#     return render(request, 'order_djangoform', context)
class CreateOrderDjangoForm(CreateView):
    model = Order
    template_name = "order_djangoform.html"
    fields = ["name", "address", "contacts", "descriptions"]
    success_url = "/order/"

    #Вызывает текст "7"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context["our_number"] = 7
    #     return context

