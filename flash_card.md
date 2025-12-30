# Lesson Notes & Flashcards

## Lesson 1 - Learning (minimal TODO core)
- Single-file FastAPI app: main.py
- SQLite file DB: sqlite:///./dev.db (configurable via .env)
- SQLAlchemy basics: engine, SessionLocal (sessionmaker), declarative_base(), ORM models
- One-session-per-request pattern using a dependency with yield + finally db.close()
- Pydantic v2 models:
  - Separate models for create/update/response
  - Use `model_config = {"from_attributes": True}` to accept ORM objects
- CRUD endpoints for Task: create, list (pagination), get by id, update, delete
- Health endpoint uses `db.execute(text("SELECT 1"))`
- CORS middleware for dev; tighten in production
- Common runtime fixes encountered: sqlite connect_args, sqlalchemy.text, query ordering, Pydantic config issues

---

## Lesson 1 - Flashcards

1. Q: Where are FastAPI interactive docs?  
   A: http://localhost:8000/docs (Swagger) and http://localhost:8000/redoc

2. Q: What does `SessionLocal = sessionmaker(...)` provide?  
   A: A factory to create new SQLAlchemy Session instances.

3. Q: Why use a `get_db()` dependency with `yield`?  
   A: Provides one session per request and ensures `db.close()` runs for cleanup.

4. Q: Why `connect_args={"check_same_thread": False}` for SQLite?  
   A: Allows SQLite connections to be shared across threads in dev servers.

5. Q: What is `declarative_base()`?  
   A: Factory that creates a base class for ORM models to map Python classes to DB tables.

6. Q: What does `Base.metadata.create_all(bind=engine)` do on startup?  
   A: Creates missing tables based on ORM models (doesn't create the database).

7. Q: Why separate Pydantic models for Create / Update / Response?  
   A: Enforce different validation rules and avoid exposing internal fields.

8. Q: In Pydantic v2 how to accept ORM objects?  
   A: Add `model_config = {"from_attributes": True}` on the response model.

9. Q: What's a common Pydantic v2 pitfall?  
   A: Don't use both `class Config` and `model_config` on the same model.

10. Q: Why call `db.commit()` and then `db.refresh(obj)`?  
    A: `commit()` persists the transaction; `refresh()` loads DB-generated fields (id, timestamps).

11. Q: How to implement simple pagination?  
    A: Use `query.offset(skip).limit(limit).all()` and return total/skip/limit metadata.

12. Q: What does CORS middleware enable?  
    A: Browser cross-origin requests by setting Access-Control-* headers and handling preflight.

13. Q: Security note about `allow_origins=["*"]` + `allow_credentials=True`?  
    A: Unsafe in production — use explicit origin whitelist when credentials are allowed.

14. Q: How to test DB connectivity in code?
    A: db.execute(text("SELECT 1")) inside a try/except to confirm DB reachable.

15. Q: Why return Pydantic models (response_model) instead of raw dicts?
    A: Automatic validation & serialization, consistent API contract, and generated OpenAPI docs.

---

## Artifacts (where things live)
- App: `main.py` (project root)
- DB: `./dev.db` (created after first run)
- Notes & flashcards: `lesson_notes.md` (this file)

---

## Next steps
- Lesson 2: Add User model + `/auth/register` and `/auth/login` (no hashing) — say "start lesson 2" to proceed.
- I will append new lesson sections and related flashcards to this file as we progress.

## Lesson 2 - Learning (User auth scaffold)

- Added a simple User ORM model (SQLAlchemy) with fields:
  - id, email, username, hashed_password (temporary raw), is_active, timestamps.
- Added helper DB functions:
  - get_user_by_username(db, username)
  - get_user_by_email(db, email)
- Added Pydantic schemas:
  - UserCreate (email, username, password)
  - UserResponse (id, email, username, is_active, created_at) — uses Pydantic v2 model_config={"from_attributes": True}
  - UserLogin (username, password)
  - UserLoginResponse (access_token, token_type)
- Endpoints (no hashing / no JWT yet):
  - POST /auth/register — registers user, checks uniqueness, stores password as-is (Lesson 3 will add hashing)
  - POST /auth/login — verifies credentials and returns a placeholder token
- Notes:
  - Keep `.env` and DATABASE_URL correctly configured.
  - Next lesson: replace raw password storage with passlib bcrypt and implement JWT tokens; then protect /tasks endpoints by current_user dependency.

---

## Lesson 2 - Flashcards (Q = front, A = back)

1. Q: What new ORM model was added in Lesson 2?  
   A: User model with id, email, username, hashed_password (temporary), is_active, created_at/updated_at.

2. Q: Why have helper functions get_user_by_username / get_user_by_email?  
   A: Encapsulate common DB lookups and keep route logic simple and testable.

3. Q: What Pydantic schema validates registration input?  
   A: UserCreate (EmailStr, username constr, password constr).

4. Q: Why does UserResponse need model_config = {"from_attributes": True}?  
   A: Pydantic v2 requires it to convert SQLAlchemy ORM objects (attribute access) into response models.

5. Q: What does POST /auth/register do today?  
   A: Validates uniqueness, creates a User record, and returns the user object (password stored raw for now).

6. Q: What does POST /auth/login return today?  
   A: A placeholder access token string (no real JWT yet).

7. Q: What must be changed next for security?  
   A: Hash passwords with bcrypt (passlib) and implement JWT tokens; do not store raw passwords.

---

## Quick test snippets

- Register:
  curl -X POST "http://localhost:8000/auth/register" -H "Content-Type: application/json" -d '{"email":"a@b.com","username":"me","password":"secret"}'

- Login:
  curl -X POST "http://localhost:8000/auth/login" -H "Content-Type: application/json" -d '{"username":"me","password":"secret"}'

---

## Next action
- Proceed to Lesson 3: add password hashing (passlib) and verify login with hashed passwords. Say "start lesson 3" to continue.
