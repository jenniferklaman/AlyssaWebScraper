from datetime import date

def check_for_alerts(cleaned_data_list):
    today = str(date.today())
    for row in cleaned_data_list:
        if row.get("Quote Due Date") == today:
            send_alert_email(row)

def send_alert_email(row):
 # Placeholder for sending emails (use smtplib or Slack webhook)
# Use smtplib to send email with subject:
# "Reminder: Quote Due Today for [Account Name]"
# Include broker, premium, and notes in body
    print(f"ALERT: Quote due today for {row['Account Name']}")
