import requests, json

url = "https://script.googleusercontent.com/macros/s/AKfycb…/exec"

payload = {
  "action": "sendEmail",
  "params": {
    "to":     "someone@example.com",
    "subject":"בדיקה",
    "body":   "שלום! זה נשלח מהסוכן 🎉",
    "attachmentIds": []      # או ["1AbcDEF…"] אם תרצה לצרף קובץ מגוגל-דרייב
  }
}

res = requests.post(url, json=payload)
print(res.json())   # אמור להחזיר { "ok": true }
