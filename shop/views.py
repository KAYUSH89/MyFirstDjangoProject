from django.shortcuts import render
from .forms import OrderForm
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.views.generic.base import View
from .forms import FeedbackForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'products/product.html', locals())


class MyFeedback(FormView):
    form_class = FeedbackForm
    template_name = "products/feedback.html"

    def get(self, request, *args, **kwargs):
        print(request.GET)
        return super().get(request, *args, **kwargs)


class SearchResultsView(TemplateView):
    model = Product

    def post(self, request):
        query = request.POST['search']
        result_list = Product.objects.filter(name__contains=query)
        if result_list.count() != 0:
            context = {
                'result_list': result_list,
                'query': query,
            }
        else:
            context = {
                'empty': "Ничего не найдено",
                'query': query,
            }
        return render(request, 'search_result.html', context)


def order(request):
    form = OrderForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        form = form.save()

    return render(request, 'order.html', locals())


def start(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_jackets = products_images.filter(product__category__id=1)
    products_images_suits = products_images.filter(product__category__id=2)
    return render(request, 'start.html', locals())


def jackets(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_jackets = products_images.filter(product__category__id=1)
    products_images_suits = products_images.filter(product__category__id=2)
    return render(request, 'products/jackets.html', locals())


def siuts(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_jackets = products_images.filter(product__category__id=1)
    products_images_suits = products_images.filter(product__category__id=2)
    return render(request, 'products/siuts.html', locals())


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):

        return super(RegisterFormView, self).form_invalid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

