from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from apscheduler.schedulers.background import BackgroundScheduler
import uvicorn
import webbrowser
from token_utils import get_authorization_url, exchange_code_for_tokens, refresh_tokens

app = FastAPI()

@app.get("/")
def root():
    url = get_authorization_url()
    return RedirectResponse(url)

@app.get("/callback")
def callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        return {"error": "Authorization code not found."}
    tokens = exchange_code_for_tokens(code)
    return {
        "message": "Authorization successful.",
        "access_token": tokens["access_token"]
    }

def start_token_refresher():
    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh_tokens, "interval", minutes=30)
    scheduler.start()
    print("🔁 Token refresh job started (every 30 min).")

if __name__ == "__main__":
    import threading
    import time

    def open_browser():
        time.sleep(1)
        webbrowser.open("http://localhost:8000")

    threading.Thread(target=open_browser).start()
    start_token_refresher()
    uvicorn.run(app, host="0.0.0.0", port=8000)
