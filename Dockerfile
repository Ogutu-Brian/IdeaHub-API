# Pull base image

FROM python:3.7

#Environment variables
ENV PYTHONDONTWRITEBYTHECODE 1
ENV PYTHONUNBUFFERED 1

#Work directory
RUN mkdir /code
WORKDIR /code

# install psycopg2 dependencies


# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt


# Copy project
COPY . /code/
