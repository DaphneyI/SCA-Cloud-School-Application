# syntax=docker/dockerfile:1

# state base image
FROM python:3.9.6-alpine

# set working directory
WORKDIR /src

# install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy app content into image
COPY . .

# specify command to be executed when running container
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]