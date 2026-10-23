#!/usr/bin/env bash
set -euo pipefail

if [ -f .env ]; then
  set -a
  . ./.env
  set +a
fi

if [ -z "${GMAIL_USER:-}" ] || [ -z "${GMAIL_APP_PASSWORD:-}" ] || [ -z "${SMTP_FROM:-}" ]; then
  echo "Missing required env values. Update .env or export GMAIL_USER, SMTP_FROM, and GMAIL_APP_PASSWORD."
  exit 1
fi

DRY_RUN="${DRY_RUN:-false}"
CV_PATH="${CV_PATH:-cv_v3_text.txt}"

DRY_RUN="$DRY_RUN" CV_PATH="$CV_PATH" python3 scripts/send_applications.py
