FROM python3.9

RUN mkdir build

COPY requirements.txt ./build/requirements.txt

RUN apt update && apt install -y python3-pip                                  \
    && pip3 install -r /build/requirements.txt

COPY . ./build

WORKDIR /build

CMD ['python', './app/main.py']