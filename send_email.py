import smtplib
from email.message import EmailMessage
from pathlib import Path      # רק אם תרצה צרופות

# ========= הגדרות =========
EMAIL      = "הכתובת-שלך@gmail.com"
APP_PASS   = "ueeicwrdprwwrzzq"          # סיסמת-האפליקציה שהפקת
SMTP_HOST  = "smtp.gmail.com"
SMTP_PORT  = 465                        # SSL

TO         = "someone@example.com"
SUBJECT    = "בדיקה"
BODY       = "שלום! זהו מייל בדיקה ✉️"

ATTACHMENTS = [
    # Path("docs/report.pdf"),
    # Path("images/pic.jpg"),
]

# ========= בניית ההודעה =========
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"]   = TO
msg["Subject"] = SUBJECT
msg.set_content(BODY)

for file_path in ATTACHMENTS:
    data = file_path.read_bytes()
    msg.add_attachment(
        data,
        maintype="application",
        subtype="octet-stream",
        filename=file_path.name,
    )

# ========= שליחה =========
with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
    smtp.login(EMAIL, APP_PASS)
    smtp.send_message(msg)

print("✓ המייל נשלח בהצלחה")
