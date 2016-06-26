FROM python:2.7
ADD . /dmm
WORKDIR /dmm
RUN pip install -r requirements.txt
CMD python dmm.py
