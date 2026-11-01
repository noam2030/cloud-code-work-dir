Minimal FastAPI app with a simple UI

- Run locally:
  - python3 -m venv .venv && . .venv/bin/activate
  - pip install -r requirements.txt
  - uvicorn main:app --reload --host 0.0.0.0 --port 8080
- Visit http://localhost:8080/ to see a clean web UI.
- JSON API is still available at http://localhost:8080/api/hello

Deployment
- This repo includes a Dockerfile suitable for Cloud Run.
- GitHub Actions workflow .github/workflows/deploy.yml deploys on push to main using gcloud run deploy --source .
