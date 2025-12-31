Below is a concise step‑by‑step teaching plan (hands‑on, incremental) to build the single‑file FastAPI app in main.py, starting from the minimal todo core and adding features one lesson at a time.

High‑level approach
- Start minimal and ship working code each step.
- Each lesson: goal, deliverable, commands, test checklist.
- Use SQLite file (sqlite:///./dev.db) and uv for dependency management / running.

Recommended dependencies (uv)
- uv add fastapi uvicorn sqlalchemy pydantic python-jose passlib[bcrypt] python-multipart
- uv add --dev pytest httpx pytest-asyncio

Teaching plan (lessons)

1) Lesson 1 — Project bootstrap & minimal todo core (45–75m)
- Goal: single main.py with SQLite, DB init, Task model, CRUD endpoints (no auth).
- Deliverable: main.py with models, Pydantic schemas, create/list/get/update/delete task endpoints, /docs visible.
- Commands:
  - uv init (if you want)
  - uv add ...
  - uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
- Tests: manual via /docs and one pytest test for create + get + delete.
- Checkpoints: DB file created, /tasks endpoints work.

2) Lesson 2 — User model + basic registration/login scaffold (90m)
- Goal: add User model and register endpoint; login endpoint returns placeholder token (no security).
- Deliverable: /auth/register and /auth/login endpoints, users stored in DB.
- Tests: register user, ensure user uniqueness checks.

3) Lesson 3 — Password hashing (bcrypt) and secure storage (45m)
- Goal: integrate passlib bcrypt hashing; store hashed_password, never return password in responses.
- Deliverable: hashed password on register, verify hashing on tests.
- Tests: attempt login comparing raw password fails if hashing not used; then succeeds when verifying.

4) Lesson 4 — JWT auth (30m–60m)
- Goal: implement JWT tokens (30 min expiry), OAuth2PasswordBearer dependency, create_access_token.
- Deliverable: /auth/login returns JWT, /auth/me protected endpoint using get_current_user.
- Tests: obtain token and call /auth/me.

5) Lesson 5 — Protect task endpoints & ownership (60m)
- Goal: require auth for /tasks endpoints; tasks owned by user; enforce ownership in read/update/delete.
- Deliverable: tasks require Authorization: Bearer <token>, user-only views.
- Tests: two users cannot access each other’s tasks.

6) Lesson 6 — Validation, enums, timestamps, complete endpoint, status updates (45m)
- Goal: add Status/Priority enums, created_at/updated_at, /tasks/{id}/complete; validate input lengths.
- Deliverable: full Task schema and business logic.
- Tests: status transitions and is_completed behavior.

7) Lesson 7 — Pagination & filtering (30m)
- Goal: add skip/limit, status_filter query param, total/page metadata.
- Deliverable: /tasks/?skip=0&limit=10&status_filter=completed
- Tests: verify total & page_size fields.

8) Lesson 8 — Error handling, health checks, CORS (30m)
- Goal: consistent HTTPException responses, /health that checks DB, CORS middleware for local dev.
- Deliverable: robust error messages, healthy probe.

9) Lesson 9 — Unit/integration tests (2–3h)
- Goal: write pytest + httpx async tests for all critical flows (register/login/create/read/update/delete, auth failures).
- Deliverable: tests/test_api.py passing locally.
- Commands: uv run pytest

10) Lesson 10 — Dev packaging: Dockerfile + docker-compose (1–2h)
- Goal: produce small multi-stage Dockerfile and compose for local dev (persisted sqlite volume).
- Deliverable: Dockerfile and docker-compose.yml (we’ll do this after app is stable).

11) Lesson 11 — Observability & CI basics (1–2h)
- Goal: add structured logging, simple health metrics, and a GitHub Actions workflow to run tests and build image.
- Deliverable: minimal workflow .github/workflows/ci.yml.

12) Lesson 12+ — Kubernetes, Terraform, rollout strategies (later)
- Goal: manifests, Helm/terraform infra, rollout/monitoring. (Do after Docker/CI working.)

How we’ll work together (recommended cadence)
- I’ll generate the main.py for each lesson (or patch on your file) with clear comment sections.
- You run it locally with uv run uvicorn main:app --reload, test, and report issues.
- I’ll iterate quickly on fixes/tests and then move to next lesson.

