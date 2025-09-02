import httpx

SENDGRID_API_KEY = "your-sendgrid-api-key"
SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"
TWILIO_ACCOUNT_SID = "your-account-sid"
TWILIO_AUTH_TOKEN = "your-auth-token"
TWILIO_FROM_NUMBER = "+254111395016"


async def send_sms_async(to_number: str, message: str):
    url = (
        f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_ACCOUNT_SID}/Messages.json"
    )
    data = {"From": TWILIO_FROM_NUMBER, "To": to_number, "Body": message}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url, data=data, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        )
        return response.status_code


async def send_email_async(to_email: str, subject: str, content: str):
    headers = {
        "Authorization": f"Bearer {SENDGRID_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "personalizations": [{"to": [{"email": to_email}], "subject": subject}],
        "from": {"email": "noreply@prodpulse.io"},
        "content": [{"type": "text/plain", "value": content}],
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(SENDGRID_URL, json=payload, headers=headers)
        return response.status_code


async def send_slack_alert(message: str):
    webhook_url = "https://hooks.slack.com/services/your/webhook/url"
    async with httpx.AsyncClient() as client:
        await client.post(webhook_url, json={"text": message})
