Minimal FastAPI Hello World

- Run locally:
  - python3 -m venv .venv && source .venv/bin/activate
  - pip install -r requirements.txt
  - uvicorn main:app --reload --host 0.0.0.0 --port 8080
- Visit http://localhost:8080/ to see {"message": "Hello, world!"}

Deployment
- This repo includes a Dockerfile suitable for Cloud Run.
- GitHub Actions workflow .github/workflows/deploy.yml deploys on push to main using gcloud run deploy --source .
