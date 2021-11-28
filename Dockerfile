# # init a base image (Alpine is small Linux distro)
# FROM python:3.6.1-alpine
# # present working directory
# initialise a base image
FROM python:3.8-slim
# present working directory
WORKDIR /docker-api
# copy the contents into the working dir
COPY requirements.txt .
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
COPY . .
#Set docker env as 0.0.0.0 to mirror local env
ENV FLASK_RUN_HOST=0.0.0.0
#set port
EXPOSE 5000
#instruct docker to run flask app
CMD ["python","api.py"]

