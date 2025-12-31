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

## Lesson 3 - Learning (Password hashing)

- Use passlib.CryptContext to hash & verify passwords; prefer Argon2id (or bcrypt).
- Store only the hashed password (hash string contains algorithm, salt, params).
- Use pwd_context.hash() on register and pwd_context.verify() on login.
- Use pwd_context.needs_update() to detect old hashes and rehash on successful login.
- Install required libs: pip install "passlib[bcrypt]" or pip install "passlib[argon2]" + argon2-cffi.
- Consider a server-side pepper (secret in env/secret manager) for extra defense; handle rehashing & secrets carefully.
- Always use HTTPS, rate limiting, and secure password reset flows.

### Quick commands
- Install:
  - pip install "passlib[bcrypt]"
  - or pip install "passlib[argon2]" argon2-cffi
- Test hashing in REPL:
  ```python
  from passlib.context import CryptContext
  pwd = CryptContext(schemes=["argon2","bcrypt"], deprecated="auto")
  h = pwd.hash("secret")
  print(h, pwd.verify("secret", h), pwd.verify("wrong", h))
  ```

---

## Lesson 3 - Flashcards (Q = front, A = back)

1. Q: What do you store in the DB for a password?  
   A: Only the salted, slow hash string (contains algorithm, salt, params) — never plaintext.

2. Q: Which library is recommended for hashing in Python?  
   A: passlib (with Argon2 or bcrypt backends).

3. Q: How do you hash a password before saving?  
   A: Use pwd_context.hash(password) and save the returned string.

4. Q: How do you verify a login password?  
   A: Use pwd_context.verify(plain_password, stored_hash).

5. Q: What is pwd_context.needs_update(stored_hash) used for?  
   A: To detect hashes that use old params/algorithms so you can rehash and persist an updated hash after successful login.

6. Q: Do you need to manage salts manually?  
   A: No — modern schemes (Argon2/bcrypt) generate and store salts automatically in the hash string.

7. Q: What is a "pepper"?  
   A: An optional server-side secret combined with the password before hashing, stored outside the DB (env/secret manager) for extra security.

8. Q: What operational protections accompany password hashing?  
   A: Use HTTPS, account lockout/backoff, rate limiting, secure password reset, and secrets management for keys/peppers.

## Lesson 4 — JWT auth & per-user tasks
- Implemented JWT creation using `python-jose` (install with `uv add "python-jose[cryptography]"`).
- Login endpoint uses `OAuth2PasswordRequestForm` so Swagger "Authorize" works.
- `create_access_token({"sub": user.username})` issues signed token with `exp`.
- `get_current_user` dependency decodes token and loads user.Protected task endpoints by adding current_user: User = Depends(get_current_user) to create/list/get/update/delete.
- Tasks model updated with `owner_id` FK and relationship to User.
- Added owner relationship to Task (owner_id FK → users.id) and filter queries by `Task.owner_id == current_user.id` so users see only their own tasks.
- All task endpoints require authenticated user and filter by `current_user.id`.
- To apply owner_id in dev you can remove `dev.db` and restart (create_all will recreate tables), or use Alembic for migrations.
- Security notes: set a strong SECRET_KEY in env, use HTTPS, short token lifetimes, and consider refresh-token rotation/revocation.

### Quick commands
- Install jose (in venv): uv add "python-jose[cryptography]"
- Get a token via swagger: /docs → Authorize (enter username/password)  
- Or curl (form): curl -X POST -d "username=me" -d "password=secret" http://localhost:8000/auth/login
- Call protected endpoint: curl -H "Authorization: Bearer <token>" http://localhost:8000/tasks/

## Lesson 4 — JWT auth & per-user tasks (Q / A)

1. Q: Why issue JWTs after login?  
    A: To provide a stateless bearer token the client can send on subsequent requests.

2. Q: Which package implement JWT used here?  
    A: python-jose (install with uv add "python-jose[cryptography]").

3. Q: If you accidentally installed package named 'jose', what happens?  
    A: It can be the wrong old lib (Py2) and cause SyntaxError. Uninstall and install python-jose.

4. Q: What does create_access_token do?  
    A: Encodes payload (e.g., {"sub": username}) with exp claim into a signed JWT.

5. Q: How does get_current_user work?  
    A: Decodes JWT, checks signature & claims, grabs username from "sub", loads user from DB, or raises 401.

