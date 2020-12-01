from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
import boto3
from botocore.exceptions import ClientError
from typing import Optional
from .models import File



    #Must update the .aws/credentials with aws student session token every time!
    #Remeber for demo
def create_presigned_url(bucket_name: str, object_name: str, expiration=300) -> Optional[str]:
    #Grab current session
    s3_client = boto3.session.Session().client('s3')

    try:
        #Attempts to generate a presigned url given the above parameters
        response = s3_client.generate_presigned_url('get_object',Params={'Bucket': bucket_name,'Key': object_name},ExpiresIn=expiration)
    except ClientError as e:
        print(e)
        return None
    return response


# function that calls above function to create presigned url
def generate_presigned_url(item):
    bucket_name = "uploads-project"
    bucket_resource_url = "bidden.jpg" #"https://s3.us-east-1.amazonaws.com/" + bucket_name + "/" + item
    url = create_presigned_url(bucket_name,bucket_resource_url)
    return {
        'url': url
    }


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


# uses the home.html template to show the files as a single item
class FileDetailView(DetailView):
    model = File
    # do the s3 link view here
    # add a link attr to file
    # display it on file_detail
    File.link = generate_presigned_url(File.name)['url']
    print(File.link)

# shows new item for a post
class FileCreateView(CreateView):
    model = File
    fields = ['name','content', 'extension', 'link']

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
    return render(request, 'uploads/upload.html')
