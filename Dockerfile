# syntax = docker/dockerfile:1.2
FROM node:12.13.1-slim as frontend-dev
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ["django_template_project/frontend/package.json",\
      "django_template_project/frontend/package-lock.json",\
      "./"\
]
RUN --mount=type=cache,target=/root/.npm npm install
COPY django_template_project/frontend .
CMD npm run start

FROM node:12.13.1-slim as frontend-builder
WORKDIR /app
COPY --from=frontend-dev /app ./
RUN npm run build

FROM alpine as frontend-build
WORKDIR /app
COPY --from=frontend-builder /app/build ./build
COPY --from=frontend-builder /app/config ./config

FROM python:3.8.7-slim as backend-base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

ADD requirements/base.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r base.txt
ADD . ./
CMD ["./entrypoint.sh"]

FROM backend-base as backend-dev
ADD requirements/dev.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r dev.txt

FROM backend as production
ADD requirements/prod.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r prod.txt
COPY --from=frontend-build /app/build ./django_template_project/frontend/build
COPY --from=frontend-build /app/config ./django_template_project/frontend/config
RUN python manage.py collectstatic --noinput