6. Q: How to make Swagger's Authorize work?  
    A: Use OAuth2PasswordRequestForm in /auth/login so Swagger can request token using form data.

7. Q: How to protect endpoints with JWT?  
    A: Add current_user: User = Depends(get_current_user) to route signature.

8. Q: Why were all tasks visible before adding owner_id?  
    A: Because tasks had no owner relation; authentication alone doesn't filter resources.

9. Q: How to make tasks per-user?  
    A: Add owner_id FK to Task and filter queries by Task.owner_id == current_user.id.

10. Q: What to do about DB schema change (owner_id) in dev?  
    A: For quick dev reset remove dev.db and restart; for production use Alembic migrations.

11. Q: What should you store in SECRET_KEY?  
    A: A strong random secret (not checked into source), stored in env or secret manager.

12. Q: How to call login from CLI so Swagger works too?  
    A: curl -X POST -d "username=me" -d "password=secret" http://localhost:8000/auth/login

13. Q: How to call protected endpoint with token?  
    A: curl -H "Authorization: Bearer <token>" http://localhost:8000/tasks/

14. Q: Storage advice for tokens in browser clients?  
    A: Prefer httpOnly secure cookies; localStorage is vulnerable to XSS.

15. Q: Should access tokens be long-lived?  
    A: No — keep access tokens short-lived and use refresh tokens with rotation if needed.

## Lesson 5 — 





# more flashcards
# Flashcards & Lesson Notes (expanded Q&A, Lessons 1–4)

Quick navigation
- Lesson 1 — Core app & DB
- Lesson 2 — Users & auth scaffold
- Lesson 3 — Password hashing
- Lesson 4 — JWT auth & per-user tasks
- Quick commands & troubleshooting

---

## Lesson 1 — Core app & DB (Q / A)

1. Q: Where are the interactive docs?  
   A: http://localhost:8000/docs (Swagger) and /redoc.

2. Q: What does SessionLocal = sessionmaker(...) give you?  
   A: A factory to create new SQLAlchemy Session objects.

3. Q: Why use get_db() as a dependency with yield?  
   A: One DB session per request and guaranteed cleanup (db.close()).

4. Q: Why set connect_args={"check_same_thread": False} for SQLite?  
   A: So SQLite works with threads used by Uvicorn in dev.

5. Q: What does Base = declarative_base() do?  
   A: Creates the base class for ORM models so SQLAlchemy can map classes to tables.

