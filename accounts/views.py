from django.shortcuts import redirect, render
from django.views import View

from accounts.form import LoginForm, SignupForm

# Create your views here.


def login_view(request):
    template_name="login.html"
    form = LoginForm()
    context={
        "form_me":form
    }
    return render(request,template_name,context)


# def signup_view(request):
#     template_name="signup.html" 
#     context={ 
#         "form_key":SignupForm()
#     }
#     return render(request,template_name,context)


class SignupView(View):
    def get(self, request):
        template_name="signup.html" 
        context={ 
            "form_key":SignupForm()
        }
        return render(request,template_name,context)

    def post(self,request):
        form= SignupForm(request.POST)
        user  =form.save(commit=False)
        password =form.cleaned_data['password']
        user.set_password(password)
        user.save()

        return redirect('accountsss:signup')