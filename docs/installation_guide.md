# OpenFootprint Installation Guide

This guide provides instructions for installing and setting up the OpenFootprint CSRD compliance reporting software.

## System Requirements

### Server Requirements
- **Operating System**: Linux (Ubuntu 20.04 LTS or newer recommended)
- **CPU**: 2+ cores
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 20GB minimum

### Software Prerequisites
- **Python**: 3.10 or newer
- **PostgreSQL**: 13 or newer
- **Node.js**: 16 or newer
- **npm**: 8 or newer
- **Git**: 2.25 or newer

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/d-ajvdvoort/openfootprint.git
cd openfootprint
```

### 2. Set Up Backend

#### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

#### Configure Database

Create a PostgreSQL database:

```bash
sudo -u postgres psql
```

In the PostgreSQL shell:

```sql
CREATE DATABASE openfootprint;
CREATE USER openfootprint_user WITH ENCRYPTED PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE openfootprint TO openfootprint_user;
\q
```

Update the database connection string in `backend/app/db/database.py`:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://openfootprint_user:your_secure_password@localhost/openfootprint"
```

#### Run Migrations

```bash
cd backend
alembic upgrade head
```

#### Create .env File

Create a `.env` file in the `backend` directory:

```
DATABASE_URL=postgresql://openfootprint_user:your_secure_password@localhost/openfootprint
SECRET_KEY=your_secret_key_for_jwt_tokens
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Replace `your_secret_key_for_jwt_tokens` with a secure random string.

### 3. Set Up Frontend

#### Install Dependencies

```bash
cd frontend
npm install
```

#### Configure API URL

Create a `.env` file in the `frontend` directory:

```
REACT_APP_API_URL=http://localhost:8000/api
```

### 4. Development Mode Setup

#### Run Backend Server

```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Run Frontend Development Server

```bash
cd frontend
npm start
```

The frontend will be available at http://localhost:3000

### 5. Production Deployment

#### Backend Deployment

Install production dependencies:

```bash
pip install gunicorn
```

Create a systemd service file at `/etc/systemd/system/openfootprint.service`:

```
[Unit]
Description=OpenFootprint Backend
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/path/to/openfootprint/backend
ExecStart=/path/to/openfootprint/venv/bin/gunicorn -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000 app.main:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Start and enable the service:

```bash
sudo systemctl start openfootprint
sudo systemctl enable openfootprint
```

#### Frontend Deployment

Build the frontend:

```bash
cd frontend
npm run build
```

Install and configure Nginx:

```bash
sudo apt install nginx
```

Create an Nginx configuration file at `/etc/nginx/sites-available/openfootprint`:

```
server {
    listen 80;
    server_name your_domain.com;

    location / {
        root /path/to/openfootprint/frontend/build;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://localhost:8000/api;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/openfootprint /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 6. SSL Configuration (Recommended for Production)

Install Certbot:

```bash
sudo apt install certbot python3-certbot-nginx
```

Obtain and configure SSL certificate:

```bash
sudo certbot --nginx -d your_domain.com
```

Follow the prompts to complete the SSL configuration.

## Docker Installation (Alternative)

### Prerequisites
- Docker
- Docker Compose

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/d-ajvdvoort/openfootprint.git
   cd openfootprint
   ```

2. Create a `.env` file in the root directory:
   ```
   POSTGRES_USER=openfootprint_user
   POSTGRES_PASSWORD=your_secure_password
   POSTGRES_DB=openfootprint
   SECRET_KEY=your_secret_key_for_jwt_tokens
   ```

3. Build and start the containers:
   ```bash
   docker-compose up -d
   ```

4. Run migrations:
   ```bash
   docker-compose exec backend alembic upgrade head
   ```

The application will be available at http://localhost:3000

## Post-Installation Steps

### Create an Admin User

```bash
cd backend
python -m app.scripts.create_admin_user --username admin --password secure_password --email admin@example.com
```

### Verify Installation

1. Open a web browser and navigate to your OpenFootprint instance
2. Log in with the admin credentials you created
3. Navigate to the Dashboard to verify that the application is working correctly

## Troubleshooting

### Database Connection Issues

If you encounter database connection issues:

1. Verify PostgreSQL is running:
   ```bash
   sudo systemctl status postgresql
   ```

2. Check database credentials in `backend/app/db/database.py`

3. Ensure the database exists and the user has appropriate permissions:
   ```bash
   sudo -u postgres psql -c "\l"
   ```

### Backend Server Not Starting

If the backend server fails to start:

1. Check for error messages in the logs:
   ```bash
   sudo journalctl -u openfootprint
   ```

2. Verify the virtual environment is activated and dependencies are installed

### Frontend Not Loading

If the frontend doesn't load:

1. Check Nginx configuration:
   ```bash
   sudo nginx -t
   ```

2. Verify the build directory exists and contains the built files:
   ```bash
   ls -la /path/to/openfootprint/frontend/build
   ```

3. Check Nginx logs:
   ```bash
   sudo tail -f /var/log/nginx/error.log
   ```

## Upgrading

To upgrade to a newer version:

1. Pull the latest changes:
   ```bash
   cd /path/to/openfootprint
   git pull
   ```

2. Update backend dependencies:
   ```bash
   cd backend
   source ../venv/bin/activate
   pip install -r requirements.txt
   alembic upgrade head
   ```

3. Update frontend dependencies and rebuild:
   ```bash
   cd frontend
   npm install
   npm run build
   ```

4. Restart services:
   ```bash
   sudo systemctl restart openfootprint
   sudo systemctl restart nginx
   ```

## Support

For installation support, please contact your OpenFootprint administrator or support team.
