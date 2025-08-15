# ProdPulse API

A lightweight, Django REST Framework–powered backend for managing users, organizations, products, and time-series pulses.

## Key Features

- Custom User model with unique email and role field  
- Organization model for multi-tenant grouping  
- JWT authentication via djangorestframework-simplejwt  
- Role-based permissions (`Admin`, `Vendor`, `User`)  
- Modular apps:  
  - **authentication** (register, login, logout)  
  - **users** (profile CRUD)  
  - **products** (categories & items)  
  - **pulses** (metrics time-series)  

## Getting Started

1. Clone the repo  
2. Create a virtualenv and install requirements  
3. Configure your database and `.env` settings  
4. Run migrations:  
   ```bash
   python manage.py makemigrations
   python manage.py migrate