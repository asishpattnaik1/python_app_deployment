
#import  & config
from typing import List, Optional
from fastapi import FastAPI,HTTPException,Depends, status
from pydantic import BaseModel, constr, Field, EmailStr  # <-- added EmailStr
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text, text
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime  import datetime
import os
from dotenv import load_dotenv, find_dotenv

#load .env file if present
env_path = find_dotenv() or ".env"
load_dotenv(env_path)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
print("Using DATABASE_URL:", DATABASE_URL)
#Database setup
# For sqlite disable same thread check for multithreading
engine= create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},  # <-- use lowercase key
    echo=False # To see the generated SQL queries
)

#what this will do is create a session factory that will generate new Session objects when called.
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)
# what this will do is create a base class for our ORM models to inherit from.
#can you explain declarative_base in sqlalchemy
#Declarative_base is a factory function in SQLAlchemy that creates a base class for your ORM models to inherit from when using the declarative system.
# It provides a way to define database tables and their mappings to Python classes in a clear and concise manner.
# When you create a base class using declarative_base(), you can then define your ORM models as subclasses of this base class.
# This allows SQLAlchemy to automatically generate the necessary database schema and handle the mapping between your Python classes and database tables.
# By using declarative_base, you can easily create and manage your database models while keeping your code organized and maintainable.
# In summary, declarative_base is a key component of SQLAlchemy's ORM that simplifies the process of defining and working with database models in Python.
# what is ORM
#ORM stands for Object-Relational Mapping. It is a programming technique that allows developers to interact with relational databases using object-oriented programming concepts.
#ORM provides a way to map database tables to classes in a programming language, allowing developers to work with database records as if they were regular objects in their code.
#With ORM, developers can perform database operations such as querying, inserting, updating, and deleting records using familiar object-oriented syntax, rather than writing raw SQL queries.
#ORM frameworks handle the translation between the object-oriented code and the underlying database structure, making it easier to work with databases and reducing the amount of boilerplate code needed for database interactions.
#Some popular ORM frameworks include SQLAlchemy for Python, Hibernate for Java, and Entity Framework for .NET.
#Overall, ORM simplifies database interactions and improves developer productivity by providing a more intuitive way to work with relational data.
# what if my database is in ADLS
#If your database is in Azure Data Lake Storage (ADLS), you can still use ORM frameworks to interact with the data, but the approach may vary depending on the specific ORM and the way you access ADLS.
#ADLS is primarily designed for storing large amounts of unstructured data, so you may need to use additional tools or libraries to read and write data from ADLS before using an ORM.
#One common approach is to use a data processing framework like Apache Spark or Azure Data Factory to read data from ADLS and then use an ORM to interact with the processed data.
#is this standard practice for relational databases using ORM
#Yes, using ORM (Object-Relational Mapping) is a standard practice for interacting with relational databases in many programming languages, including Python, Java, and .NET.
#ORM frameworks provide a convenient way to map database tables to classes in the programming language, allowing developers to work with database records as if they were regular objects in their code.
#This approach simplifies database interactions, reduces boilerplate code, and improves developer productivity.
#Popular ORM frameworks like SQLAlchemy for Python, Hibernate for Java, and Entity Framework for .NET are widely used in the industry for building applications that interact with relational databases.
#However, it's important to note that while ORM is a standard practice, it may not be suitable for all use cases.
#In some scenarios, such as complex queries or performance-critical applications, developers may choose to write raw SQL queries or use a combination of ORM and direct SQL to achieve the desired results.
#Overall, ORM is a widely accepted and standard practice for working with relational databases, but the choice of whether to use it or not depends on the specific requirements of the application.
# what about databricks sql tables
#Databricks SQL tables can be accessed using various methods, including JDBC/ODBC connections
# or using the Databricks REST API. However, using ORM frameworks directly with Databricks SQL tables may not be as straightforward as with traditional relational databases.
#Databricks is primarily designed for big data processing and analytics, and it may not support all the features and capabilities of traditional relational databases.
#If you want to use ORM with Databricks SQL tables, you may need to use a combination of tools and libraries.
#One approach is to use a data processing framework like Apache Spark to read data from Databricks SQL tables and then use an ORM to interact with the processed data.
#Alternatively, you can use JDBC/ODBC connections to connect to Databricks SQL tables and execute SQL queries directly, without using an ORM.
# if we use ORM with sqlalchemy does that mean we dont have to create those tables in the database
#When using ORM with SQLAlchemy, you typically define your database tables as Python classes that inherit from a base class created using declarative_base().
#SQLAlchemy will then use these class definitions to automatically generate the necessary database schema and create the tables in the database when you call the create_all() method on the metadata of the base class.
#However, it's important to note that while SQLAlchemy can create the tables for you based on your class definitions, you still need to ensure that the database itself exists and is accessible.
#In other words, SQLAlchemy can handle the creation of tables within an existing database, but it cannot create the database itself.
#Additionally, if you have existing tables in the database that you want to work with using ORM, you will need to define the corresponding Python classes that match the structure of those tables.
#Overall, using ORM with SQLAlchemy can simplify the process of creating and managing database tables, but you still need to ensure that the database is set up and accessible.


