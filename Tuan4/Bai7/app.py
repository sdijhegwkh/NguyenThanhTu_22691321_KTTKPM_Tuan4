import os

app_env = os.getenv("APP_ENV", "undefined")

print(f"App is running in {app_env} mode")