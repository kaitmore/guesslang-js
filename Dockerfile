# set base image (host OS)
FROM --platform=darwin/amd64 python:3.7

# set the working directory in the container
WORKDIR /guesslang

# copy the dependencies file to the working directory
COPY /guesslang .

# install dependencies
RUN pip install -r requirements.txt

RUN ls -la
RUN ./build.sh

CMD ["sleep", "99999999"]