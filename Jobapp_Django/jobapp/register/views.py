from django.shortcuts import render, redirect
from django.urls import reverse
from register.forms import RegisterForm

# from register.form import SubscribeForm

from register.models import Register

# Create your views here.


def register(request):
    # empty_mail = ""
    # form = SubscribeForm()
    form = RegisterForm()
    if request.POST:
        # firstname = request.POST.get('f_name'),
        # lastname = request.POST.get('l_name'),
        # email = request.POST.get('email')
        # upfirst = request.POST.get('update_f_name')
        # uplast = request.POST.get('update_l_name')

        # # hoặc email = request.POST['email']
        # print(firstname)
        # print(lastname)
        # print(email)
        # print(upfirst)
        # print(uplast)
        # if email == "":
        #     empty_mail = "email should not be empty"
        # subscribe = Register(first_name=firstname,
        #                      last_name=lastname,
        #                      email=email,
        #                      update_f_name=upfirst,
        #                      update_l_name=uplast)
        # subscribe.save()
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('Valid form')
            # first_name = form.cleaned_data['first_name'],
            # last_name = form.cleaned_data['last_name'],
            # email = form.cleaned_data['email']
            # upfirst = form.cleaned_data['update_f_name']
            # uplast = form.cleaned_data['update_l_name']
            # register = Register(first_name=first_name,
            #                      last_name=last_name,
            #                      email=email,
            #                      update_f_name=upfirst,
            #                      update_l_name=uplast)
            # register.save()

            # nếu sử dụng model form thì không cần định nghĩa field
            form.save()
            return redirect(reverse('thank_you'))
    context = {"form": form}
    return render(request, 'register/register.html', context)


def thank_you(request):
    context = {}
    return render(request, 'register/thank.html', context)
