# System Architecture

**Version:** 1.0
**Status:** Approved
**Last Updated:** July 2026

---

# Purpose

This document defines the high-level architecture of ResearchFlow AI.

The goal is to build a modular AI research platform that is easy to understand, maintain, and scale.

The MVP architecture focuses on simplicity while ensuring that future production features can be added without major rewrites.

---

# High-Level Architecture

```

+-------------------------+
\| Next.js Frontend |
+-----------+-------------+
|
REST API
|
+-----------v-------------+
\| FastAPI Backend |
+-----------+-------------+
|
+---------------------+----------------------+
| | |
Auth Research Document
Service Service Service
| | |
+---------------------+----------------------+
|
Research Service
|
Agent Orchestrator
(LangGraph)
|
+--------+--------+--------+--------+
| | | |
Planner Search Retrieval Report
Agent Agent Agent Agent
| | | |
+--------+--------+--------+--------+
|
Shared Research State
|
+---------------+------------------+
| |
PostgreSQL FAISS
|
LLM Provider

```

---

# Architecture Layers

## 1. Presentation Layer

Technology

- Next.js
- JavaScript
- Tailwind CSS

Responsibilities

- User Interface
- Authentication Screens
- Research Dashboard
- Chat Interface
- File Upload
- Report Viewer

The frontend never communicates directly with the LLM.

All communication goes through the FastAPI backend.

---

## 2. API Layer

Technology

- FastAPI

Responsibilities

- Authentication
- Request Validation
- Route Handling
- Response Formatting
- Error Handling

The API layer should remain thin.

Business logic must never be implemented inside route handlers.

---

## 3. Service Layer

The service layer contains the application's business logic.

Services include:

- Authentication Service
- Research Service
- Document Service
- Report Service

Responsibilities

- Coordinate workflows
- Validate business rules
- Interact with repositories
- Invoke AI workflows

---

## 4. AI Layer

Technology

- LangGraph

Responsibilities

- Execute agent workflows
- Manage shared state
- Coordinate AI agents

The AI layer is isolated from business logic.

Agents should not know about:

- FastAPI
- PostgreSQL
- HTTP Requests
- User Authentication

---

## 5. Data Layer

Technologies

- PostgreSQL
- FAISS

Responsibilities

PostgreSQL

- Users
- Research Sessions
- Reports
- Conversations
- Metadata

FAISS

- Vector Embeddings
- Semantic Search
- Similarity Retrieval

---

# Agent Architecture

The MVP contains four agents.

## Planner Agent

Responsibilities

- Understand user intent
- Create research plan
- Define execution strategy

Input

User Question

Output

Research Plan

---

## Search Agent

Responsibilities

- Search external information
- Retrieve supporting evidence

Input

Research Plan

Output

Relevant Sources

---

## Retrieval Agent

Responsibilities

- Search uploaded documents
- Retrieve relevant chunks

Input

Research Plan

Output

Document Context

---

## Report Agent

Responsibilities

- Combine retrieved information
- Generate final response
- Create citations
- Produce structured report

Input

Research Context

Output

Research Report

---

# Shared Research State

The agents communicate using a shared state managed by LangGraph.

The shared state may contain:

- Original Query
- Research Plan
- Search Results
- Retrieved Documents
- Intermediate Notes
- Final Report

No agent communicates directly with another agent.

All communication occurs through the shared state.

---

# LLM Abstraction

The system shall never call an LLM directly from an agent.

Instead:

Planner Agent

↓

LLM Service

↓

Gemini / Ollama / OpenRouter

This allows the project to switch providers without modifying agent logic.

---

# Prompt Management

Prompts are stored as separate Markdown files.

Example

prompts/

planner.md

search.md

report.md

No prompts should be hardcoded inside Python files.

---

# Design Principles

The architecture follows these principles:

- Separation of Concerns
- Single Responsibility Principle
- Modular Components
- Replaceable LLM Providers
- Stateless APIs
- Extensible Agent Framework

---

# Future Scalability

Future versions may introduce:

- Verification Agent
- Memory Agent
- Citation Agent
- Workspace Support
- Background Jobs
- Redis Cache
- Streaming Responses
- Analytics
- Monitoring

The MVP architecture already supports these additions.

---

# Engineering Decisions

Decision 1

The frontend communicates only with the FastAPI backend.

Reason

Prevents direct exposure of AI providers.

---

Decision 2

Business logic is separated from API routes.

Reason

Improves maintainability.

---

Decision 3

Agents communicate through shared state rather than directly.

Reason

Simplifies orchestration and debugging.

---

Decision 4

LLM providers are abstracted behind an LLM service.

Reason

Allows switching between Ollama, Gemini, and future providers with minimal code changes.

---

Decision 5

Prompts are stored outside the application code.

Reason

Prompt engineering should not require source code modifications.