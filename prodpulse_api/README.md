```markdown   
# ProdPulse API

A modular, Django REST Framework–powered backend for managing users, organizations, products, orders, pulses (time-series metrics) and analytics. Designed for real-time dashboards, async ingestion, multi-channel notifications, and enterprise-grade secret management.

---

## Table of Contents

- [Features](#features)  
- [External Integrations](#external-integrations)  
- [Data Models](#data-models)  
- [API Endpoints](#api-endpoints)  
- [Setup & Installation](#setup--installation)  
- [Environment & Secrets](#environment--secrets)  
- [Testing](#testing)  
- [Conclusive Summary](#conclusive-summary)  
- [Challenges & Solutions](#challenges--solutions)  
- [Next Steps](#next-steps)  

---

## Features

- User registration and JWT-based authentication (access + refresh)  
- Custom `User` model with roles (`admin`, `vendor`, `user`) and `Organization` grouping  
- CRUD operations for Products, Categories, Tags, Reviews, Orders (with `OrderItem`)  
- Full-text search on Products (`SearchVector` + GIN index)  
- Pagination, sorting, filtering (price range, category, availability)  
- Image uploads via Cloudinary (signed URLs, transformations)  
- Stock management with low-stock notifications (Celery + Mailgun webhook)  
- Role-based access control for admin vs. vendor vs. end user  
- Async metric ingestion (`httpx` + `sync_to_async`) and real-time “pulse” streaming (Django Channels + WebSockets)  
- Multi-channel alerts: Slack webhook, SendGrid email, Twilio SMS  
- Basic analytics endpoints:  
  - Sales estimates (`/api/analytics/sales/estimate/`)  
  - Stripe usage summaries (`/api/analytics/stripe/usage/`)  
  - Product view counts (`/api/analytics/products/views/`)  
- Interactive API documentation via Swagger/OpenAPI (`drf-spectacular`)  
- Redis caching for hot list views  

---

## External Integrations

- **Cloudinary**: image storage, transformations, signed URLs  
- **Mailgun**: email notifications for orders and low-stock alerts  
- **Twilio**: SMS notifications for critical events  
- **Stripe**: analytics (usage record summaries) via API key, rate-limited  

---

## Data Models

- **User** (`apps/users/models.py`)  
  - Inherits `AbstractUser`, adds `email` (unique), `role`, and optional org FK  
- **Organization** (`apps/users/models.py`)  
  - `name`, `created_at`, `updated_at`  
- **Category** & **Tag** (`apps/products/models.py`)  
  - `name`, `slug`, M2M with `Product`  
- **Product** (`apps/products/models.py`)  
  - `title`, `description`, `price`, `stock_qty`, `sku`, `is_active`, `created_at`, `search_vector`  
- **Review** (`apps/products/models.py`)  
  - `rating`, `comment`, FK to `Product` and `User`  
- **Order** & **OrderItem** (`apps/orders/models.py`)  
  - `status`, `total_amount`, M2M through `OrderItem`, FK to `User`  
- **Pulse** (`apps/pulses/models.py`)  
  - `product_id`, `timestamp`, `value`, `unit`  
- **ProductView** (`apps/analytics/models.py`)  
  - Tracks `count` per `Product`  

---

## API Endpoints

| Path                                      | Method              | Description                             |
|-------------------------------------------|---------------------|-----------------------------------------|
| `/api/auth/register/`                     | POST                | Create new user (public)                |
| `/api/token/` & `/api/token/refresh/`     | POST                | Obtain or refresh JWT                   |
| `/api/users/users/`                       | GET, POST           | List/create users (admin)               |
| `/api/products/products/`                 | GET, POST           | List/create products (vendor/admin)     |
| `/api/products/products/{id}/`            | GET, PUT, DELETE    | Retrieve/update/delete product          |
| `/api/categories/`                        | GET, POST           | List/create categories                  |
| `/api/tags/`                              | GET, POST           | List/create tags                        |
| `/api/products/products/{id}/reviews/`    | GET, POST           | List/add product reviews                |
| `/api/orders/orders/`                     | GET, POST           | List/create orders                      |
| `/api/analytics/sales/estimate/`          | GET                 | Sum of all order totals (admin)         |
| `/api/analytics/stripe/usage/`            | GET                 | Stripe monthly usage summary (admin)    |
| `/api/analytics/products/views/`          | GET                 | Product view counts                     |
| WebSocket: `ws://…/ws/pulses/stream/`     | WebSocket           | Real-time pulse streaming               |

---

## Setup & Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/your-org/prodpulse-api.git
   cd prodpulse-api
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Configured database and `.env` settings
5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```