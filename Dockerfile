FROM python
ENV PYTHONBUFFERED 1 
COPY requirements.txt .
RUN apt update \
    && apt upgrade -y 
RUN apt install -y apt-utils python3-setuptools vim
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /project
COPY django /project/
WORKDIR /project
