from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,ListView,UpdateView
from socialweb.forms import RegistrationForm,LoginForm,UserprofileForm,PostForm,CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from api.models import Userprofile,Post
from django.urls import reverse_lazy
from api.models import Post,Comments


# Register your models here.
class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")
    # def get(self,request,*args,**kwargs):
    #     form=RegistrationForm()
    #     return render(request,"register.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=RegistrationForm(request.POST)
    #     if form.is_valid():
    #         return redirect("signin")
    #     else:
    #         return render(request,"register.html",{"form":form})
            

class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                 return render(request,"login.html",{"form":form})

class HomeView(CreateView,ListView):
    model=Post
    form_class=PostForm
    template_name="index.html"
    success_url=reverse_lazy("home")
    context_object_name="posts"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        return Post.objects.all().order_by("-date")

class ProfileCreateView(CreateView):
    model=Userprofile
    form_class=UserprofileForm
    template_name="userprofile.html"
    success_url=reverse_lazy("profile_detail")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    

class UserprofileView(TemplateView):
    template_name="profile_detail.html"
    

    # def get(self,request,*args,**kwargs):
    #     qs=Userprofile.objects.filter(user=request.user)
    #     return render(request,"profile_detail.html",{"profile":qs})

class AddCommentView(View):
    def post(self,request,*args,**kwargs):
        pid=kwargs.get("id")
        pos=Post.objects.get(id=pid)
        usr=request.user
        com=request.POST.get("comment")
        Comments.objects.create(user=usr,post=pos,comment=com)
        return redirect("home")
        
    
class ProfileUpdateView(UpdateView):
    model=Userprofile
    form_class=UserprofileForm
    template_name="profile-change.html"
    success_url=reverse_lazy("home")
    pk_url_kwarg="id"

class UpvoteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        po=Post.objects.get(id=id)
        po.upvote.add(request.user)
        po.save()
        return redirect("home")
    
class PostDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Post.objects.get(id=id).delete()
        return redirect("home")
    
class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")

class UpvoteRemoveView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        po=Post.objects.get(id=id)
        po.upvote.remove(request.user)
        po.save()
        return redirect("home")    
    
class Commentupvoteview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        co=Comments.objects.get(id=id)
        co.upvote.add(request.user)
        co.save()
        return redirect("home")
    
class CommentdeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Comments.objects.get(id=id).delete()
        return redirect ("home")