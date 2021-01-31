# Using Python 3.7 Base docker image
FROM python:3.7-slim 

# Change working directory 
WORKDIR /usr/src/app 

# Copy the content of the app folder into the working directory
COPY . .

# Run system update 
RUN apt-get -y update

# Run application
CMD ["python3", "app.py"]