FROM mcr.microsoft.com/azure-functions/python:2.0
RUN apt-get update && apt-get install -y wget gnupg apt-transport-https && \
    wget -qO - https://packages.confluent.io/deb/5.2/archive.key | apt-key add - && \
    apt-get install -y software-properties-common && \
    add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/5.2 stable main" && \
    add-apt-repository "deb http://security.debian.org/debian-security jessie/updates main"

RUN apt-get update && apt install -y librdkafka-dev

COPY . /home/site/wwwroot
ENV AZURE_FUNCTIONS_ENVIRONMENT=Development
RUN cd /home/site/wwwroot && \
    pip install --upgrade pip && \
    pip install wheel && \
    pip uninstall -y azure-functions-worker && \ 
    pip uninstall -y azure-functions && \
    pip install azure-functions-1.0.0b4.tar.gz && \
    pip install azure_functions_worker-1.0.0b4-py3-none-any.whl && \
    pip install -r requirements.txt
