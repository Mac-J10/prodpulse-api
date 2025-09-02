import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def get_monthly_usage():
    usages = stripe.UsageRecordSummary.list(limit=100)
    return usages.data
