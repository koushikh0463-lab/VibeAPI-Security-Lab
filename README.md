VibeAPI Professional Lab
========================
This is an intentionally vulnerable Flask API lab for testing your VibeGuard scanner.
LOCAL TESTING ONLY. It binds to 127.0.0.1 and must never be deployed publicly.

Run on Windows PowerShell:
1. Extract the ZIP.
2. Open PowerShell inside the VibeAPI_Professional_Lab folder.
3. Create a virtual environment:
   py -m venv .venv
4. Activate it:
   .\.venv\Scripts\Activate.ps1
5. Install the SAFE runtime requirements:
   python -m pip install -r requirements.txt
6. Start the application:
   python app.py
7. Open:
   http://127.0.0.1:5003

Dashboard:
- http://127.0.0.1:5003/

API routes:
- GET /api/users
- GET /api/users/1
- GET /api/users/2
- GET /api/debug/config
- GET /api/crash

Intentional scanner findings:
- VA-01 Hardcoded fake secrets in config.py
- VA-02 Sensitive data exposure from /api/users and /api/users/<id>
- VA-03 Debug/configuration and stack trace exposure
- VA-04 Outdated package versions in requirements-vulnerable.txt

IMPORTANT:
- requirements-vulnerable.txt is included for dependency-scanner testing only.
- DO NOT install requirements-vulnerable.txt.
- All accounts, tokens and personal-looking values are fake test data.
- Keep this application on localhost. Do not expose it to a LAN or public internet.
