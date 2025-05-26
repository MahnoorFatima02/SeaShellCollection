from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from utils.custom_exceptions import ValidationException, NotFoundException, InternalServerException

def register_error_handlers(app: FastAPI):
    @app.exception_handler(ValidationException)
    async def validation_exception_handler(request, exc: ValidationException):
        return JSONResponse(
            status_code=400, 
            content={"error": str(exc)}
            )

    @app.exception_handler(NotFoundException)
    async def not_found_exception_handler(request, exc: NotFoundException):
        return JSONResponse(
            status_code=404,
            content={"error": "Resource Not Found"}
            )

    @app.exception_handler(InternalServerException)
    async def internal_server_exception_handler(request, exc: InternalServerException):
        return JSONResponse(
            status_code=500,
            content={"error": str(exc)}
            )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"error": "An unexpected error occurred"}
            )   