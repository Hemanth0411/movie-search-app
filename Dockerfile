FROM python:3.10-slim-bullseye AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

FROM base AS builder

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


FROM base AS final

COPY --from=builder /usr/src/app/wheels /wheels

RUN pip install --no-cache /wheels/*

COPY ./src .

EXPOSE 5000

CMD ["python", "app.py"]