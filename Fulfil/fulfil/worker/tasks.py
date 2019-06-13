import os
import os.path

from worker.worker import app


@app.task
def upload_csv_to_db(location, document_id):
    from app.models import Document, Product
    import csv
    doc = Document.objects.get(pk=document_id)
    with open(location) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            if line == 0:
                print(str(row))
                line +=1
            else:
                product,status = Product.objects.update_or_create(sku=row[1].lower(), defaults={ 'name':row[0], 'description':row[2], 'document':doc})

