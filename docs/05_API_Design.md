# API Design

**Version:** 1.0
**Status:** Approved
**Last Updated:** July 2026

---

# Purpose

This document defines the REST API for ResearchFlow AI.

The API follows REST principles.

All communication between the frontend and backend occurs through these endpoints.

---

# Base URL

/api/v1

---

# Authentication

## Register

POST

/auth/register

---

## Login

POST

/auth/login

---

## Logout

POST

/auth/logout

---

## Current User

GET

/auth/me

---

# Research

## Create Session

POST

/research

---

## Get All Sessions

GET

/research

---

## Get Session

GET

/research/{id}

---

## Delete Session

DELETE

/research/{id}

---

## Ask Question

POST

/research/{id}/query

Request

```json
{
  "question": "Compare LangGraph and CrewAI"
}
```

---

Response

```json
{
  "status":"completed",
  "reportId":"..."
}
```

---

# Documents

## Upload

POST

/documents/upload

Multipart Form Data

---

## List Documents

GET

/documents/{researchId}

---

## Delete Document

DELETE

/documents/{id}

---

# Reports

## Get Report

GET

/reports/{id}

---

## Download PDF

GET

/reports/{id}/download

---

# Health

GET

/health

---

# Response Format

Every successful response

```json
{
  "success": true,
  "data": {},
  "message": "Success"
}
```

---

Every error response

```json
{
  "success": false,
  "error": {
    "code": "...",
    "message": "..."
  }
}
```

---

# Status Codes

200 OK

201 Created

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

422 Validation Error

500 Internal Server Error

---

# Authentication

JWT Bearer Token

Authorization

Bearer <token>

---

# Future APIs

Streaming

WebSockets

Background Jobs

Notifications

Analytics

Workspace APIs

These are not part of MVP.

---

# Engineering Decisions

Decision 1

Version APIs from day one.

Reason

Avoid breaking clients.

---

Decision 2

Keep routes resource-oriented.

Reason

REST consistency.

---

Decision 3

Separate research, document, and report APIs.

Reason

Single responsibility and maintainability.