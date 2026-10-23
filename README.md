# Job Application Mailer

This repository contains a Python mailer that packages each Z83 application with a CV attachment and sends it to the relevant recruitment email address.

## Clone

```bash
git clone https://github.com/ana20261932/job.git
cd job
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Required environment variables

Create a local `.env` file (copy from `.env.example`), then fill in your real Gmail app password:

```bash
cp .env.example .env
source .env
```

Example values:

```bash
export GMAIL_USER="fidelkekana@gmail.com"
export SMTP_FROM="fidelkekana@gmail.com"
export GMAIL_APP_PASSWORD="YOUR_GMAIL_APP_PASSWORD"
export SMTP_HOST="smtp.gmail.com"
export SMTP_PORT="587"
export DRY_RUN="false"
export CV_PATH="cv_v3_text.txt"
```

Important:
- Use a Gmail App Password, not your normal Gmail password.
- Enable 2-Step Verification on the Gmail account first.
- `CV_PATH` should point to a small file in the repo to stay under 10 MB total.
- The safe default is `cv_v3_text.txt`.

## Run in dry-run mode

```bash
DRY_RUN=true CV_PATH=cv_v3_text.txt python3 scripts/send_applications.py
```

## Send for real

```bash
DRY_RUN=false CV_PATH=cv_v3_text.txt python3 scripts/send_applications.py
```

## One-command launcher

```bash
bash send_jobs.sh
```

The script sends each application to the department email listed in `scripts/send_applications.py` and will stop if:
- SMTP config is missing
- the CV or Z83 file is missing
- the combined attachment size exceeds 10 MB

## Notes

- The repo includes `cv_v3_text.txt` as the recommended compact CV attachment.
- The script is intentionally safe by default and only sends for real when `DRY_RUN=false`.
