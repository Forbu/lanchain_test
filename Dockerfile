FROM python:3.7

# install requirements
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt




