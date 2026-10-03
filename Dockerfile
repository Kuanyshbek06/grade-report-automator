FROM python:3.13-slim

WORKDIR /app

COPY src ./src
COPY data ./data

RUN mkdir -p output

CMD ["python", "src/report_generator.py"]