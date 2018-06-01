# Build an debian image
FROM python:3.6

# Install SO dependecies
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    libpq-dev \
    python3-setuptools \
    gettext \
    vim \
    build-essential \
    postgresql \
    postgresql-contrib \
    apt-utils

# Install pip dependecies
RUN pip3 install --upgrade pip

# Insert Enviroment variable
ENV MODE_ENVIROMENT=production

# Create software folder
ADD . /software
WORKDIR /software
RUN pip3 install -r fga_ontology/requirements.txt

# Expose the port 8000
EXPOSE 8000

# Run the dev script before and after any command
RUN chmod +x compose/production/production.sh
ENTRYPOINT ["compose/production/production.sh"]

# Run the server
CMD ["gunicorn", "--bind 0.0.0.0:8000", "--chdir fga_ontology", "fga_ontology.wsgi"]
