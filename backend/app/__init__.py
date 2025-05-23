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


# Register routes
app.include_router(shell_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")

# Register error handlers
register_error_handlers(app)