FROM python3.9

COPY requirements.txt ./build/requirements.txt

RUN pip install -r /build/requirements.txt

COPY . ./build

WORKDIR /build

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$PORT"]