# Project Status

## Build status
Complete for the requested local portfolio scope; deterministic operation requires no paid API.

## Completed features
Intake, nine-way classification, dependency-aware task plans, risk/approval controls, explained routing, simulation-only automation recommendations, status simulation, SQLite timeline and audit records, regression evaluation, requested API, dashboard, tests and CI.

## Testing status
Run `pytest -q`; the final result is recorded during the publication safety gate.

## Known limitations
Rule/template coverage is finite; risk values are heuristic; no real scheduler, connector, authentication or production hardening is provided.

## Safety boundaries
Synthetic workflows only. No emails, API calls or real automations. Every recommendation is human-reviewable. No production, client, enterprise or commercial claims.

## Files excluded from Git
Environment files, credentials, databases, logs, PDFs, caches, virtual environments, dependencies, builds, generated outputs, uploads, private data/documents, real company workflows, real customers and real emails.

## Before making public
Run tests and evaluation; scan for credentials and private data; inspect staged files; confirm examples are synthetic; verify no trigger code exists; review README claims; create privately before changing visibility.
