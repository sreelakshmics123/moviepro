from django.shortcuts import render
from app.models import Movie
from app.forms import movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# def home(request):
#     m=Movie.objects.all()
#     return render(request,'home.html',{'m':m})



class MovieList(ListView):    #ListView displays all objects/records retrieving from a model.
    model=Movie
    template_name="home.html"
    context_object_name="m"




# def details(request,p):
#     m=Movie.objects.get(name=p)
#     return render(request,'details.html',{'m':m})

class MovieDetail(DetailView):     #dispalys a particular object retrieving from a model
    model=Movie
    template_name="details.html"
    context_object_name="m"


class MovieAdd(CreateView):
    model=Movie
    template_name="addmovie.html"
    fields='__all__'
    success_url=reverse_lazy('app:home')


class Movieupdate(UpdateView):
    model=Movie
    template_name="update.html"
    fields='__all__'
    success_url=reverse_lazy('app:home')


class Moviedelete(DeleteView):
    model=Movie
    success_url=reverse_lazy('app:home')
    template_name="delete.html"




# def update(request,p):
#     m=Movie.objects.get(name=p)
#     if(request.method=="POST"):
#         form=movieform(request.POST,request.FILES,instance=m)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     form=movieform(instance=m)
#     return render(request,'update.html',{'form':form})

# def delete(request,p):
#     m=Movie.objects.get(name=p)
#     m.delete()
#     return home(request)