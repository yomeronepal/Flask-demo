FROM python:3.8

# setup environment variable
ENV WorkDir=/app
# set work directory
RUN mkdir -p $WorkDir
WORKDIR ${WorkDir}

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

COPY . ${WorkDir}
RUN pip install -r requirements.txt
RUN flask db upgrade
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 8000
# CMD python app.py
CMD ["/entrypoint.sh"]


