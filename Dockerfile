# set base image (host OS)
FROM --platform=darwin/amd64 python:3.7

# set the working directory in the container
WORKDIR /guesslang

# copy the dependencies file to the working directory
COPY /guesslang .

# install dependencies
RUN pip install -r requirements.txt

RUN ls -la
RUN pyinstaller guesslang/__main__.py -n guess -y --additional-hooks-dir ./hooks/ --add-data ./guesslang/data/:./guesslang/data/ --onefile

CMD ["sleep", "99999999"]