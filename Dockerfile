FROM python:3.10

RUN pip install git+https://github.com/hwchase17/langchain.git

# install requirements
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt





