FROM python:alpine

WORKDIR /FREQ

COPY code.py random_paragraphs.txt /FREQ/

RUN pip install nltk

CMD ["python", "code.py"]
