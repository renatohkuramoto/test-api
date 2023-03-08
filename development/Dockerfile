FROM python:3.10

ADD development/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY development/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 755 /usr/local/bin/entrypoint.sh \
    && ln -s /usr/local/bin/entrypoint.sh /

EXPOSE 80

ENTRYPOINT [ "entrypoint.sh" ]
