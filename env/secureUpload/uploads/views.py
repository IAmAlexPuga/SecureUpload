from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
from .models import File

@login_required
def home(request):
    context = {
        'posts': File.objects.all()
    }
    return render(request, 'uploads/home.html', context)

# uses the home.html template to show the files as a list
class FileListView(ListView):
    model = File
    template_name = 'uploads/home.html'
    context_object_name = 'posts'


# uses the home.html template to show the files as a list
class FileDetailView(DetailView):
    model = File

# shows new item for a post
class FileCreateView(CreateView):
    model = File
    fields = ['name','content', 'extension']

    # validates the form with the current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super().form_valid(form)


def upload(request):
    if request.method == 'POST':
        f = request.FILES['document']
        print(f.name)
        # upload the content to users db 
        home(request)
    return render(request, 'uploads/upload.html')
