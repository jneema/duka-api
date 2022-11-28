FROM python:3.7.0

RUN mkdir app

COPY . .

WORKDIR /

RUN python3 -m pip install --upgrade pip
RUN pip install fastapi SQLAlchemy
RUN pip3 install -r requirements.txt
RUN pip install uvicorn
RUN pip install firebase
RUN pip install firebase-admin


CMD ["uvicorn", "app.main:app","--reload"]