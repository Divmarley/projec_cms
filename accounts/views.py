
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.views import View
from accounts.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate,login,logout
from accounts.models import User

# Create your views here.

class SignupView(View):
    template_name= 'signup.html'
    def get(self,request):
       
        users =User.objects.all()
        form =SignupForm()
        context={
            'form_key':form,
            "users_me":users
        }
        return render(request,self.template_name,context)

    def post(self, request):
        form = SignupForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password) 
            login(request, user)
            return redirect("blow:dashboard")
        return render(request, self.template_name, {'form': form.errors})
        # return redirect('account:dashboard')
    

class DashboardView(View):
    def get(self,request):
        template_name= 'dashboard.html'
        users =User.objects.all()
        form =SignupForm()
        context={
            'form_key':form,
            "users_me":users
        }
        return render(request,template_name,context)



# login
class LoginView(View):
    form_class = LoginForm
    template_name = "login.html"

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated and request.user.is_active and request.user.is_superuser==True:
            return redirect("blow:dashboard")
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password) 
            if user.is_active:
                login(request, user)
                redirect_url = self.request.GET.get('redirect_to', 'blow:dashboard')
                return redirect(redirect_url)
            else:
                messages.error(request, 'Your account is not activated.')

        return render(request, self.template_name, {'form': form})



class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('blow:login')
