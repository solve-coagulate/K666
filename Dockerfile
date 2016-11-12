FROM debian
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-psycopg2 \
    && rm -rf /var/lib/apt/lists/*
# Maybe ?
#    git \
#    python-virtualenv \
#    vim \

ENV DJANGO_SETTINGS_MODULE="k666.settings"
EXPOSE 8000

RUN pip3 install --upgrade 'pip<7' # We want this gone too! We need the latest version of pip that supports unzip.

ADD setup.py /code/setup.py
WORKDIR /code
RUN python3 setup.py install
RUN pip unzip django_messages # We want this gone!

ADD . /code
WORKDIR /code

# RUN python3 manage.py migrate
# RUN python3 manage.py createsuperuser

# ENTRYPOINT ["./docker-entrypoint.sh"]
# CMD python3 manage.py runserver 0.0.0.0:8000
CMD /code/docker-entrypoint.sh