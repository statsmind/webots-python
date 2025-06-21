FROM python:3.11

WORKDIR /workspace
COPY . /workspace
RUN pip install .

