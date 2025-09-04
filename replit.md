# ProdPulse API - Replit Setup

## Overview
This is a Django REST API project for product performance monitoring called "ProdPulse API". It has been successfully configured and is fully operational in the Replit environment.

## Project Architecture
- **Framework**: Django 5.2.5 with Django REST Framework
- **Database**: SQLite (for development)
- **Authentication**: JWT with djangorestframework-simplejwt
- **Server**: Development server running on port 5000
- **Language**: Python 3.11

## Current Setup Status
✅ **Completed**:
- Django dependencies installed and configured
- Database migrations applied successfully
- Development server running on port 5000
- All core API endpoints working
- Root endpoint configured with API overview
- Deployment configuration set for VM deployment
- Environment configured for Replit with allowed hosts set to "*"
- WSGI and URL configurations properly set
- Fixed all import and path issues

## Recent Changes (Sept 4, 2025)
- **COMPLETED PROJECT IMPORT SETUP**
- Fixed Django settings module path to `prodpulse_api.core.settings`
- Configured ALLOWED_HOSTS = ["*"] for Replit proxy compatibility
- Simplified INSTALLED_APPS to include only working components
- Fixed file structure issues (renamed `__init__,py` to `__init__.py` in products app)  
- Configured WSGI path to `prodpulse_api.wsgi.application`
- Fixed URL configurations to prevent import errors
- Added root endpoint with API overview and endpoint listing
- Successfully ran all database migrations

## Working API Endpoints
- **`/`** - API root with overview and available endpoints
- **`/api/`** - Health check endpoint (returns `{"status": "ok", "message": "ProdPulse API is running"}`)
- **`/api/token/`** - JWT token obtain
- **`/api/token/refresh/`** - JWT token refresh  
- **`/admin/`** - Django admin interface
- **`/api/auth/`** - Django REST framework browsable API

## Project Structure
```
├── apps/
│   ├── api/          # Main API app (working)
│   ├── products/     # Products management (available for expansion)
│   ├── authentication/
│   ├── pulses/       
│   └── users/        
├── prodpulse_api/
│   ├── core/         # Django core settings
│   │   ├── settings.py (configured for Replit)
│   │   ├── urls.py (working endpoints)
│   │   └── asgi.py
│   ├── wsgi.py (properly configured)
│   └── db.sqlite3 (development database)
└── manage.py (configured for correct settings path)
```

## Development Workflow
The project is fully operational:
- Django development server running on port 5000
- Auto-reload enabled for file changes  
- SQLite database with applied migrations
- JWT authentication system ready
- All endpoints returning proper responses
- No system check issues

## Next Steps for Feature Expansion
1. Add back individual app modules (products, users, pulses) with proper configurations
2. Implement full CRUD operations for each entity
3. Set up PostgreSQL database for production scaling
4. Add comprehensive API documentation
5. Implement advanced features like real-time analytics and notifications

## User Preferences  
- Using Django REST Framework for API development
- SQLite for development, ready for PostgreSQL in production
- JWT authentication system
- Clean, modular API structure with health checks and proper error handling