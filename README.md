# Python FastAPI Application - Complete DevOps Learning Project

---

## 📋 APPLICATION REQUIREMENTS DOCUMENT

### **What Are We Building?**
A **Task Management API** - A backend REST API that allows users to manage their personal tasks/to-dos.

---

## 🎯 **BUSINESS REQUIREMENTS**

### **Core Features**
1. **User Management**
   - Users can register with email, username, and password
   - Users can login and receive a secure token (JWT)
   - Only authenticated users can access their tasks
   - Users can only see and manage their own tasks

2. **Task Management**
   - Users can create tasks with:
     - Title (required)
     - Description (optional)
     - Priority (low, medium, high, urgent)
     - Due date (optional)
   - Users can view all their tasks
   - Users can view a specific task
   - Users can update task details
   - Users can mark tasks as completed
   - Users can delete tasks
   - Tasks have automatic timestamps (created_at, updated_at)

3. **Task Filtering**
   - Filter tasks by status (pending, in_progress, completed, cancelled)
   - Pagination support for task lists

---

## 🏗️ **TECHNICAL REQUIREMENTS**

### **1. Database Design**

**Two Main Entities:**

#### **User Entity**
```
User
├── id (Primary Key, Auto-increment)
├── email (Unique, Required)
├── username (Unique, Required)
├── hashed_password (Required, Never exposed in API)
├── is_active (Boolean, Default: True)
├── is_superuser (Boolean, Default: False)
├── created_at (DateTime, Auto-generated)
└── updated_at (DateTime, Auto-updated)
```

**Why these fields?**
- `id`: Unique identifier for each user
- `email`: For password recovery (future feature)
- `username`: For login
- `hashed_password`: Security - never store plain passwords
- `is_active`: Soft delete / account suspension capability
- `is_superuser`: Admin features (future)
- `created_at/updated_at`: Audit trail

#### **Task Entity**
```
Task
├── id (Primary Key, Auto-increment)
├── title (Required)
├── description (Optional)
├── status (Enum: pending, in_progress, completed, cancelled)
├── priority (Enum: low, medium, high, urgent)
├── is_completed (Boolean, Default: False)
├── due_date (DateTime, Optional)
├── created_at (DateTime, Auto-generated)
├── updated_at (DateTime, Auto-updated)
└── owner_id (Foreign Key → User.id, Required)
```

**Why these fields?**
- `id`: Unique identifier for each task
- `title`: What the task is about
- `description`: Detailed information
- `status`: Track task lifecycle
- `priority`: Help users prioritize
- `is_completed`: Quick check for completion
- `due_date`: Deadline tracking
- `owner_id`: Link task to user (One-to-Many relationship)

**Relationship:**
- One User can have Many Tasks
- Each Task belongs to One User
- Cascading delete: If user is deleted, all their tasks are deleted

---

### **2. API Endpoints Design**

#### **Authentication Endpoints** (`/auth`)
```
POST   /auth/register      # Register new user
POST   /auth/login         # Login and get JWT token
GET    /auth/me            # Get current user info (requires auth)
```

#### **Task Endpoints** (`/tasks`)
```
POST   /tasks/                    # Create new task (requires auth)
GET    /tasks/                    # Get all user's tasks (requires auth, supports pagination)
GET    /tasks/{task_id}           # Get specific task (requires auth)
PUT    /tasks/{task_id}           # Update task (requires auth)
DELETE /tasks/{task_id}           # Delete task (requires auth)
POST   /tasks/{task_id}/complete  # Mark task as completed (requires auth)
```

#### **System Endpoints**
```
GET    /                   # Welcome message
GET    /health             # Health check (for K8s probes)
GET    /docs               # Auto-generated API documentation
```

---

### **3. Security Requirements**

1. **Password Security**
   - Passwords must be hashed using bcrypt (never stored as plain text)
   - Minimum password length: 6 characters

