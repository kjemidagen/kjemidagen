FROM python:3.10-bullseye

COPY ./requirements.txt /setupdir/
RUN pip install --no-cache-dir -r /setupdir/requirements.txt
