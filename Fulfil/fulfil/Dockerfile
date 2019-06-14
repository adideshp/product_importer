# start from an official image
FROM python:3.6

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install our two dependencies
RUN pip install gunicorn django psycopg2 djangorestframework requests celery channels django-eventstream

# copy our project code
COPY . /opt/services/djangoapp/src

# expose the port 8000
EXPOSE 8000
EXPOSE 9000

# define the default command to run when starting the container
#CMD ["gunicorn", "--chdir", "fulfil", "--bind", ":8000", "fulfil.wsgi:application"]
CMD sh commands.sh