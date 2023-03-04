from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CommentForm

# Create your views here.

def home(request):
    comments = Comment.objects.order_by('-date_added')
    context = {'comments':comments}
    return render(request, 'foods/home.html', context)

@login_required
def editcomment(request, id):
    comment = Comment.objects.filter(owner=request.user).order_by('-date_added')
    comment = Comment.objects.get(id=id)
    if comment.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('foods:viewyourcomment'))
    context = {'comment': comment, 'form': form}
    return render(request, 'foods/editcomment.html', context)

@login_required
def viewyourcomment(request):
    comments = Comment.objects.filter(owner=request.user).order_by('-date_added')
    context = {'comments': comments}
    return render(request, 'foods/viewyourcomment.html', context)

@login_required
def addcomment(request):
    if request.method != 'POST':
        form = CommentForm() 
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.owner = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse('foods:viewyourcomment'))
    context = {'form': form}
    return render(request, 'foods/addcomment.html', context)

@login_required
def deletecomment(request, id):
    Foods = Comment.objects.filter(owner=request.user).order_by('-date_added')
    Foods=Comment.objects.get(id=id)
    if Foods.owner != request.user:
        raise Http404
    Foods.delete()
    return HttpResponseRedirect(reverse('foods:viewyourcomment'))

@login_required
def contactus(request):
    return render(request, 'foods/contactus.html')

@login_required
def aboutus(request):
    return render(request, 'foods/aboutus.html')

class register(CreateView):
    model = User  
    form_class = RegisterForm
    template_name= 'foods/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')
