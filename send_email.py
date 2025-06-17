import requests, json

url = "https://script.googleusercontent.com/macros/s/AKfycb…/exec"  # כתובת ה-Web App שלך

payload = {
  "action": "sendEmail",
  "params": {
    "to": "someone@example.com",
    "subject": "בדיקה",
    "body": "שלום! הודעת מבחן 🎉",
    "attachmentIds": []   # אם תרצה לצרף קובץ Drive, הכנס כאן את ה-ID שלו
  }
}

res = requests.post(url, json=payload)
print(res.json())   # אמור להחזיר { "ok": true }
