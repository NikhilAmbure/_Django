#base image
FROM python:3.10-slim 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1  
#prevents python from buffering print statements or loggers

# working directory
WORKDIR /code

COPY requirements.txt /core/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /core/

