FROM python:3.9

ENV FLASK_APP run.py
ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PATH "/app/scripts:${PATH}"

EXPOSE 8000

WORKDIR /app
COPY run.py requirements*  /app/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /app/

RUN ["chmod", "+x", "/app/scripts/website-entrypoint.sh"]
ENTRYPOINT website-entrypoint.sh
CMD ['run']