2. **Authentication**
   - JWT (JSON Web Tokens) for stateless authentication
   - Token expires after 30 minutes
   - Token includes username in payload

3. **Authorization**
   - Users can only access their own tasks
   - All task endpoints require authentication
   - Public endpoints: register, login, health check

4. **Data Validation**
   - Email must be valid format
   - Username: 3-50 characters
   - Task title: 1-200 characters
   - Task description: max 1000 characters

---

### **4. Request/Response Examples**

#### **Register User**
```json
Request: POST /auth/register
{
  "email": "john@example.com",
  "username": "john_doe",
  "password": "secure123"
}

Response: 201 Created
{
  "id": 1,
  "email": "john@example.com",
  "username": "john_doe",
  "is_active": true,
  "created_at": "2025-10-30T10:30:00"
}
```

#### **Login**
```json
Request: POST /auth/login
{
  "username": "john_doe",
  "password": "secure123"
}

Response: 200 OK
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

#### **Create Task**
```json
Request: POST /tasks/
Headers: Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
{
  "title": "Complete Python project",
  "description": "Build a FastAPI task management API",
  "priority": "high",
  "due_date": "2025-11-15T23:59:59"
}

Response: 201 Created
{
  "id": 1,
  "title": "Complete Python project",
  "description": "Build a FastAPI task management API",
  "status": "pending",
  "priority": "high",
  "is_completed": false,
  "due_date": "2025-11-15T23:59:59",
  "created_at": "2025-10-30T10:45:00",
  "updated_at": "2025-10-30T10:45:00",
  "owner_id": 1
}
```

#### **Get All Tasks**
```json
Request: GET /tasks/?skip=0&limit=10&status_filter=pending
Headers: Authorization: Bearer eyJhbGciOiJIUzI1NiIs...

Response: 200 OK
{
  "tasks": [
    {
      "id": 1,
      "title": "Complete Python project",
      "status": "pending",
      ...
    }
  ],
  "total": 15,
  "page": 1,
  "page_size": 10
}
```

---

## 🧩 **APPLICATION COMPONENTS & OOP DESIGN**

### **Why We Need Multiple Layers?**
We follow the **Service Layer Architecture** (also called Clean Architecture):
- Separates concerns
- Makes code testable
- Easier to maintain and extend
- Industry best practice

### **Component Breakdown**

#### **1. Models Layer** (`app/models/`)
**Purpose:** Database representation (ORM - Object-Relational Mapping)

**Files:**
- `user.py` - User database model
- `task.py` - Task database model

**OOP Concepts:**
- Classes represent database tables
- Attributes represent columns
- Methods for object behavior (e.g., `mark_completed()`)
- Relationships between objects (User → Tasks)

**Why?**
- Abstraction: Work with Python objects instead of SQL
- Encapsulation: Data and methods together
- Type safety: Python knows the data types

---

#### **2. Schemas Layer** (`app/schemas/`)
**Purpose:** Data validation and API request/response models

**Files:**
- `user.py` - User request/response schemas
- `task.py` - Task request/response schemas

**OOP Concepts:**
- Inheritance (Base → Create → Response)
- Data validation
- Type hints
- Hide sensitive data (password never in response)

**Why separate from Models?**
- Models = Database structure
- Schemas = API contract
- Different concerns:
  - Database might have `hashed_password`
  - API response should NOT have password
  - Create request needs password
  - Update request has optional fields

**Example:**
```python
UserCreate (has password) → Database → UserResponse (no password)
```

---

#### **3. Services Layer** (`app/services/`)
**Purpose:** Business logic (the "brain" of the application)

**Files:**
- `auth_service.py` - Authentication logic (register, login, JWT)
- `task_service.py` - Task business logic (CRUD operations)

**OOP Concepts:**
- Static methods (don't need object instance)
- Separation of concerns
- Single Responsibility Principle
- Dependency injection

**Why?**
- Routers should be thin (just handle HTTP)
- Business logic should be reusable
- Easy to test
- Easy to change logic without touching API routes

**Example Flow:**
```
Router → Service → Model → Database
         ↓
    (Business Logic)
