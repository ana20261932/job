#!/usr/bin/env python3
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

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


def build_message(application):
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
    message["From"] = os.environ.get("SMTP_FROM", "noreply@example.com")
    message.set_content(body)

    pdf_path = ROOT / application["pdf"]
    if not pdf_path.exists():
        raise FileNotFoundError(f"Missing PDF: {pdf_path}")

    with pdf_path.open("rb") as fp:
        pdf_data = fp.read()

    message.add_attachment(
        pdf_data,
        maintype="application",
        subtype="pdf",
        filename=pdf_path.name,
    )
    return message


def send_email(message):
    host = os.environ.get("SMTP_HOST")
    port = int(os.environ.get("SMTP_PORT", "587"))
    username = os.environ.get("SMTP_USERNAME")
    password = os.environ.get("SMTP_PASSWORD")

    if not host or not username or not password:
        raise RuntimeError(
            "SMTP configuration is missing. Set SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, and SMTP_FROM as GitHub secrets."
        )

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(message)


def main():
    dry_run = os.environ.get("DRY_RUN", "true").lower() == "true"

    for application in APPLICATIONS:
        message = build_message(application)
        if dry_run:
            print(f"DRY RUN: {application['email']} :: {message['Subject']}")
            continue

        send_email(message)
        print(f"Sent {application['reference']} to {application['email']}")


if __name__ == "__main__":
    main()
