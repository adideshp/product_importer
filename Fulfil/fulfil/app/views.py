from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from worker.tasks import upload_csv_to_db
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            upload_csv_to_db.delay(form.instance.document.url, form.instance.id)
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'app/document_upload.html', {
        'form': form
    })


@csrf_exempt
def push_sse(request):
    from django_eventstream import send_event
    if request.method == 'POST':
        sku = request.POST["sku"]
        curr = request.POST["curr"]
        total = request.POST["total"]
        doc_id = request.POST["doc_id"]
        send_event('test', 'message', {'sku': str(sku), 'curr': str(curr), 'total': str(total), 'doc_id': str(doc_id)})
    return HttpResponse({"status": "Event Sent"}, content_type="application/json")

def home(request):
    documents = Document.objects.all()
    return render(request, 'app/home.html', { 'documents': documents })