import os
import os.path

from worker.worker import app
import requests

@app.task
def upload_csv_to_db(location, document_id):
    from app.models import Document, Product
    import csv
    from django_eventstream import send_event
    total = 0
    doc = Document.objects.get(pk=document_id)
    #Find total objects
    with open(location) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        total = sum(1 for row in csv_reader)
    doc.elements = total
    doc.save()
    
    with open(location) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            if line == 0:
                print(str(row))
                line +=1
            else:
                product,status = Product.objects.update_or_create(sku=row[1].lower(), defaults={ 'name':row[0], 'description':row[2], 'document':doc})
                r = requests.post("http://0.0.0.0:8000/sse/post_event", data={'sku': str(product.sku), 'curr': str(line), 'total': str(total)})
                print(r.status_code, r.reason)
                line +=1
