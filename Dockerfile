FROM python:3.13
WORKDIR /app
COPY ./app .
RUN pip3 install -r requirements.txt --break-system-packages
RUN cd 
CMD ["gunicorn" ,"--bind" ,"0.0.0.0:5005" ,"main:app"]  