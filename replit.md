# ProdPulse API - Replit Setup

## Overview
This is a Django REST API project for product performance monitoring called "ProdPulse API". It's been successfully configured to run in the Replit environment with SQLite database and is ready for development and deployment.

## Project Architecture
- **Framework**: Django 5.2.5 with Django REST Framework
- **Database**: SQLite (for development)
- **Authentication**: JWT with djangorestframework-simplejwt
- **Server**: Development server running on port 5000
- **Language**: Python 3.11

## Current Setup Status
✅ **Completed**:
- Django dependencies installed
- Database migrations applied
- Development server running on port 5000
- Basic API health check endpoint working at `/api/`
- Deployment configuration set for VM deployment
- Environment configured for Replit with allowed hosts set to "*"

## Recent Changes (Sept 4, 2025)
- Fixed Django settings module path from `core.settings` to `prodpulse_api.core.settings`
- Configured ALLOWED_HOSTS = ["*"] for Replit proxy compatibility
- Simplified INSTALLED_APPS to include only working components initially
- Fixed file structure issues (renamed `__init__,py` to `__init__.py` in products app)
- Configured WSGI path to `prodpulse_api.wsgi.application`
- Created basic API health check endpoint for initial testing

## Working API Endpoints
- `/api/` - Health check endpoint (returns JSON status)
- `/api/token/` - JWT token obtain
- `/api/token/refresh/` - JWT token refresh
- `/admin/` - Django admin interface

## Project Structure
```
├── apps/
│   ├── api/          # Main API app (working)
│   ├── products/     # Products management (configured but not active)
│   ├── authentication/
│   ├── pulses/       
│   └── users/        
├── prodpulse_api/
│   ├── core/         # Django core settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── asgi.py
│   └── wsgi.py
└── manage.py
```

## Development Workflow
The project is running with:
- Django development server on port 5000
- Auto-reload enabled for file changes
- SQLite database ready for development
- JWT authentication configured

## Next Steps for Full Feature Implementation
1. Gradually add back individual app modules with proper configurations
2. Set up PostgreSQL database for production
3. Configure static files serving
4. Add comprehensive API endpoints for products, users, and analytics
5. Set up proper error handling and logging

## User Preferences
- Using Django REST Framework for API development
- SQLite for development, preparing for PostgreSQL in production
- JWT authentication preferred
- Clean API structure with health checks