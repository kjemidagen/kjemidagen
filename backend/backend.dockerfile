FROM python:3.11

SHELL [ "/bin/bash", "-ec" ]

COPY ./requirements.txt /setupdir/
RUN pip install --no-cache-dir -r /setupdir/requirements.txt

COPY ./ /app/
