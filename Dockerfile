FROM python:3.11

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y libgl1 poppler-utils

RUN pip install vila

COPY convert.py ./

RUN python convert.py

CMD [ "python", "convert.py" ]