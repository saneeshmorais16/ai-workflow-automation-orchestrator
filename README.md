# AI Workflow Automation Orchestrator

**A local-first applied AI platform that turns ambiguous synthetic business requests into structured, risk-aware and human-reviewable workflow plans.**

## Why AI workflow orchestration matters

Automation without controls can make mistakes faster. Useful AI workflow systems must expose their plans, dependencies, routing rationale, approval gates and history. This portfolio project demonstrates those engineering patterns without triggering real actions or claiming production readiness.

## Problem statement

Messy requests such as “handle refunds safely” omit owners, dependencies, risk controls and approval boundaries. The orchestrator converts that intent into a typed workflow, structured task graph, risk assessment, approval state, team route, simulation and audit trail.

## Architecture

```text
Messy business request
      |
      v
Workflow classifier
      |
      v
Task planner
      |
      v
Risk + approval engine
      |
      v
Routing recommendation
      |
      v
Workflow simulator
      |
      v
Audit trail + dashboard
```

## Core features

- Typed workflow intake with priority, requester and business area
- Explainable rule-based classification across nine workflow categories
- Dependency-aware task planning with owner roles and approval markers
- Low/Medium/High/Critical risk scoring and explicit risk signals
- Guarded Draft/Needs Review/Approved/Rejected/Escalated decisions
- Team routing with a human-readable rationale
- Safe automation recommendations labelled `simulation_only`
- Progress simulation, immutable timeline events and SQLite audit records
- Seven-case regression evaluation, FastAPI/OpenAPI, dark operations dashboard, tests and CI

## Classification and task planning

Keyword evidence maps each request to Support Triage, Report Approval, Refund Review, HR Onboarding, IT Access Request, AI Risk Review, Data Quality Review, Document Processing or General Automation. Each class selects an inspectable task template with stable IDs, owners, dependencies, priorities and approval gates. The default planner is deterministic and requires no LLM.

## Risk and approval engine

The engine detects financial action, customer impact, personal data, access permission, compliance sensitivity, AI-generated decisions and ambiguity. Weighted signals produce a risk level and an approval requirement. High-impact actions remain behind explicit human decisions.

## Routing

Classification selects the relevant team—Support, Finance, HR, IT, Data, AI Governance, Manager Review or General Operations—and records why. Critical workflows route to manager oversight before domain processing.

## Audit trail

Intake, classification, planned task count, risk score, routing, approval decisions, reviewer notes and every simulated status transition are timestamped in SQLite and returned with the full workflow record.

## Evaluation strategy

Synthetic golden cases verify classification, planning completeness, risk level, routing and approval detection. The regression gate passes only when every check in every case succeeds. API tests also confirm workflow creation, timeline state, audit creation and dashboard aggregation.

## Example request

> Review AI system risk, model decision oversight, personal data sensitivity and compliance before approval.

## Example generated plan

```json
{
  "workflow_type": "AI Risk Review",
  "risk_level": "High",
  "approval_required": true,
  "route_to": "AI Governance Team",
  "tasks": [
    {"task_name": "Review system purpose", "owner_role": "AI Governance Reviewer", "requires_approval": false},
    {"task_name": "Check data sensitivity", "owner_role": "Data Owner", "requires_approval": true},
    {"task_name": "Confirm human oversight control", "owner_role": "Product Owner", "requires_approval": true}
  ],
  "audit_status": "workflow_plan_created"
}
```

## Example audit output

```json
[
  {"action": "intake", "details": "Synthetic workflow request recorded"},
  {"action": "classification", "details": "AI Risk Review"},
  {"action": "planned_tasks", "details": "3 tasks"},
  {"action": "risk_score", "details": "84"},
  {"action": "routing_decision", "details": "Manager Review"}
]
```

## API endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Confirm local simulation mode |
| POST | `/workflows` | Create a synthetic workflow request |
| GET | `/workflows` | List workflows |
| GET | `/workflows/{workflow_id}` | Full plan, timeline and audit |
| POST | `/workflows/{workflow_id}/plan` | Generate plan, risk and route |
| POST | `/workflows/{workflow_id}/approve` | Record approval with note |
| POST | `/workflows/{workflow_id}/reject` | Record rejection with note |
| POST | `/workflows/{workflow_id}/escalate` | Escalate with note |
| POST | `/workflows/{workflow_id}/simulate` | Advance simulated status |
| GET | `/dashboard` | Aggregate status/risk metrics |
| POST | `/evaluate` | Run regression suite |

## Setup and local use

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Open `http://127.0.0.1:8000`; interactive API documentation is at `/docs`. Alternatively run `uvicorn app.main:app --reload`.

## Tests

```bash
pytest -q
```

Tests cover classification, planning, risk, approvals, routing, simulation, audit shape, workflow creation, dashboard metrics, API health and evaluation. GitHub Actions runs them on pushes and pull requests.

## Screenshot/demo

> Add a local dashboard screenshot or short GIF here.

## Privacy and safety

All workflows, names and events are synthetic. The system sends no email, calls no external business API and triggers no real automation. `.env`, keys, databases, logs, private documents and real workflow/customer/email folders are excluded. LLM settings are blank and disabled by default. Every recommendation is inspectable and human-reviewable.

## Limitations

Rules and templates do not understand every phrasing; risk scores are transparent heuristics rather than calibrated probabilities. Simulation is intentionally not an execution engine. Authentication, tenancy, queues, distributed scheduling, connectors and production controls are out of scope. No real clients, deployment or commercial use is claimed.

## Future improvements

Add a visual DAG editor, configurable policy packs, SLA simulation, task retries, role-based access, signed audit exports, OpenTelemetry traces, calibrated risk models, local-model planning, and disabled-by-default connector adapters with dry-run enforcement.
