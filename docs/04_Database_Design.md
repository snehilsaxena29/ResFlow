# Database Design

**Version:** 1.0
**Status:** Approved
**Last Updated:** July 2026

---

# Purpose

This document defines the relational database schema for the MVP of ResearchFlow AI.

The database is responsible for storing application data such as users, research sessions, uploaded documents, generated reports, and conversations.

The database is **not responsible** for storing vector embeddings.

Embeddings are stored separately in FAISS.

---

# Database Choice

Technology

- PostgreSQL

Reason

- ACID compliance
- Strong relational support
- Mature Python ecosystem
- Easy migration using Alembic
- Production ready

---

# High-Level ER Diagram

```
User
 │
 ├──────────────┐
 │              │
ResearchSession Document
 │              │
 │              │
Conversation    │
 │              │
 └──────────────┘
        │
      Report
```

---

# Tables

## User

Purpose

Stores user information.

Fields

- id (UUID)
- full_name
- email
- password_hash
- created_at
- updated_at

Relationship

One User

↓

Many Research Sessions

---

## Research Session

Purpose

Represents one research project.

Example

"LangGraph vs CrewAI"

Fields

- id
- user_id
- title
- status
- created_at
- updated_at

Relationship

One Research Session

↓

Many Conversations

↓

Many Documents

↓

One Report

---

## Conversation

Purpose

Stores messages exchanged during research.

Fields

- id
- research_session_id
- role (user / assistant)
- content
- timestamp

---

## Document

Purpose

Stores uploaded document metadata.

Fields

- id
- research_session_id
- file_name
- file_path
- file_size
- upload_time

The actual PDF remains on disk (MVP).

Only metadata is stored in PostgreSQL.

---

## Report

Purpose

Stores generated research reports.

Fields

- id
- research_session_id
- markdown_content
- pdf_path
- created_at

---

# FAISS

FAISS stores:

- Embeddings
- Chunk IDs
- Metadata References

FAISS never stores:

- User passwords
- Reports
- Authentication data

---

# Relationships

User

1

↓

N

Research Session

Research Session

1

↓

N

Conversation

Research Session

1

↓

N

Document

Research Session

1

↓

1

Report

---

# Data Ownership

User owns

- Research Sessions

Research Session owns

- Documents
- Conversations
- Reports

Deleting a research session should remove all associated data.

---

# Future Tables

Future versions may introduce:

- Workspace
- Research Template
- Citation
- Agent Execution
- Analytics
- Notifications

These are intentionally excluded from the MVP.

---

# Engineering Decisions

Decision 1

Store only metadata for uploaded files.

Reason

Allows future migration to cloud storage.

---

Decision 2

Use UUIDs instead of auto-increment IDs.

Reason

Better for distributed systems and external APIs.

---

Decision 3

Separate relational data from vector data.

Reason

PostgreSQL and FAISS solve different problems.

---

Decision 4

Research Sessions are the central entity of the application.

Reason

Almost every feature belongs to a research session.