```

---

#### **4. Routers Layer** (`app/routers/`)
**Purpose:** API endpoints (HTTP routes)

**Files:**
- `auth.py` - Authentication endpoints (/auth/register, /auth/login)
- `tasks.py` - Task endpoints (/tasks/...)

**OOP Concepts:**
- Dependency injection (FastAPI's strength)
- Decorators (@router.post, @router.get)
- Type hints for automatic validation

**Why?**
- Handles HTTP requests/responses
- Route organization
- Delegates work to services
- Thin layer (no business logic)

**Responsibility:**
- Receive HTTP request
- Validate input (automatic via Pydantic)
- Call service method
- Return HTTP response

---

#### **5. Database Layer** (`app/database/`)
**Purpose:** Database connection and session management

**Files:**
- `database.py` - Database setup, connection, session

**OOP Concepts:**
- Singleton pattern (one database connection)
- Context manager (automatic cleanup)
- Dependency injection

**Why?**
- Centralized database configuration
- Connection pooling
- Session management
- Easy to switch databases (SQLite → PostgreSQL)

---

#### **6. Config Layer** (`app/config.py`)
**Purpose:** Application configuration and environment variables

**OOP Concepts:**
- Settings class
- Singleton pattern
- Type validation

**Why?**
- Centralized configuration
- Environment variable management
- Type-safe settings
- Easy to change between dev/prod

---

#### **7. Main Application** (`app/main.py`)
**Purpose:** FastAPI application setup and entry point

**Responsibilities:**
- Create FastAPI app
- Include routers
- Setup middleware (CORS)
- Startup/shutdown events
- Root endpoints

---

## 🔄 **REQUEST FLOW EXAMPLE**

Let's trace a "Create Task" request:

```
1. User sends: POST /tasks/ with JWT token
                ↓
2. FastAPI receives request
                ↓
3. Router (tasks.py) endpoint handles it
                ↓
4. Dependency injection:
   - Validates JWT token
   - Gets current user from database
   - Creates database session
                ↓
5. Router calls TaskService.create_task()
                ↓
6. Service layer:
   - Creates Task object
   - Validates business rules
   - Saves to database
                ↓
7. Returns Task object to router
                ↓
8. Router converts to TaskResponse schema
                ↓
9. FastAPI sends JSON response to user
```

**This shows:**
- Separation of concerns
- Each layer has specific responsibility
- Easy to test each part independently
- Easy to maintain and extend

---

## 🎓 **OOP CONCEPTS YOU'LL LEARN**

### **1. Classes & Objects**
```python
# Define a class (blueprint)
class Task:
    def __init__(self, title):
        self.title = title
    
# Create an object (instance)
task = Task("Learn Python")
```

### **2. Inheritance**
```python
class TaskBase:           # Parent class
    title: str

class TaskCreate(TaskBase):  # Child inherits title
    description: str
```

### **3. Encapsulation**
```python
class User:
    hashed_password: str  # Internal only
    
    def to_dict(self):
        return {"username": self.username}
        # Password NOT included!
```

### **4. Static Methods**
```python
class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        # Don't need 'self', works on class level
        return bcrypt.hash(password)
```

### **5. Relationships**
```python
class User:
    tasks = relationship("Task")  # One-to-Many

class Task:
    owner = relationship("User")  # Many-to-One
```

### **6. Dependency Injection**
```python
async def create_task(
    db: Session = Depends(get_db),  # Injected automatically
    user: User = Depends(get_current_user)  # Injected automatically
):
    # Use db and user without creating them
```

---

## 📊 **DATA FLOW DIAGRAM**

```
┌─────────────┐
│   Client    │
│  (Browser/  │
│   Postman)  │
└──────┬──────┘
       │ HTTP Request
       ↓
