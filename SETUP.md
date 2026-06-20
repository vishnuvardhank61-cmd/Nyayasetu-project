# NyayaSetu - Setup & Installation Guide

## Phase Completion Summary

✅ **Phase 1: Security & Performance Fixes**
- Fixed sensitive credentials exposure (settings.py)
- Added environment variable support (python-decouple)
- Fixed N+1 query problem in complaints views
- Added proper model validation and constraints
- Implemented error handling and logging
- Added audit fields (updated_at)
- Optimized database queries with select_related/prefetch_related

✅ **Phase 2: New Features - 7 New Apps Created**
1. `women_safety` - Women's safety rights and laws
2. `regions` - State-specific laws (J&K, etc.)
3. `violations` - Consequences of rights violations
4. `documents` - Government documents with guides/PDFs
5. `applications` - Government service applications (Driving License, PAN, Voter ID, Vehicle Registration)
6. `police_stations` - Police stations with Leaflet & OpenStreetMap support
7. `helplines` - Emergency helplines and support services

---

## Installation Steps

### 1. **Install Python Dependencies**

```bash
cd nyayasetu
pip install -r requirements.txt
```

### 2. **Create .env File**

Copy `.env.example` to `.env` and fill in your configuration:

```bash
cp .env.example .env
```

Update `.env` with:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,yourdomain.com
```

### 3. **Create Logs Directory**

```bash
mkdir logs
```

### 4. **Run Migrations**

Create migration files for new apps:

```bash
python manage.py makemigrations accounts
python manage.py makemigrations women_safety
python manage.py makemigrations regions
python manage.py makemigrations violations
python manage.py makemigrations documents
python manage.py makemigrations applications
python manage.py makemigrations police_stations
python manage.py makemigrations helplines
python manage.py makemigrations complaints
python manage.py makemigrations rights
```

Apply migrations:

```bash
python manage.py migrate
```

### 5. **Create Superuser**

```bash
python manage.py createsuperuser
```

### 6. **Collect Static Files** (for production)

```bash
python manage.py collectstatic --noinput
```

### 7. **Run Development Server**

```bash
python manage.py runserver
```

Visit: http://localhost:8000/admin

---

## Database Structure

### New Models Created:

**women_safety/**
- `WomenSafetyRight` - Women-specific safety rights (8 fields)

**regions/**
- `State` - Indian states/UTs
- `RegionalLaw` - State-specific laws (10 fields)

**violations/**
- `ViolationConsequence` - Consequences of rights violations (7 fields)

**documents/**
- `GovernmentDocument` - Govt documents with guides (13 fields)

**applications/**
- `ApplicationService` - Available services
- `UserApplication` - User submissions (10 fields)

**police_stations/**
- `PoliceStation` - Police stations with coordinates (12 fields)

**helplines/**
- `Helpline` - Emergency helplines (11 fields)

---

## URL Routing Map

```
/                              → Home
/admin/                        → Admin Panel
/accounts/                     → User account management
/accounts/register/            → Register
/accounts/login/               → Login
/accounts/dashboard/           → Dashboard
/accounts/profile/             → Profile

/rights/                       → Fundamental rights
/women-safety/                 → Women's safety rights
/regional-laws/                → State-specific laws
/violations/                   → Violation consequences
/complaints/                   → File complaints
/documents/                    → Government documents
/services/                     → Government service applications
/police-stations/              → Police stations with maps
/helplines/                    → Emergency helplines
```

---

## Admin Management

All new models have full admin interfaces with:
- List displays
- Search and filtering
- Custom fieldsets
- Readonly audit fields

Access via: http://localhost:8000/admin

---

## TODO Before Production

- [ ] Create superuser
- [ ] Add seed data (states, laws, documents, etc.)
- [ ] Setup email backend (Gmail, SendGrid, etc.)
- [ ] Finalize Bootstrap 5 templates
- [ ] Setup multi-language translations
- [ ] Configure static file hosting (CDN)
- [ ] Setup database backups
- [ ] Enable HTTPS/SSL
- [ ] Configure CORS settings in .env

---

## Management Commands to Create

```bash
# Add seed data
python manage.py seed_states
python manage.py seed_laws
python manage.py seed_documents
python manage.py seed_helplines
```

---

## Testing

Run tests:

```bash
python manage.py test
```

---

## Support & Documentation

- Django Docs: https://docs.djangoproject.com/
- Bootstrap 5: https://getbootstrap.com/
- Leaflet.js: https://leafletjs.com/
