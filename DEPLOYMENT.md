# Production Deployment Guide

This document describes recommended steps for deploying **K666** in a production environment. The instructions in `README.md` focus on local development, while this guide covers a typical production setup.

## Prerequisites

- A server running Linux with Python 3.8 or newer.
- A production-ready database such as PostgreSQL.
- A Web server capable of running WSGI applications (e.g. Gunicorn behind Nginx).
- Access to the repository and ability to install Python packages.

## 1. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## 2. Configure Environment Variables

Copy `.env.example` to `.env` and edit the values:

- **`SECRET_KEY`** – set to a unique, unpredictable string.
- **`DEBUG`** – leave unset or set to `False`.
- **`DEFAULT_DATABASE`** – set to `postgresql` to use the PostgreSQL settings in `k666/settings.py`.
- **`ALLOWED_HOSTS`** – update `k666/settings.py` with the hostname(s) your site will serve.

## 3. Prepare the Database

Create the production database and run migrations:

```bash
python manage.py migrate
```

Create an administrative user if needed:

```bash
python manage.py createsuperuser
```

## 4. Collect Static Files

Define `STATIC_ROOT` in your environment or `k666/settings.py` and collect static assets:

```bash
python manage.py collectstatic
```

## 5. Run the Application

Use a WSGI server such as Gunicorn and place a web server like Nginx in front of it:

```bash
gunicorn k666.wsgi:application --bind 0.0.0.0:8000
```

Configure Nginx (or another reverse proxy) to forward requests to Gunicorn and handle TLS termination.

## 6. Security Settings

- Ensure `DEBUG` is disabled.
- Set `ALLOWED_HOSTS` to your domain name(s).
- Use HTTPS and configure a strong TLS certificate.

## 7. Monitoring and Maintenance

Monitor logs from Gunicorn and your web server. Apply database migrations whenever deploying new versions and keep `requirements.txt` packages updated.

---

Refer back to `README.md` for local development instructions.
