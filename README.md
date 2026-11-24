# Network Security System

An end-to-end Machine Learning pipeline designed to detect and classify network security threats (such as phishing and malicious traffic). Built with a modular, production-ready architecture, containerization, and CI/CD workflows.

---

## Project Architecture

```text
networksecurity/
├── .github/workflows/    # CI/CD automation pipelines
├── .vscode/              # Editor configuration
├── networksecurity/      # Core application package
│   ├── cloud/            # Cloud storage & deployment integrations
│   ├── components/       # Data ingestion, validation, transformation & model training
│   ├── constant/         # Project-wide constants and configuration parameters
│   ├── entity/           # Configuration and artifact data classes
│   ├── exception/        # Custom exception handling
│   ├── logging/          # Centralized application logging
│   ├── pipeline/         # Training and batch prediction pipelines
│   └── utils/            # Reusable helper functions
├── .gitignore            # Git ignore rules
├── Dockerfile            # Container image definition
├── README.md             # Project documentation
├── requirements.txt      # Project dependencies
└── setup.py              # Package installation script
```

---

## Getting Started & Local Setup

### Prerequisites
- **Python 3.9+**
- **Git**
- **Docker** *(optional, for containerized runs)*

### 1. Clone the Repository
```bash
git clone https://github.com/rashidkhan-DataScience/networksecurity.git
cd networksecurity
```

### 2. Create and Activate a Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows (Command Prompt / PowerShell)
venv\Scripts\activate

# Activate on macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies & Package
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### 4. Environment Variables (Optional)
If your pipeline uses cloud credentials, database URIs, or API keys, create a `.env` file in the project root before running pipelines:
```env
# Example environment variables
MONGODB_URL=your_mongodb_connection_string
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
```

---

## Running with Docker

To build and run the project inside a container:

```bash
docker build -t networksecurity .
docker run -p 8080:8080 networksecurity
```

---

## Tech Stack
- **Language:** Python
- **Packaging:** `setuptools` (`setup.py`)
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

---

## License
This project is open-source and available under the [MIT License](LICENSE).