┌─────────────────────────────────────────┐
│          FastAPI Application            │
│  ┌───────────────────────────────────┐  │
│  │  Routers (API Endpoints)          │  │
│  │  - Handles HTTP                   │  │
│  │  - Validates input                │  │
│  └────────────┬──────────────────────┘  │
│               ↓                          │
│  ┌───────────────────────────────────┐  │
│  │  Services (Business Logic)        │  │
│  │  - Authentication                 │  │
│  │  - Task operations                │  │
│  │  - Business rules                 │  │
│  └────────────┬──────────────────────┘  │
│               ↓                          │
│  ┌───────────────────────────────────┐  │
│  │  Models (ORM)                     │  │
│  │  - User, Task classes             │  │
│  │  - Database operations            │  │
│  └────────────┬──────────────────────┘  │
└───────────────┼──────────────────────────┘
                ↓
       ┌────────────────┐
       │  SQLite DB     │
       │  - users table │
       │  - tasks table │
       └────────────────┘
```

---

## 🎯 **WHY THIS APPLICATION IS PERFECT FOR LEARNING**

1. **Simple enough** to understand in one project
2. **Complex enough** to demonstrate real-world patterns
3. **Covers all major concepts:**
   - OOP (classes, inheritance, encapsulation)
   - REST API design
   - Authentication & Authorization
   - Database relationships
   - Clean architecture
   - Testing
   - DevOps (Docker, K8s, Terraform)

4. **Extensible:** Easy to add features later:
   - Task categories/tags
   - Task sharing
   - Email notifications
   - File attachments
   - Comments on tasks

---

## 📚 Learning Path

### **PHASE 1: Python FastAPI Application (OOP)**
Learn: FastAPI, Python OOP, Pydantic, JWT authentication

### **PHASE 2: Docker**
Learn: Dockerfile, docker-compose, multi-stage builds, container networking

### **PHASE 3: Kubernetes**
Learn: Deployments, Services, ConfigMaps, Secrets, Ingress

### **PHASE 4: Terraform**
Learn: Infrastructure as Code, AWS EKS/Local K8s provisioning

### **PHASE 5: CI/CD Pipeline**
Learn: GitHub Actions, automated testing, deployment automation

---

## 🚀 PHASE 1: FastAPI Application Setup

### Step 1.1: Install UV and Create Project Structure
```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Initialize the project with UV
uv init

# Verify UV installation
uv --version
```

### Step 1.2: Install Dependencies
```bash
# Create requirements with UV
uv add fastapi uvicorn sqlalchemy pydantic pydantic-settings python-jose passlib python-multipart bcrypt

# For development
uv add --dev pytest httpx pytest-asyncio
```

### Step 1.3: Project Structure
Create the following files and folders:
```
python_app_deployment/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── task.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── task.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── task_service.py
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       └── tasks.py
├── tests/
│   ├── __init__.py
│   └── test_api.py
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── k8s/
├── terraform/
└── .github/workflows/
```

### Step 1.4: Run the Application
```bash
# Run with UV
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Access the API documentation
# Open browser: http://localhost:8000/docs
```

### Step 1.5: Test API Endpoints
Use the Swagger UI at `http://localhost:8000/docs` to:
1. Register a new user (`POST /auth/register`)
2. Login (`POST /auth/login`) - Get JWT token
3. Create tasks (`POST /tasks`)
4. Get tasks (`GET /tasks`)
5. Update tasks (`PUT /tasks/{id}`)
6. Delete tasks (`DELETE /tasks/{id}`)

---

## 🐳 PHASE 2: Docker

### Step 2.1: Understanding the Dockerfile
The Dockerfile uses multi-stage build:
- **Stage 1 (builder)**: Install dependencies with UV
- **Stage 2 (runtime)**: Copy only necessary files for smaller image

### Step 2.2: Build and Run with Docker
```bash
# Build the Docker image
docker build -t task-api:latest .

# Run the container
docker run -d -p 8000:8000 --name task-api task-api:latest

# View logs
docker logs -f task-api

# Stop and remove
docker stop task-api
docker rm task-api
```

