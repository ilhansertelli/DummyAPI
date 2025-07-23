FROM python:3.11-slim

# Install Git and required libraries
RUN apt-get update && apt-get install -y \
    git

RUN pip install --upgrade --no-cache-dir pip

COPY dummy-api /home/codes/dummy-api

WORKDIR /home/codes/dummy-api

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 88

ENTRYPOINT [ "python", "main.py" ]