6. Q: What does Base.metadata.create_all(bind=engine) do?  
   A: Creates DB tables from models if missing (doesn't run migrations).

7. Q: Why use response_model in FastAPI routes?  
   A: Automatic validation/serialization and OpenAPI docs.

8. Q: How to implement pagination in a list endpoint?  
   A: Use query.offset(skip).limit(limit).all() and return metadata (total, skip, limit).

9. Q: How to check DB connectivity in an endpoint?  
   A: db.execute(text("SELECT 1")) wrapped in try/except.

10. Q: What CORS setting is unsafe for production?  
    A: allow_origins=["*"] combined with allow_credentials=True.

---

## Lesson 2 — Users & auth scaffold (Q / A)

11. Q: Why add helper functions like get_user_by_username()?  
    A: Keeps route logic thin and centralizes DB lookups for reuse/testing.

12. Q: Which Pydantic field type validates email?  
    A: EmailStr — requires the email-validator package.

13. Q: What happens if email-validator is missing?  
    A: ImportError: "email-validator is not installed". Install via pip install "pydantic[email]" or email-validator.

14. Q: Should you ever store plaintext passwords?  
    A: No — only for early lessons; always replace with hashing in real apps.

15. Q: How to test /auth/register from CLI?  
    A: curl -X POST -H "Content-Type: application/json" -d '{"email":"a@b.com","username":"me","password":"secret"}' http://localhost:8000/auth/register

16. Q: Why might Swagger's Authorize not work with JSON login?  
    A: Swagger expects the OAuth2 password grant (form data). Use OAuth2PasswordRequestForm to enable automatic token fetching.

---

## Lesson 3 — Password hashing (Q / A)

17. Q: What library is recommended for password hashing?  
    A: passlib (with bcrypt or argon2 backends).

18. Q: How to hash a password?  
    A: pwd_context.hash(password).

19. Q: How to verify a password?  
    A: pwd_context.verify(plain_password, stored_hash).

20. Q: What does pwd_context.needs_update(hash) do?  
    A: Detects if a stored hash uses old params/alg or needs rehashing.

21. Q: Is it OK to use multiple schemes like ["argon2","bcrypt"]?  
    A: Yes — new hashes use the first scheme; verification supports older hashes; use needs_update to migrate.

22. Q: How to verify hashing worked locally?  
    A: Create a user, inspect DB via sqlite3 to see hash string (starts with $argon2id$ or $2b$), then try login.

23. Q: Command to install passlib + bcrypt in venv?  
    A: pip install "passlib[bcrypt]"

24. Q: What is a "pepper"?  
    A: Optional server-side secret added before hashing; stored outside DB (env/secret manager).

---

## Lesson 4 — JWT auth & per-user tasks (Q / A)

25. Q: Why issue JWTs after login?  
    A: To provide a stateless bearer token the client can send on subsequent requests.

26. Q: Which package implement JWT used here?  
    A: python-jose (install with pip install "python-jose[cryptography]").

27. Q: If you accidentally installed package named 'jose', what happens?  
    A: It can be the wrong old lib (Py2) and cause SyntaxError. Uninstall and install python-jose.

28. Q: What does create_access_token do?  
    A: Encodes payload (e.g., {"sub": username}) with exp claim into a signed JWT.

29. Q: How does get_current_user work?  
    A: Decodes JWT, checks signature & claims, grabs username from "sub", loads user from DB, or raises 401.

30. Q: How to make Swagger's Authorize work?  
    A: Use OAuth2PasswordRequestForm in /auth/login so Swagger can request token using form data.

31. Q: How to protect endpoints with JWT?  
    A: Add current_user: User = Depends(get_current_user) to route signature.

32. Q: Why were all tasks visible before adding owner_id?  
    A: Because tasks had no owner relation; authentication alone doesn't filter resources.

33. Q: How to make tasks per-user?  
    A: Add owner_id FK to Task and filter queries by Task.owner_id == current_user.id.

34. Q: What to do about DB schema change (owner_id) in dev?  
    A: For quick dev reset remove dev.db and restart; for production use Alembic migrations.

35. Q: What should you store in SECRET_KEY?  
    A: A strong random secret (not checked into source), stored in env or secret manager.

36. Q: How to call login from CLI so Swagger works too?  
    A: curl -X POST -d "username=me" -d "password=secret" http://localhost:8000/auth/login

37. Q: How to call protected endpoint with token?  
    A: curl -H "Authorization: Bearer <token>" http://localhost:8000/tasks/

38. Q: Storage advice for tokens in browser clients?  
    A: Prefer httpOnly secure cookies; localStorage is vulnerable to XSS.

39. Q: Should access tokens be long-lived?  
    A: No — keep access tokens short-lived and use refresh tokens with rotation if needed.

---

## Quick troubleshooting (Q / A)

40. Q: Why get 405 Method Not Allowed on /auth/register in browser?  
    A: Route only accepts POST; visiting via browser issues GET.

41. Q: Why Pydantic raised "Config and model_config cannot be used together"?  
    A: Pydantic v2 disallows defining both class Config and model_config; keep model_config for v2.

42. Q: Why did EmailStr raise ImportError?  
    A: Missing email-validator package; install pydantic[email] or email-validator.

43. Q: Why was jwt import failing with SyntaxError?  
    A: Wrong 'jose' package installed; uninstall it and install python-jose[cryptography].

44. Q: How to inspect users/hashes in SQLite?  
    A: sqlite3 ./dev.db -header -column "SELECT id, username, hashed_password FROM users;"

45. Q: How to rehash on login?  
    A: After verify, if pwd_context.needs_update(stored_hash): new_hash = pwd_context.hash(plain); save new_hash to DB.

---

## Quick commands (copy-paste)

- Start server:
  uvicorn main:app --reload --host 0.0.0.0 --port 8000

- Register (JSON):
  curl -X POST -H "Content-Type: application/json" -d '{"email":"a@b.com","username":"me","password":"secret"}' http://localhost:8000/auth/register

- Login (form for Swagger):
  curl -X POST -d "username=me" -d "password=secret" http://localhost:8000/auth/login

- Call protected endpoint:
  curl -H "Authorization: Bearer <token>" http://localhost:8000/tasks/

- Inspect DB:
  sqlite3 ./dev.db -header -column "SELECT * FROM users;"

- Install libs (venv):
  pip install "passlib[bcrypt]" "python-jose[cryptography]" "pydantic[email]"

