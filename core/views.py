from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from core.forms import *
from core.models import Bottle
from django.views.generic import ListView, View, DetailView


def contacts(request):
    return render(request, 'core/contacts.html')
# class CantactsView


# def bottle_list(request):
#     context = {}
#     context["core"] = Bottle.objects.all()
#     return render(request, 'botlle.html', context)
class BottleListView(ListView):
    model = Bottle
    template_name = "botlle.html"


# def bottle_detail(request, id):
#     contex = {
#         "bottle": Bottle.objects.get(id=id)
#         #SELECT * FROM Bottle WHERE id+id:
#     }
#     return render(request, "bottle_info.html", contex)
class BottleDetailView(DetailView):
    model = Bottle
    template_name = "bottle_info.html"


def about(request):
    return render(request, 'about.html')



def makers_list(requests):
    context  = {}
    #SELECT * FROM Bottle
    bottles_lists = Bottle.objects.all()
    context["bottles_list"] = bottles_lists
    return render(requests, 'makers.html', context)
#render - принимает запрос,


class MyView(View):
    def get(self, request):
        return render(request, "about.html")

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "core/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()))


def logout_user(request):
    logout(request)
    return redirect("/")



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно")
            return redirect('/')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, "core/register.html", {'form': form})




# def user_login(request):
#     if request.method=="POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 messages.success(request, "Успешно")
#                 return HttpResponse("url 'about.html' ")
#             else:
#                 messages.error(request, "Ошибка")
#                 return HttpResponse("<h1> Disable account </h1>")
#         else:
#             messages.info(request, "Неправильный логин или пароль ")
#             return render(request, "core/login.html")
#     else:
#         pass
#     return render(request, "core/login.html")




# class LoginView(View):
#     def get(self, request):
#         context = {"form": LoginForm()}
#         return render(request, 'core/login.html', context)
#
#     def post(self, request):
#         if request.method=="POST":
#             data = request.POST
#             user_login = data["username"]
#             password = data["password"]
#             user = authenticate(request, username=user_login, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect("/")
#                 else:
#                     return HttpResponse("<h1> Disable account </h1>")
#             else:
#                 messages.error(request, "Неправильный логин или пароль")
#         else:
#             return render(request, "login.html")






