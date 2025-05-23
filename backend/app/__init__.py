from fastapi import FastAPI, Depends, Security, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes.shell_routes import shell_router
from app.error_handlers import register_error_handlers
from routes.user_routes import user_router
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI(title="SeaShell API", description="API for managing seashell collections", version="1.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security scheme for Swagger UI
bearer_scheme = HTTPBearer()


# def get_current_user(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
#     token = credentials.credentials
#     # Validate token here (e.g., decode JWT, check DB, etc.)
#     if not token or token != "your_expected_token":
#         raise HTTPException(status_code=401, detail="Invalid or missing token")
#     return token

# Register routes
app.include_router(shell_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")

# Register error handlers
register_error_handlers(app)