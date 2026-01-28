import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from backend.server import app
except ImportError as e:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    app = FastAPI()
    
    @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
    async def catch_all(path: str):
        return JSONResponse(
            status_code=500,
            content={"error": f"Import error: {str(e)}", "path": path}
        )

# This is necessary for Vercel to find the app instance
handler = app
