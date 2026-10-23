#!/usr/bin/env python3
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_TOTAL_ATTACHMENT_SIZE = 10 * 1024 * 1024  # 10MB

APPLICATIONS = [
    {
        "reference": "DPSA/IT/2026/001",
        "position": "IT Specialist",
        "email": "psvc@dpsa.gov.za",
        "pdf": "Z83_DPSA_IT_2026_001.pdf",
    },
    {
        "reference": "DEL/WEB/2026/045",
        "position": "Web Developer",
        "email": "career@labour.gov.za",
        "pdf": "Z83_DEL_WEB_2026_045.pdf",
    },
    {
        "reference": "DHA/SW/2026/012",
        "position": "Software Developer",
        "email": "hr@homeaffairs.gov.za",
        "pdf": "Z83_DHA_SW_2026_012.pdf",
    },
    {
        "reference": "GPG/IT/2026/078",
        "position": "IT Support",
        "email": "gpgrecruitment@gauteng.gov.za",
        "pdf": "Z83_GPG_IT_2026_078.pdf",
    },
    {
        "reference": "NT/SA/2026/003",
        "position": "Systems Analyst",
        "email": "hr@treasury.gov.za",
        "pdf": "Z83_NT_SA_2026_003.pdf",
    },
    {
        "reference": "DOT/SE/2026/021",
        "position": "Junior Engineer",
        "email": "recruitment@dot.gov.za",
        "pdf": "Z83_DOT_SE_2026_021.pdf",
    },
    {
        "reference": "DOH/DB/2026/034",
        "position": "Database Admin",
        "email": "hr@health.gov.za",
        "pdf": "Z83_DOH_DB_2026_034.pdf",
    },
    {
        "reference": "DBE/PC/2026/011",
        "position": "Project Coordinator",
        "email": "recruitment@education.gov.za",
        "pdf": "Z83_DBE_PC_2026_011.pdf",
    },
]

DEFAULT_CV_CANDIDATES = [
    "cv_v3_text.txt",
    "cv_extracted.txt",
    "cv_page-1.png",
    "cv_v3_page-1.ppm",
    "cv_extract-1.png",
    "cv_extract-1.ppm",
]


def resolve_cv_path():
    cv_path = os.environ.get("CV_PATH")
    if cv_path:
        candidate = ROOT / cv_path
        if candidate.exists():
            return candidate
        raise FileNotFoundError(f"CV file not found: {candidate}")

    for name in DEFAULT_CV_CANDIDATES:
        candidate = ROOT / name
        if candidate.exists():
            return candidate

    raise FileNotFoundError(
        "No CV file found in repo. Set CV_PATH to a valid file (for example: CV_PATH=cv_v3_text.txt)"
    )


def attach_file(message, file_path, mime_type, attachment_name):
    if not file_path.exists():
        raise FileNotFoundError(f"Missing file: {file_path}")

    file_size = file_path.stat().st_size
    if file_size > MAX_TOTAL_ATTACHMENT_SIZE:
        raise ValueError(f"{file_path.name} exceeds 10MB limit: {file_size} bytes")

    with file_path.open("rb") as fp:
        data = fp.read()

    message.add_attachment(
        data,
        maintype=mime_type.split("/")[0],
        subtype=mime_type.split("/")[1],
        filename=attachment_name,
    )
    return file_size


def build_message(application, cv_path=None):
    subject = f"APPLICATION: {application['reference']} - Fidel Nkwe - {application['position']}"
    body = """Dear Recruitment Team,

I am writing to apply for the position of {position} as advertised under reference {reference}.

Please find attached my completed Z83 application form and Curriculum Vitae.

Application Details:
- Reference Number: {reference}
- Position: {position}
- Applicant: Fidel Nkwe
- Phone: 064 551 0575
- Email: fidelkekana@gmail.com

Thank you for considering my application.

Sincerely,
Fidel Nkwe
Phone: 064 551 0575
Email: fidelkekana@gmail.com
""".format(position=application["position"], reference=application["reference"])

    message = EmailMessage()
    message["Subject"] = subject
    message["To"] = application["email"]
    sender_value = os.environ.get("SMTP_FROM") or os.environ.get("GMAIL_USER") or "noreply@example.com"
    message["From"] = sender_value
    message.set_content(body)

    pdf_path = ROOT / application["pdf"]
    pdf_size = attach_file(message, pdf_path, "application/pdf", pdf_path.name)

    cv_name = cv_path.name if cv_path else "CV.pdf"
    if cv_path:
        cv_size = attach_file(message, cv_path, "application/octet-stream", cv_name)
        if pdf_size + cv_size > MAX_TOTAL_ATTACHMENT_SIZE:
            raise ValueError(
                f"Combined Z83 + CV attachment exceeds 10MB limit: {pdf_size + cv_size} bytes"
            )

    return message


def get_smtp_config():
    gmail_user = os.environ.get("GMAIL_USER")
    gmail_password = os.environ.get("GMAIL_APP_PASSWORD")
    smtp_host = os.environ.get("SMTP_HOST") or ("smtp.gmail.com" if gmail_user else None)
    smtp_port = os.environ.get("SMTP_PORT") or ("587" if gmail_user else "587")
    smtp_username = os.environ.get("SMTP_USERNAME") or gmail_user
    smtp_password = os.environ.get("SMTP_PASSWORD") or gmail_password

    return smtp_host, int(smtp_port), smtp_username, smtp_password


def send_email(message):
    host, port, username, password = get_smtp_config()

    if not host or not username or not password:
        raise RuntimeError(
            "SMTP configuration is missing. Add Gmail secrets: GMAIL_USER and GMAIL_APP_PASSWORD, or SMTP_HOST/SMTP_USERNAME/SMTP_PASSWORD."
        )

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(message)


def main():
    dry_run = os.environ.get("DRY_RUN", "true").lower() == "true"
    cv_path = resolve_cv_path() if os.environ.get("CV_PATH") or any((ROOT / name).exists() for name in DEFAULT_CV_CANDIDATES) else None

    for application in APPLICATIONS:
        message = build_message(application, cv_path=cv_path)
        if dry_run:
            print(f"DRY RUN: {application['email']} :: {message['Subject']} :: CV={cv_path.name if cv_path else 'none'}")
            continue

        send_email(message)
        print(f"Sent {application['reference']} to {application['email']}")


if __name__ == "__main__":
    main()