### Step 2.3: Docker Compose (Multiple Services)
```bash
# Start all services (app + future additions like PostgreSQL)
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild after code changes
docker-compose up -d --build
```

### Step 2.4: Key Docker Concepts Learned
- ✅ Multi-stage builds (optimized image size)
- ✅ Layer caching
- ✅ Environment variables
- ✅ Port mapping
- ✅ Volume mounts for development
- ✅ Docker networking

---

## ☸️ PHASE 3: Kubernetes

### Step 3.1: Setup Local Kubernetes
```bash
# Option 1: Docker Desktop (Enable Kubernetes in settings)
# Option 2: Minikube
brew install minikube
minikube start

# Verify
kubectl cluster-info
kubectl get nodes
```

### Step 3.2: Understand Kubernetes Manifests
Files in `k8s/` directory:
- `namespace.yaml` - Logical isolation
- `configmap.yaml` - Configuration data
- `secret.yaml` - Sensitive data (base64 encoded)
- `deployment.yaml` - Pod management
- `service.yaml` - Service discovery
- `ingress.yaml` - External access

### Step 3.3: Deploy to Kubernetes
```bash
# Apply all manifests
kubectl apply -f k8s/

# Check deployment status
kubectl get all -n task-api

# View pods
kubectl get pods -n task-api

# View logs
kubectl logs -f deployment/task-api -n task-api

# Port forward to access locally
kubectl port-forward -n task-api service/task-api 8000:80

# Access: http://localhost:8000/docs
```

### Step 3.4: Kubernetes Operations
```bash
# Scale the application
kubectl scale deployment/task-api -n task-api --replicas=3

# Update the image (rolling update)
kubectl set image deployment/task-api -n task-api task-api=task-api:v2

# Rollback deployment
kubectl rollout undo deployment/task-api -n task-api

# View rollout history
kubectl rollout history deployment/task-api -n task-api

# Delete all resources
kubectl delete -f k8s/
```

### Step 3.5: Key Kubernetes Concepts Learned
- ✅ Pods, Deployments, Services
- ✅ ConfigMaps and Secrets
- ✅ Namespaces for isolation
- ✅ Rolling updates and rollbacks
- ✅ Horizontal scaling
- ✅ Service discovery
- ✅ Health checks (liveness/readiness probes)

---

## 🏗️ PHASE 4: Terraform

### Step 4.1: Install Terraform
```bash
brew install terraform

# Verify
terraform --version
```

### Step 4.2: Understand Terraform Structure
```
terraform/
├── main.tf           # Main configuration
├── variables.tf      # Input variables
├── outputs.tf        # Output values
├── providers.tf      # Provider configuration
└── terraform.tfvars  # Variable values
```

### Step 4.3: Terraform for Local Kubernetes
```bash
cd terraform/

# Initialize Terraform
terraform init

# Preview changes
terraform plan

# Apply infrastructure
terraform apply

# View outputs
terraform output

# Destroy infrastructure
terraform destroy
```

### Step 4.4: Key Terraform Concepts Learned
- ✅ Infrastructure as Code (IaC)
- ✅ Resources and providers
- ✅ Variables and outputs
- ✅ State management
- ✅ Declarative configuration
- ✅ Kubernetes provider

---

## 🔄 PHASE 5: CI/CD Pipeline

### Step 5.1: GitHub Actions Workflow
The `.github/workflows/ci-cd.yml` automates:
1. **Continuous Integration (CI)**
   - Run tests
   - Lint code
   - Build Docker image
   - Security scanning

2. **Continuous Deployment (CD)**
   - Push image to registry
   - Deploy to Kubernetes
   - Health checks

### Step 5.2: Setup GitHub Repository
```bash
# Initialize git (if not done)
git init
git add .
git commit -m "Initial commit"

# Create repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/python_app_deployment.git
git branch -M main
git push -u origin main
```

