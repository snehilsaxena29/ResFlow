# Development Guide

**Version:** 1.0
**Status:** Approved
**Last Updated:** July 2026

---

# Purpose

This document defines the development environment, coding standards, Git workflow, and project conventions for ResearchFlow AI.

Every contributor should be able to clone the repository and start development by following this guide.

---

# Development Philosophy

ResearchFlow AI is built using an MVP-first approach.

Phase 1 focuses on shipping a polished resume-worthy project.

Phase 2 focuses on scaling the architecture into a production-grade platform.

We optimize for:

* Simplicity
* Readability
* Modularity
* Incremental development

---

# Required Software

## Backend

* Python 3.12+
* pip
* PostgreSQL 16+
* Git

---

## Frontend

* Node.js 22 LTS
* npm

---

## IDE

Recommended

* Visual Studio Code

Recommended Extensions

* Python
* Pylance
* Black Formatter
* Prettier
* ESLint
* Tailwind CSS IntelliSense
* GitLens
* Error Lens
* Docker

---

# Project Structure

```
ResearchFlow-AI/

backend/
frontend/
docs/
tests/
docker/
scripts/
```

---

# Backend Structure

```
backend/

app/

api/
routes/
dependencies/

core/

database/

models/

schemas/

repositories/

services/

agents/

workflows/

llm/

prompts/

utils/

tests/

main.py
```

---

# Frontend Structure

```
frontend/

src/

components/

pages/

layouts/

hooks/

services/

context/

utils/

assets/
```

---

# Branch Strategy

Main branches

* main
* develop

Feature branches

Examples

feature/backend-setup

feature/authentication

feature/research-session

feature/planner-agent

feature/report-generator

---

# Commit Convention

Use Conventional Commits.

Examples

```
feat(auth): implement JWT authentication

feat(research): create research session API

docs(system): update architecture

fix(report): resolve markdown export bug

refactor(agent): simplify planner workflow

test(auth): add login tests

chore: configure pre-commit hooks
```

---

# Coding Standards

## Python

* Follow PEP 8
* Use type hints
* Keep functions small
* Prefer dependency injection
* Avoid global variables

---

## JavaScript

* Use ES6+
* Prefer async/await
* Use meaningful names
* Keep components focused

---

# Naming Conventions

## Python

Classes

UserService

PlannerAgent

ResearchWorkflow

Functions

create_session()

generate_report()

verify_token()

Variables

research_session

planner_output

document_chunks

---

# Environment Variables

Backend

```
DATABASE_URL=

JWT_SECRET=

JWT_ALGORITHM=

LLM_PROVIDER=

GOOGLE_API_KEY=

OLLAMA_BASE_URL=
```

Frontend

```
NEXT_PUBLIC_API_URL=
```

---

# Development Workflow

Every feature follows the same process.

1. Create GitHub Issue
2. Create Feature Branch
3. Implement Feature
4. Test Feature
5. Update Documentation
6. Commit
7. Open Pull Request (optional for solo development)
8. Merge into develop

---

# Definition of Done

A feature is considered complete only if:

* Code is working
* Errors are handled
* API is tested
* Documentation is updated
* Commit message follows convention
* Code is pushed to GitHub

---

# MVP Development Order

Sprint 1

* Backend Setup
* Database Connection
* Health Endpoint

Sprint 2

* Authentication
* User Management

Sprint 3

* Research Sessions

Sprint 4

* Planner Agent

Sprint 5

* Search Agent

Sprint 6

* Document Upload
* FAISS Integration

Sprint 7

* Report Generation

Sprint 8

* Frontend Integration

Sprint 9

* Deployment

---

# Rules

* Never hardcode secrets.
* Never mix business logic with API routes.
* Keep prompts outside Python files.
* Keep agents independent.
* Every feature should be modular.
* Every major decision must be documented.

---

# Future Improvements

* Docker Compose
* GitHub Actions
* Unit Tests
* Integration Tests
* Background Jobs
* Redis
* Streaming Responses
* Production Monitoring
