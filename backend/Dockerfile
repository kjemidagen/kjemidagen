FROM python:3.10
ENV PYTHONBUFFERED=1
ENV PYTHONPATH = "${PYTHONPATH}: /root/.local/bin"
RUN pip install --upgrade pip
WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r ../tmp/requirements.txt

COPY . /app

CMD ["uvicorn", "kjemidagen.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]