# FastAPI MVC Project

A modern, scalable FastAPI application following Clean Architecture principles and MVC pattern.

## 🚀 Features

- Clean Architecture implementation
- MVC (Model-View-Controller) pattern
- PostgreSQL database integration
- Pydantic for data validation
- SQLAlchemy ORM
- Environment-based configuration
- Type hints and strict typing

## 🛠️ Tech Stack

- Python 3.x
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

## 📋 Prerequisites

- Python 3.x
- PostgreSQL
- pip (Python package manager)

## 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi_mvc
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

## 🚀 Running the Application

1. Start the server:
```bash
uvicorn app.main:app --reload
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📁 Project Structure

```
fastapi_mvc/
├── app/
│   ├── controllers/     # Request handlers
│   ├── models/         # Database models
│   ├── repositories/   # Data access layer
│   ├── dtos/          # Data Transfer Objects
│   ├── db/            # Database configuration
│   └── main.py        # Application entry point
├── requirements.txt    # Project dependencies
└── .env              # Environment variables
```

## 📚 Documentation

For detailed technical documentation, please refer to [TECHNICAL.md](TECHNICAL.md).

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
