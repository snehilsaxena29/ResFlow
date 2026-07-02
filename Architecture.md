
                 Frontend (Next.js)

                        │

                  FastAPI Backend

                        │

                Agent Orchestrator
                 (LangGraph)

                        │
 ┌────────────┬──────────────┬─────────────┐
 │            │              │             │
Planner     Search        Retrieval     Report
 Agent       Agent          Agent       Generator
 │            │              │             │
 └────────────┴──────────────┴─────────────┘

                Shared Memory & State

                   PostgreSQL

                 Vector Database

                Local / Cloud LLM


                     User
                      │
                      ▼
            Query Understanding
                      │
                      ▼
              Planner Agent
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 Search Agent               Document Agent
        │                           │
        └─────────────┬─────────────┘
                      ▼
           Verification Agent
                      ▼
            Summarization Agent
                      ▼
          Report Generation Agent
                      ▼
              Final Response


### Layer 1 — AI Core
Multi-agent orchestration
Prompt management
LLM abstraction
RAG
Memory
### Layer 2 — Platform
Authentication
Projects/workspaces
Research history
File management
Reports
Settings
### Layer 3 — User Experience
Modern dashboard
Streaming responses
Agent activity timeline
Report viewer
Citations
Progress tracking

#### This separation has two advantages:
It's easier to extend in the future (e.g., add a Resume Analyzer or Legal Assistant).
It gives you a great architecture story to tell in interviews.