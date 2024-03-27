# Use the official Python image as a base image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get -y update && apt-get install -y \
    wget \
    gnupg \
    lsb-release
RUN pip install -U pip \
    && apt install -y curl netcat 


# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code
RUN pip install -r requirements.txt
# Copy the current directory into the container at /code/Travans
COPY . /code

# Copy the .env file into the container
COPY .env /code

RUN ["chmod", "+755", "entrypoint.sh"]
ENTRYPOINT ["/code/entrypoint.sh"]