Base= declarative_base()

# -------------------------
# User ORM model (Lesson 2)
# -------------------------
class User(Base):
    __tablename__ ="users"
    id= Column(Integer, primary_key=True, index=True)
    email= Column(String(320), unique=True, index=True, nullable=False)
    username= Column(String(150), unique=True, index=True, nullable=False)
    hashed_password= Column(String(255), nullable=False) # will store raw password for Lesson 2 (we'll add hashing next lesson)
    is_active= Column(Boolean, default=True, nullable=False)
    created_at= Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at= Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

# -------------------------
# Helper DB functions
# -------------------------
def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter((User.username== username)).first()

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter((User.email== email)).first()
####################################################################

#Database Models
class Task(Base):
    __tablename__ = "tasks"
    id= Column(Integer, primary_key=True, index=True)
    title= Column(String(100), nullable=False)
    description= Column(Text, nullable=True)
    is_completed= Column(Boolean, default=False, nullable=False)
    due_date= Column(DateTime, nullable=True)
    created_at= Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at= Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

####################################################################
#pydantic schemas for Task
# what are pydantic schemas
#Pydantic schemas are data models defined using the Pydantic library in Python.
#Pydantic is a data validation and settings management library that uses Python type annotations to define data structures.
#Pydantic schemas allow you to define the shape and structure of your data, including the types of each field, default values, and validation rules.
#When you define a Pydantic schema, you create a class that inherits from pydantic.BaseModel.
#Each attribute of the class represents a field in the schema, and you can use type hints to specify the expected data type for each field.
#Pydantic schemas are commonly used in web frameworks like FastAPI to define request and response models for API endpoints.
#They help ensure that the data being sent and received conforms to the expected structure, making it easier to validate and process the data.
#Overall, Pydantic schemas provide a powerful way to define and validate data structures in Python applications.
####################################################################
class TaskCreate(BaseModel):
    title: constr(min_length=1, max_length=200)
    description: Optional[constr(max_length=1000)] = None
    due_date: Optional[datetime] = None

class TaskUpdate(BaseModel):
    title: Optional[constr(min_length=1, max_length=200)] = None
    description: Optional[constr(max_length=1000)] = None
    is_completed: Optional[bool] = None
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_completed: bool
    due_date: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

     # Pydantic v2: allow creating model from ORM objects / attributes
    model_config = {"from_attributes": True}

class TaskListResponse(BaseModel):
    tasks: List[TaskResponse]
    total: int
    skip: int
    limit: int

# -------------------------
# Pydantic schemas (User)
# -------------------------

class UserCreate(BaseModel):
    email: EmailStr
    username: constr(min_length=3, max_length=50)
    password: constr(min_length=6, max_length=128)

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_active: bool
    created_at: datetime

    # Pydantic v2: allow creating model from ORM objects / attributes
    model_config = {"from_attributes": True}

class UserLogin(BaseModel):
    username: str
    password: str

class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


####################################################################
#dependency to get DB session
# this function is a dependency that provides a database session for each request. One session per request: you avoid sharing a single Session across requests (prevents data corruption and concurrency bugs).
# Proper cleanup: db.close() always runs, preventing connection/session leaks.
# Thread-safety: each request gets its own Session instance; combined with SQLite connect_args or other DB drivers this avoids threading issues.
# Simpler error handling: the session is closed even if the handler raises an exception.
# Testability: you can override this dependency in tests to inject a test DB/session.
# Works with FastAPI lifecycle: using yield in dependency acts like a setup/teardown (similar to context manager).
####################################################################
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


####################################################################
#FastAPI app and middlewares
######################################################################
app = FastAPI(title='ToDO API with FastAPI and SQLAlchemy', version='1.0.0')

##################################################################
#allow all origins for simplicity
# In production, restrict this to specific origins for security

