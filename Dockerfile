FROM python:alpine

WORKDIR /dash-la

COPY requirements.txt .

ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY /src .

CMD ["python", "app.py"]

EXPOSE 8050