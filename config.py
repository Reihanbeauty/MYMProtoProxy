import os

# Port to listen on
PORT = int(os.environ.get("PORT", 443))

# User secrets (32 hex characters)
USERS = {
    "tg": "e9630df34ae5fb7361e5b04ccc9d6f43",
}

MODES = {
    # Classic mode (dd-secret disabled)
    "classic": False,

    # Secure mode (dd-secret) - REQUIRED for AD_TAG to display
    "secure": True,

    # TLS mode (ee-secret) - Telegram disables AD_TAG in Fake TLS mode
    "tls": False
}

# Domain for TLS mode (Ignored when tls is False)
TLS_DOMAIN = "www.google.com"

# Tag for advertising, obtainable from @MTProxybot
# Reads from Railway variables if available, otherwise uses fallback value
AD_TAG = os.environ.get("AD_TAG", "84b48fa37d379ad01cd3abaee33b05ba")
