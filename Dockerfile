FROM python
RUN pip install nltk
WORKDIR /FREQ

COPY code.py /FREQ
COPY random_paragraphs.txt /FREQ

CMD python code.py