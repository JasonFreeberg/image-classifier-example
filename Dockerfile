# TODO:

# Use one of the Python base images from DockerHub
# Copy backend and frontend directory
# Build Flask app (you don't need to use a virtual env because there's only this one app)
# Set entrypoint for "python main.py" just like when you run it locally

FROM python:3


WORKDIR /IMAGE-CLASSIFIER-EXAMPLE

ADD . /IMAGE-CLASSIFIER-EXAMPLE


COPY ./backend/image-upload-api/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000
# frontend stuff won't work
CMD [ "python3", "./backend/image-upload-api/flask-api/main.py","--host=0.0.0.0"]

