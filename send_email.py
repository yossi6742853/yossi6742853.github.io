import smtplib
from email.message import EmailMessage
import os

# --- הגדרות קבועות ---
EMAIL     = "youraddress@gmail.com"          # חשבון השולח
APP_PASS  = os.environ.get("APP_PASS", "")   # סיסמת-אפליקציה (או להדביק ישירות)

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465          #  SSL

TO       = "someone@example.com"
SUBJECT  = "בדיקה"
BODY     = "שלום! זה מייל בדיקה ✉️"

# --- בניית ההודעה ---
msg = EmailMessage()
msg["From"]    = EMAIL
msg["To"]      = TO
msg["Subject"] = SUBJECT
msg.set_content(BODY)

# --- שליחה ---
with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
    smtp.login(EMAIL, APP_PASS)
    smtp.send_message(msg)

print("✓ המייל נשלח בהצלחה")
