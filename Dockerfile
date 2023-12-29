FROM python:3.12 AS requirements-stage

ARG package_name=cleankedex
ARG module_name=cleankedex

# Create structure and install poetry
WORKDIR /tmp
RUN mkdir projects
RUN pip install poetry

# Build requirements
COPY ./${package_name}/pyproject.toml ./${package_name}/poetry.lock* ./projects/${package_name}/
# WORKDIR /projects/${package_name}
RUN cd projects/${package_name} && poetry export -f requirements.txt --output requirements.txt --without-hashes

# ---------------------------------

# Build execution container
FROM python:3.12

# ARGs are needed in all the stages
ARG package_name=cleankedex
ARG module_name=cleankedex

ENV PORT 8000

EXPOSE 8000/tcp
EXPOSE 80/tcp

WORKDIR /code

# Install requirements
COPY --from=requirements-stage /tmp/projects/${package_name}/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./${package_name}/src/${module_name} /code/${module_name}

CMD ["sh", "-c", "uvicorn cleankedex.main:app --host 0.0.0.0 --port $PORT"]
