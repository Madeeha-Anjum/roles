FROM python:3.14.0-slim-trixie

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


# Ensures that Python output is sent straight to terminal (e.g., your container log) without being buffered first
ENV PYTHONUNBUFFERED 1 