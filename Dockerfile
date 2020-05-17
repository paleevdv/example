FROM python:3.7
RUN mkdir /app
WORKDIR /app

COPY app /app
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --deploy --system
ENV PYTHONPATH=/app
CMD ["python3", "app.py"]