#what does CORS middleware do
#CORS (Cross-Origin Resource Sharing) middleware is a component that helps manage and control cross-origin requests in web applications.
#When a web application makes a request to a different domain (origin) than the one it was served from, the browser enforces the same-origin policy, which restricts such requests for security reasons.
#CORS middleware allows you to specify which origins are allowed to access your resources, what HTTP methods are permitted, and which headers can be included in the requests.
#By configuring CORS middleware, you can enable or restrict cross-origin requests based on your application's requirements.
#This is particularly important for APIs that are intended to be accessed from web applications hosted on different domains.
#Overall, CORS middleware is essential for ensuring secure and controlled access to web resources across different origins.
"""What it does (concise)

Enables CORS handling for incoming requests so the server sends the appropriate Access-Control-* response headers.
Lets browsers perform cross-origin calls (XHR / fetch / AJAX) to your API and handles preflight OPTIONS requests automatically.
Meaning of each option

allow_origins=["*"] — allow requests from any origin (sends Access-Control-Allow-Origin: *).
allow_credentials=True — allow sending cookies or Authorization credentials (adds Access-Control-Allow-Credentials: true).
allow_methods=["*"] — allow all HTTP methods (GET, POST, PUT, DELETE, OPTIONS, etc.).
allow_headers=["*"] — allow all request headers (Authorization, Content-Type, custom headers, etc.).
Important security notes

Browsers enforce CORS; server-side clients (curl, Postman, backend services) are unaffected.
Do NOT use allow_origins=["*"] together with allow_credentials=True in production: browsers will reject the response or the server must echo a specific origin instead of *. Allowing any origin + credentials is unsafe.
Allowing all origins/methods/headers is convenient for dev but increases attack surface in production.
Recommendations for production

Restrict allow_origins to a whitelist of trusted front-end URLs (e.g., ["https://app.example.com"]).
Keep allow_credentials=True only if you need cookies or browser-sent credentials; ensure origin is explicit.
Limit allow_methods and allow_headers to the minimal set your front end needs.
Optionally set allow_origin_regex or implement a dynamic origin function for multi-env setups.
Consider setting max_age and expose_headers if needed.
How to verify CORS is working

From the browser, open DevTools → Network and inspect the OPTIONS (preflight) and actual request/response headers for Access-Control-Allow-*.
Using curl you won't see CORS enforcement because it’s a browser policy (but you can inspect the response headers returned by the server).
"""
####################################################################
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#################################################################
#stratup: create tables
# what does it do on startup
#The on_startup function is an event handler that runs when the FastAPI application starts up.
#In this case, it calls Base.metadata.create_all(bind=engine) to create all the database tables defined in the ORM models if they do not already exist.
#This ensures that the necessary database schema is set up and ready for use when the application starts. if the tables already exist, this operation will have no effect.
#################################################################
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

###################################################################
#Root and health check endpoints
###################################################################
@app.get("/", summary="Welcome Endpoint")
def root():
    return {"message": "Welcome to the ToDO API built with FastAPI and SQLAlchemy!"}

@app.get("/health", summary="Health Check Endpoint")
def health_check(db: Session = Depends(get_db)):
    # Simple DB query to ensure connectivity
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database connection error")


####################################################################
# Auth endpoints (Lesson 2)
# - /auth/register : create a new user (no hashing yet)
# - /auth/login    : validate credentials and return a placeholder token
####################################################################
# Register new user
@app.post("/auth/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED, summary="Register a new user")
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    # Check if username or email already exists
    if get_user_by_username(db, user_in.username):
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    if get_user_by_email(db, user_in.email):
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    # Create new user (storing raw password for Lesson 2)
    user = User(
        email= user_in.email,
        username= user_in.username,
        hashed_password= user_in.password  # In Lesson 3, we'll hash this password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Login user
@app.post("/auth/login", response_model= UserLoginResponse,summary="Login and obtain access token")
def login_user(user_in: UserLogin, db: Session = Depends(get_db)):
    user= get_user_by_username(db, user_in.username)
    if not user or user.hashed_password != user_in.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    # Return a placeholder token (in Lesson 3, we'll implement JWT)
    return {"access_token":"fake-jwt-token-for-" + user.username, "token_type": "bearer"}


####################################################################
#Task CRUD Endpoints
#####################################################################
# Create Task
@app.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED, summary="Create a new task")
def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    task = Task(
        title= task_in.title,
        description= task_in.description,
        due_date= task_in.due_date
    )

    db.add(task)
    db.commit()
    db.refresh(task)
    return task

#get list of tasks
@app.get("/tasks/",response_model=TaskListResponse, summary="Get a list of tasks")
def get_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    q = db.query(Task)
    total = q.count()
    tasks = q.order_by(Task.created_at.desc()).offset(skip).limit(limit).all()

    return TaskListResponse(tasks=tasks, total=total, skip=skip, limit=limit)

#get task by id
@app.get("/tasks/{task_id}", response_model=TaskResponse, summary="Get a task by ID")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task= db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

#update a task
@app.post("/tasks/{task_id}", response_model=TaskResponse, summary="Update a task by ID")
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    task= db.query(Task).filter(Task.id ==task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found") 
    for var, value in vars(task_update).items():
        if value is not None:
            setattr(task, var, value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

#delete a task
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a task by ID")
def delete_task(task_id : int, db: Session = Depends(get_db)):
    task= db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db.delete(task)
    db.commit()
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

