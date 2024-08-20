# pull python 3.8
FROM python:3.8

# set working directory
WORKDIR /code

# copy dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy source code to the working directory
COPY src/ .

# executes rm.config.py in python
ENTRYPOINT ["python", "rm_config.py"]
