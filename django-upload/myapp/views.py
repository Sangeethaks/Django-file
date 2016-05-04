from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from myapp.models import Document
from myapp.forms import DocumentForm
import sys, zipfile, os, os.path,fnmatch
from zipfile import ZipFile, ZIP_DEFLATED 



def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if str(request.FILES['docfile']).endswith('zip'):
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save() 
            BASE_DIR = os.path.dirname(os.path.dirname(__file__))
            file_path = os.path.join(BASE_DIR,'uploaded_files/documents')
            pattern = '*.zip'
            for root,dirs,files in os.walk(file_path):
            	for filename in fnmatch.filter(files,pattern):        		
            		zipfile.ZipFile(os.path.join(root,filename)).extractall(os.path.join(root,os.path.splitext(filename)[0]))    		
            return HttpResponse("<h2> File uploaded successfully </h2>")
        else:
            return HttpResponse("<h2> Upload only zip files.Other files cannot be uploaded !!</h2> <br> <h2> Upload Unsuccessful </h2> ")

    else:
        form = DocumentForm() 
    documents = Document.objects.all()
    return render_to_response(
        'myapp/list.html',
        {'form': form},
        context_instance=RequestContext(request)
    )




