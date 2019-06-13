from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from worker.tasks import upload_csv_to_db
from django.core.files.storage import FileSystemStorage

def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("==============ADITYA==============")
            upload_csv_to_db.delay(form.instance.document.url, form.instance.id)
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'app/document_upload.html', {
        'form': form
    })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'app/document_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'app/document_upload.html')


def home(request):
    documents = Document.objects.all()
    return render(request, 'app/home.html', { 'documents': documents })