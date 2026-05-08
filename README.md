# API Parity Lab

## Overview

This project demonstrates a common failure pattern in backend systems:

> APIs can return successful responses while the system behaves incorrectly internally.

Traditional API tests usually validate:
- Status codes
- Response schemas
- Basic response structure

But production issues frequently occur in layers that response validation does not cover:
- Incorrect persistence
- Missing observability signals
- Behavioral divergence between systems
- Concurrency-related inconsistencies

This project focuses on detecting backend inconsistencies that traditional API validation often misses.

---

## Repository Structure

This project is part of a two-repository setup:

- `api-parity-lab` → System under test
- `api-parity-qa` → Validation framework and parity test suite

The API intentionally injects controlled failure scenarios that are difficult to detect through traditional testing alone.

---

## Architecture

```text
Client
   ↓
FastAPI Service
   ↓
Persistence Layer (SQLite)
   ↓
Application Logs
```

---

## Validation Dimensions

The companion validation suite verifies:
- Response validation
- Contract validation
- Persistence validation
- Log validation
- Parity validation
- Runtime consistency validation

---

## Clone Repository

```bash
git clone https://github.com/mmuller/api-parity-lab
cd api-parity-lab
```

---

## Quick Start

### Setup environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

---

### Start the API

```bash
uvicorn app.main:app --reload
```

API endpoint:

```text
http://localhost:8000
```

---

## Run the Companion Validation Framework

### Clone the validation suite

```bash
git clone https://github.com/mmuller/api-parity-qa
cd api-parity-qa
```

### Configure target environment

```bash
export BASE_URL=http://localhost:8000
```

### Execute validations

```bash
pytest \
  --html=reports/API_Parity_Validation_Report.html \
  --self-contained-html \
  --metadata "framework" "pytest" \
  --metadata "validation" "api-parity" \
  --metadata "scope" "backend"
```

---

## Validation Layers

| Layer       | Purpose                                  |
|-------------|------------------------------------------|
| Response    | API availability and status validation   |
| Contract    | Schema and response structure validation |
| Data        | Persistence consistency validation       |
| Logs        | Observability verification               |
| Parity      | Behavioral consistency between systems   |
| Concurrency | Runtime consistency under load           |

---

## Failure Injection Modes

Controlled failure scenarios can be enabled through request headers:

```http
x-bug-mode: silent_db_bug
x-bug-mode: missing_log
x-bug-mode: bad_correlation
```

These simulate realistic backend failures such as:
- Silent data corruption
- Observability gaps
- Duplicate trace identifiers under concurrency

---

## Example Execution

```bash
pytest tests/response      # PASS
pytest tests/contract      # PASS
pytest tests/e2e           # PASS
pytest tests/data          # FAIL
pytest tests/logs          # FAIL
pytest tests/bug           # FAIL
```

The same API response may appear valid while deeper validation layers reveal system inconsistencies.

---

## Failure Detection & System Validation

Some tests are intentionally designed to fail in order to demonstrate detection capabilities for:
- Silent data corruption
- Missing observability signals
- Correlation ID reuse / concurrency issues
- Invalid data persistence

The goal of the project is not only validating responses, but also validating correctness, consistency, and runtime system behavior across APIs, databases, and logs.

---

## Why This Matters

Many production failures are not response-level failures.

Systems may satisfy API contracts while still producing:
- Corrupted persistence state
- Observability gaps
- Behavioral inconsistencies
- Hidden operational drift

This project focuses on detecting those conditions.

---

## Real-World Inspiration

Several scenarios in this project are inspired by real-world migration and distributed-system validation challenges commonly encountered in enterprise environments.

---

## Related Repository

Companion validation framework:

- [api-parity-qa](https://github.com/mmuller/api-parity-qa)
