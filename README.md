# SuperBenchmark: LLM Performance Analysis API

___

## Project Description

SuperBenchmark is a Django-based REST API for managing and analyzing Large Language Model (LLM) performance benchmarking results. The application provides endpoints to retrieve average performance statistics across different benchmarking tests.

### Key Features

- REST API for querying LLM benchmarking results
- Aggregate performance metrics calculation
- Time-based filtering of benchmark results
- DEBUG mode with test data loading
- Configurable through environment variables

## Prerequisites

Before running the project, ensure you have:

- Python 3.10+
- pip (Python package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sergey-Chalyi/djangoRESTFramework_BenchmarksFromLLM.git
   cd djangoRESTFramework_BenchmarksFromLLM
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file in the project root (optional):

   ```
   SUPERBENCHMARK_DEBUG=True
   ```

5. Apply database migrations:

   ```bash
   cd base
   python manage.py makemigrations
   python manage.py migrate
   ```

## Running the Project

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Access the application:
   - Base URL: `http://localhost:8000`

## API Endpoints

### Benchmark Results

#### Get Average Performance Metrics

```http
GET /results/average/
```

Returns average performance statistics across all benchmarking results.

#### Get Average Performance Metrics by Time Range

```http
GET /results/average/<start_time>/<end_time>/
```

Returns average performance statistics within a specified time window.

**Note:** Both endpoints are only accessible in DEBUG mode.

### Parameters for Time Range Endpoint

- `start_time`: ISO 8601 formatted start datetime
- `end_time`: ISO 8601 formatted end datetime

## Configuration

### Environment Variables

- `SUPERBENCHMARK_DEBUG`:
  - `True`: Enable test data loading and full API functionality
  - `False`: Disable test data and API endpoints

## DEBUG Mode

In DEBUG mode, the application:

- Loads test data from `test_database.json`
- Enables full API functionality
- Provides detailed error information

## Performance Metrics

Each benchmark result includes:

- Request ID
- Prompt text
- Generated text
- Token count
- Time to first token
- Time per output token
- Total generation time
- Timestamp

## Development

- Framework: Django 5.1.2
- REST Framework: Django REST Framework
- Database: SQLite (development)

## Security Considerations

- Environment-based configuration
- Limited API access in production mode
- Secure handling of benchmark data

## Contact

For questions and support:

- Email: <ch.sergey.rb@gmail.com>