### Step 5.3: Configure Secrets
In GitHub repository settings → Secrets and variables → Actions, add:
- `DOCKER_USERNAME` - Your Docker Hub username
- `DOCKER_PASSWORD` - Your Docker Hub password/token
- `KUBECONFIG` - Your Kubernetes config (for deployment)

### Step 5.4: Trigger Pipeline
```bash
# Push changes to trigger workflow
git add .
git commit -m "Update application"
git push

# View workflow in GitHub Actions tab
```

### Step 5.5: Key CI/CD Concepts Learned
- ✅ Automated testing
- ✅ Continuous Integration
- ✅ Continuous Deployment
- ✅ Docker image building and pushing
- ✅ GitHub Actions workflows
- ✅ Environment secrets management

---

## 🧪 Testing

### Run Tests Locally
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app tests/

# Run specific test
uv run pytest tests/test_api.py::test_register_user
```

---

## 📖 Learning Objectives Checklist

### Python & OOP
- [ ] Classes and inheritance
- [ ] Abstract base classes
- [ ] Dependency injection pattern
- [ ] Service layer architecture
- [ ] Data models vs schemas

### FastAPI
- [ ] Path operations and routing
- [ ] Request/response models with Pydantic
- [ ] Dependency injection
- [ ] JWT authentication
- [ ] Middleware
- [ ] Exception handling
- [ ] API documentation (Swagger/ReDoc)

### Docker
- [ ] Dockerfile syntax
- [ ] Multi-stage builds
- [ ] Image layers and caching
- [ ] Docker Compose
- [ ] Container networking
- [ ] Environment variables
- [ ] Volume mounts

### Kubernetes
- [ ] Pods and containers
- [ ] Deployments and ReplicaSets
- [ ] Services (ClusterIP, NodePort, LoadBalancer)
- [ ] ConfigMaps and Secrets
- [ ] Namespaces
- [ ] Rolling updates
- [ ] Health checks
- [ ] Resource limits

### Terraform
- [ ] HCL syntax
- [ ] Resources and data sources
- [ ] Variables and outputs
- [ ] State management
- [ ] Provider configuration
- [ ] Modules (bonus)

### CI/CD
- [ ] GitHub Actions workflows
- [ ] Automated testing
- [ ] Docker image building
- [ ] Deployment automation
- [ ] Secret management

---

## 🎓 Next Steps for Learning

### Enhance the Application
1. **Add PostgreSQL database** (instead of SQLite)
2. **Add Redis for caching**
3. **Implement pagination**
4. **Add task categories and tags**
5. **Implement task sharing between users**
6. **Add email notifications**
7. **Implement rate limiting**

### DevOps Enhancements
1. **Monitoring**: Add Prometheus and Grafana
2. **Logging**: Centralized logging with ELK stack
3. **Service Mesh**: Try Istio
4. **Helm Charts**: Package Kubernetes manifests
5. **ArgoCD**: GitOps workflow
6. **Cloud Deployment**: Deploy to AWS EKS/GKE/AKS

### Advanced Terraform
1. **Remote state backend** (S3 + DynamoDB)
2. **Terraform modules**
3. **Workspaces for environments**
4. **AWS infrastructure** (VPC, EKS, RDS)

---

## 📚 Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Terraform Documentation](https://www.terraform.io/docs/)
- [UV Documentation](https://docs.astral.sh/uv/)

---

## 🐛 Troubleshooting

### Common Issues
1. **Port already in use**: Change port or stop conflicting service
2. **Docker build fails**: Check Dockerfile syntax and network
3. **Kubernetes pod not starting**: Check logs with `kubectl logs`
4. **Terraform state locked**: Remove lock or wait for completion

---

## 📝 Notes
- Start with Phase 1, master it, then move to Phase 2
- Test each phase thoroughly before moving forward
- Experiment with the code - break it and fix it!
- Read the documentation for each tool
- This is a learning project - make mistakes and learn from them

---

**Happy Learning! 🚀**
