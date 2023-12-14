FROM python:3.9
WORKDIR /grasp-web/

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

#ENV SECRET_KEY=
#ENV DATABASE_URL=

RUN mkdir /data/ && \
    mkdir /data/upload/ && mkdir /data/download/ && \
    mkdir /data/results/ && mkdir /data/charts/
ENV UPLOAD_FOLDER=/data/upload/
ENV DOWNLOAD_FOLDER=/data/download/
ENV RESULTS_FOLDER=/data/results/
ENV CHARTS_FOLDER=/data/charts/

EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0" ]

# build image with 'docker build -t grasp .'
# run container with 'docker run -p 5000:5000 -it --rm grasp'