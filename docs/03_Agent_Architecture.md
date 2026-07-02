# Agent Architecture

**Version:** 1.0
**Status:** Approved
**Last Updated:** July 2026

---

# Purpose

This document defines the architecture, responsibilities, and communication model for the AI agents used in ResearchFlow AI.

The MVP consists of four specialized agents.

Each agent performs exactly one responsibility.

---

# Design Philosophy

ResearchFlow AI follows a multi-agent architecture.

Instead of asking one LLM to perform every task, multiple specialized agents collaborate to solve the research problem.

Each agent:

- Has a single responsibility
- Receives structured input
- Produces structured output
- Never communicates directly with another agent
- Uses shared workflow state

---

# Agent Communication

```
User

↓

Planner Agent

↓

Search Agent

↓

Retrieval Agent

↓

Report Agent

↓

Final Report
```

Agents exchange information through the shared LangGraph state.

Direct communication between agents is prohibited.

---

# Planner Agent

## Purpose

Understand the user's research request and create an execution plan.

---

## Responsibilities

- Analyze user intent
- Break research into smaller tasks
- Define execution order
- Create research objectives

---

## Input

- User Query

---

## Output

- Research Plan

Example

```text
Topic

Comparison of LangGraph vs CrewAI

Objectives

- Compare architecture
- Compare scalability
- Compare learning curve
- Recommend use cases
```

---

## Allowed Tools

- LLM Provider

---

## Forbidden

- Web Search
- Vector Search
- Report Generation

---

# Search Agent

## Purpose

Retrieve information from external sources.

---

## Responsibilities

- Search web
- Rank useful information
- Return structured results

---

## Input

Research Plan

---

## Output

Search Results

---

## Allowed Tools

- Search API
- LLM

---

## Forbidden

- Report Generation
- Document Retrieval

---

# Retrieval Agent

## Purpose

Search uploaded documents.

---

## Responsibilities

- Query vector database
- Retrieve document chunks
- Return citations

---

## Input

Research Plan

---

## Output

Relevant Document Chunks

---

## Allowed Tools

- FAISS

---

## Forbidden

- Web Search
- Report Generation

---

# Report Agent

## Purpose

Generate the final research report.

---

## Responsibilities

- Combine all context
- Write structured report
- Generate citations
- Produce markdown

---

## Input

Research Plan

Search Results

Retrieved Documents

---

## Output

Research Report

---

## Allowed Tools

- LLM

---

## Forbidden

- Web Search
- Vector Search

---

# Shared State

The workflow state contains:

- User Query
- Research Plan
- Search Results
- Retrieved Documents
- Intermediate Notes
- Final Report

Every agent can read and update only the fields relevant to its responsibility.

---

# Error Handling

Each agent should:

- Validate input
- Return structured errors
- Avoid crashing the workflow

If an agent fails, the workflow should stop gracefully with an appropriate error message.

---

# Future Agents

Future versions may introduce:

- Verification Agent
- Citation Agent
- Memory Agent
- Evaluation Agent
- Reflection Agent
- Critic Agent

These additions should not require changes to existing agents.

---

# Engineering Principles

Every agent should satisfy the following:

- Single Responsibility Principle
- Modular Design
- Replaceable Implementation
- Stateless Execution
- Structured Inputs
- Structured Outputs