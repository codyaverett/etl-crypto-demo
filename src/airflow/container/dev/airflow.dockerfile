# from basic debian image
FROM python:3.10

ARG PID=1000
ARG AIRFLOW_VERSION=2.4.1
ARG CONSTRAINTS_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# Create airflow user
RUN useradd -ms /bin/bash airflow && \
    usermod -aG sudo airflow

USER airflow:$PID
WORKDIR /home/airflow

################
# Airflow setup

# set basic environment variables
ENV AIRFLOW_HOME /home/airflow
ENV PYTHON_VERSION "$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
ENV PATH $PATH:/home/airflow/.local/bin

# update pip
RUN pip install --upgrade pip

# install airflow
# Todo parameterize versions
RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.4.1/constraints-3.10.txt" && \
    pip install apache-airflow-providers-postgres etherscan-python

RUN airflow db init
COPY airflow.cfg $AIRFLOW_HOME/airflow.cfg
# airflow webserver --port 8080 && \
# airflow scheduler

# expose port 8080 for airflow webserver
EXPOSE 8080

# start airflow webserver
CMD ["airflow", "standalone"]