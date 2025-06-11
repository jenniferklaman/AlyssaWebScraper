def check_for_alerts(cleaned_data_list):
    today = get_today_date()
    for row in cleaned_data_list:
        if row['Quote Due Date'] == today:
            send_alert_email(row)

def send_alert_email(row):
    # Use smtplib to send email with subject:
    # "Reminder: Quote Due Today for [Account Name]"
    # Include broker, premium, and notes in body
