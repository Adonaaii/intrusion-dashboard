# Intrusion Dashboard

An early Flask prototype that tails a sample web access log and displays HTTP 401 responses as failed-login alerts. See [SentinelSOC](https://github.com/Adonaaii/larbiSOC) for the follow-on alert triage project.

## Run locally

With Python 3.12, from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
flask --app app run
```

Open `http://127.0.0.1:5000`. The [monitor](core/monitor.py) watches `data/logs/sample.log` for new entries.
