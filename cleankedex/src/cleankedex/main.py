from fastapi import FastAPI

# Settings available for the application
from cleankedex.config.settings.settings import settings
from cleankedex.config.application.start_app import start_application


# Initialize application
app: FastAPI = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
start_application(app=app)
