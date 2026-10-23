# Architecture Harness

A fork-ready, agent-assisted method for taking a cloud solution from an initial scenario to an evidence-backed design, target architecture, implementation-ready handoff, sizing model, operating model, and decision presentation.

The harness is product-independent through logical design and Microsoft-cloud-ready during architecture mapping. Microsoft Fabric, Databricks, AKS, Azure Container Apps, API Management, Event Hubs, Service Bus, Microsoft 365, Copilot, Copilot Studio, and Microsoft Entra ID are candidates, not defaults. Material product choices require evidence and an architecture decision record (ADR).

## Who this is for

Use the harness when a project needs to:

- turn an incomplete business or technical scenario into a governed architecture;
- keep business outcomes, requirements, design, products, downstream implementation, operations, and evidence connected;
- evaluate cloud platforms without selecting products before requirements are understood;
- make security, resilience, sizing, cost, deployment, and operations part of the architecture process;
- revisit only the affected work when an input, assumption, dependency, or decision changes; and
- prepare clear readiness and investment decisions without overstating prototype evidence.

The repository is a starter, not a completed reference architecture. A new project is expected to replace placeholders, add domain-specific requirements, and assign real owners and decision authorities.

## What the harness contains

- Eight phase folders from framing through presentation.
- One plan per phase with tasks, dependencies, completion checks, status, evidence, and replay rules.
- G0-G7 readiness gates.
- Stable identifiers and canonical ownership rules.
- Change-impact and task-level replay.
- An ADR process and reusable ADR template.
- Registers for assumptions, requirements, risks, gates, external evidence, sizing, planned tests, and claims.
- A final architecture-validated scenario linking business outcomes to realization, products, effort, cloud cost, operations, and evidence.
- GitHub Copilot custom agents and portable agent skills.
- A manifest-driven validator and GitHub Actions workflow.

## Quick start

### Browse the harness as a site

The repository can publish a navigable documentation site with GitHub Pages. The site is assembled from the canonical phase Markdown and agent guides; generated `docs/` and `site/` directories are not source artifacts.

To preview locally:

```bash
python scripts/prepare_pages.py
python -m pip install -r requirements-pages.txt
python -m mkdocs serve
```

Open the local URL printed by MkDocs, normally `http://127.0.0.1:8000/`.

To publish a fork, enable **Settings > Pages > Build and deployment > GitHub Actions**. The workflow in `.github/workflows/pages.yml` builds and deploys on pushes to `main` and on manual dispatch. Repository administration permissions may be required to enable Pages.

### 1. Fork and clone

Fork this repository, clone the fork, and create a project branch:

```bash
git clone https://github.com/<your-account>/<your-project>.git
cd <your-project>
git switch -c project/initial-framing
```

Do not fill every template immediately. Start with the source scenario and let the phase plans identify the next dependency-ready work.

### 2. Add the source scenario

Open [00-framing/03-scenario.md](00-framing/03-scenario.md) and record:

- each source and its provenance;
- the current situation and desired change;
- known stakeholders and decision authorities;
- organizational, data, system, environment, and jurisdictional boundaries; and
- missing information as open questions.

Preserve supplied source wording where material. Put interpretations and unverified beliefs in [00-framing/02-assumptions.md](00-framing/02-assumptions.md), not in the source record.

### 3. Start with the Program Orchestrator

In a supported GitHub Copilot agent surface, select **Program Orchestrator** and use:

```text
Assess this new project. Read the framing sources, governance, phase plans,
open changes, and gate register. Identify the smallest dependency-ready task,
its owner, required output, completion check, and evidence.
```

Continue with the same Program Orchestrator conversation while it routes bounded work to the specialist agents. The repository uses agents and skills rather than VS Code-only prompt files so the workflow remains portable across supported agent surfaces.

### 4. Execute one bounded task

Use the specialist selected by the Program Orchestrator. For example:

```text
Preparation Foundation: build the G0 framing package from the supplied scenario.
Do not select products or invent owners, facts, evidence, or approval.
```

Update the task row in the owning phase plan:

- `Not started`
- `Ready`
- `Blocked`
- `In progress`
- `Replay required`
- `Complete with evidence`

A task is complete only when its completion check is met and its evidence is linked.

### 5. Validate before review

Run:

```bash
python3 scripts/validate_harness.py
```

The validator checks required artifacts, phase and gate consistency, controlled statuses, agent and skill metadata, identifier namespaces, local links and anchors, path casing, and task-table structure. The same validation runs in GitHub Actions.

## How the lifecycle works

The phases are progressive but not strictly sequential.

| Phase | Main outcome | May start after | Exit gate requires | Exit gate |
|---|---|---|---|---|
| [00-framing](00-framing/) | Source-grounded vision, assumptions, scenario, and goals | Project input | Framing criteria | G0 |
| [01-preparation](01-preparation/) | Objectives, scope, deliverables, governance, and execution baseline | G0 | G0 | G1 |
| [02-design](02-design/) | Product-independent logical design and measurable requirements | G1 | G1 | G2 |
| [03-architecture](03-architecture/) | Capabilities, buy/build realization, required products, topology, dependencies, NFRs, and decisions | G2 | G2 | G3 |
| [04-implementation](04-implementation/) | Implementation plan, stories, building blocks, code-generation context, and engineering handoff | G3 | G3 | G4 |
| [05-sizing](05-sizing/) | Delivery effort, workload and cloud-cost model, observability requirements, and sizing validation plan | G2 | G3 and G4 | G5 |
| [06-operations](06-operations/) | Operating model, procedure requirements, rollout, support, security operations, and continuity plans | G1 | G3, G4, and G5 | G6 |
| [07-presentation](07-presentation/) | Architecture-validated scenario, traceable evidence, and decision story | G0 | G1-G6 | G7 |

The distinction is important:

- `mayStartAfter` identifies when useful work can begin.
- `exitGateRequires` identifies the prior gates required before the phase exit gate can be accepted.

This permits early work on cost, operating responsibilities, and presentation evidence without claiming those phases are ready.

## Architecture-to-engineering boundary

The harness stops at an implementation-ready handoff.

It creates:

- an implementation plan and sequenced backlog;
- user stories and acceptance scenarios;
- functional building-block specifications;
- environment, prototype/spike, release, deployment, migration, and test plans;
- code-generation context packages;
- workload, capacity, cost, and observability models;
- an operating model and operational-readiness plan; and
- a versioned handoff to a named downstream repository or engineering team.

It does not create:

- application or infrastructure code;
- executable tests or pipelines;
- cloud resources or deployments;
- generated build or release artifacts;
- executed prototypes, performance tests, or recovery exercises; or
- implementation-complete, production-ready, or operating-effectiveness claims.

The downstream implementation workflow owns execution. It returns material architecture conflicts, failed assumptions, new decisions, and relevant evidence through [04-implementation/49-implementation-handoff.md](04-implementation/49-implementation-handoff.md), [01-preparation/16-change-impact-register.md](01-preparation/16-change-impact-register.md), and [01-preparation/19-external-evidence-register.md](01-preparation/19-external-evidence-register.md).

## Ultimate delivery

The default final delivery is [07-presentation/76-validated-scenario.md](07-presentation/76-validated-scenario.md). Its definition, matrix, assessment states, and limitations are canonical; it integrates scenario outcomes, realization, products or custom build, effort, cloud cost, ownership, and external evidence without claiming implementation.

## Phase-by-phase usage

### 00 - Framing

**Goal:** understand the problem before designing a solution.

1. Capture source material and limitations in [00-framing/03-scenario.md](00-framing/03-scenario.md).
2. Record unverified beliefs in [00-framing/02-assumptions.md](00-framing/02-assumptions.md).
3. Define the mission, future state, principles, and non-goals in [00-framing/01-vision.md](00-framing/01-vision.md).
4. Define measurable or explicitly unmeasured value in [00-framing/04-business-goals.md](00-framing/04-business-goals.md).
5. Use [00-framing/00-framing-plan.md](00-framing/00-framing-plan.md) to assess G0 readiness.

Recommended agent: **Preparation Foundation**.

Do not select cloud products in this phase. A product named in a supplied source remains source context, not an accepted architecture.

### 01 - Preparation

**Goal:** establish the controlled project baseline.

1. Turn the scenario into a stakeholder and change narrative.
2. Define measurable objectives and measurement gaps.
3. Classify scope as in scope, out of scope, deferred, or experimental.
4. Define deliverables with observable acceptance and evidence.
5. Assign accountable roles or retain explicit role placeholders.
6. Baseline governance, identifiers, risk, change, and gate handling.

The core control artifacts are:

- [01-preparation/15-governance.md](01-preparation/15-governance.md)
- [01-preparation/16-change-impact-register.md](01-preparation/16-change-impact-register.md)
- [01-preparation/17-gate-register.md](01-preparation/17-gate-register.md)
- [01-preparation/18-risk-register.md](01-preparation/18-risk-register.md)

Recommended agents: **Preparation Foundation** and **Program Orchestrator**.

### 02 - Design

**Goal:** define how the solution must behave without preselecting products.

Use [02-design/21-high-level-design.md](02-design/21-high-level-design.md) for the cross-domain model and the files under [02-design/domains](02-design/domains/) for bounded concerns:

- data model and data-platform behavior;
- platform concept;
- integration patterns;
- application and AI experience;
- operating model;
- resilience; and
- security.

Record product-independent functional, design, and non-functional requirements in [02-design/23-requirements-and-acceptance.md](02-design/23-requirements-and-acceptance.md).

Recommended agent: **Solution Design Partner**.

Raise a decision question when the design reaches a material trust, data, platform, runtime, integration, security, resilience, cost, or portability choice. Do not hide that choice in a diagram.

### 03 - Architecture

**Goal:** map the accepted logical design to deployable cloud products and operating arrangements.

1. Define enterprise capabilities in [03-architecture/31-enterprise-capabilities.md](03-architecture/31-enterprise-capabilities.md).
2. Reconcile product-independent functional domains.
3. Compare credible products and patterns against mandatory constraints.
4. Define target topology, environments, regions, networks, identities, data locations, management planes, and ownership.
5. Record functional and delivery dependencies.
6. Map NFRs to architecture mechanisms, telemetry, and validation.
7. Resolve implementation-blocking choices through ADRs.
8. Map every capability to buy, configure, build, reuse, integrate, or retire in [03-architecture/37-capability-realization.md](03-architecture/37-capability-realization.md).
9. Identify every required product, service, tier, license, custom building block, owner, cost driver, and exit consideration.

Recommended agents:

- **Architecture Partner** for target mapping and topology.
- **ADR Proposal Partner** for material choices.
- **Cloud Security Reviewer** for a read-only threat-led review.
- **Sizing and FinOps Partner** for the indicative G3 estimate.

Microsoft cloud services in the templates are candidates. Select them only when their capabilities, limits, region, identity, networking, availability, lifecycle, support, licensing, cost, and portability fit the accepted requirements.

### 04 - Implementation planning and handoff

**Goal:** provide downstream engineering and code-generation workflows with complete, bounded, traceable implementation context.

1. Convert accepted scope and decisions into the implementation backlog.
2. Define user stories and functional building blocks.
3. Plan environment prerequisites and security guardrails.
4. Frame prototypes and spikes for material uncertainty.
5. Specify release, deployment, migration, rollback, and supply-chain automation requirements.
6. Define planned tests, success criteria, expected evidence, and downstream owners.
7. Create bounded code-generation contexts in [04-implementation/46-code-generation-context.md](04-implementation/46-code-generation-context.md).
8. Assemble the implementation package in [04-implementation/49-implementation-handoff.md](04-implementation/49-implementation-handoff.md).

Recommended agent: **Engineering Manager**.

The Engineering Manager edits plans and context only. It must not generate code, provision environments, run pipelines, execute tests, or claim downstream results. If engineering later discovers that an assumption or architecture decision is wrong, the handoff routes the finding back through change-impact replay.

### 05 - Sizing

**Goal:** replace unbounded delivery and architecture guesses with traceable effort, capacity, cloud/service cost ranges, confidence, observability requirements, and downstream validation plans.

Sizing has two passes:

1. **Architecture model:** build workload assumptions and compare candidate capacity and cost ranges.
2. **Delivery effort:** estimate low/base/high person-days, role demand, delivery waves, elapsed-time drivers, contingency, and optional labor cost.
3. **Validation plan:** define the downstream tests and evidence needed to calibrate the model.
4. **External calibration:** update assumptions and confidence when cited implementation or performance evidence becomes available.

Include steady, peak, burst, seasonal, growth, retention, retry, replay, failure, recovery, redundancy, non-production, observability, security, licensing, support, and network effects where relevant.

Recommended agent: **Sizing and FinOps Partner**.

Never hide delivery-capacity assumptions, list prices, negotiated discounts, commitment models, labor-rate treatment, currency, region, retrieval date, uncertainty, exclusions, or the absence of measured evidence. G5 approves effort, sizing, cost, and validation models, not a delivery or spend commitment.

### 06 - Operations

**Goal:** define how accountable teams should operate, secure, change, recover, and retire the service, and how readiness will be validated downstream.

1. Assign service, product, engineering, data, security, support, and vendor responsibilities.
2. Specify automation requirements for frequent and high-risk procedures, including authorization, safety checks, rollback, and expected evidence.
3. Define identity, vulnerability, threat, incident, secret, key, certificate, data, and supply-chain operating processes.
4. Define rollout waves, migration, coexistence, validation, hypercare, rollback, and decommissioning.
5. Plan incident response, backup, restore, failover, reduced-capacity, and continuity exercises with success criteria and downstream owners.

Recommended agents:

- **Operations Readiness Partner**
- **Cloud Security Reviewer**
- **Engineering Manager** for implementation-handoff and automation requirements

A written runbook or exercise plan is designed content. G6 confirms that the operating model and readiness plan are complete; it does not prove that procedures or recovery work in production.

### 07 - Presentation

**Goal:** prepare a decision package that is accurate at executive and technical altitude.

1. State the audience, decision authority, requested decision, alternatives, and consequence of delay.
2. Register every material claim in [07-presentation/75-claim-and-evidence-register.md](07-presentation/75-claim-and-evidence-register.md).
3. Build the business-value story.
4. Simplify the accepted architecture and functional views without changing their meaning.
5. Explain ownership, rollout, support, security, cost, resilience, and remaining gaps.
6. Assemble the architecture-validated scenario across G1-G6.
7. Review claims, timing, accessibility, objections, and distribution constraints.

Recommended agent: **Program Orchestrator**, with the phase owners reviewing claims sourced from their artifacts.

Never repair an upstream inconsistency only in the presentation. Correct the canonical source and replay the affected claim.

## Using the agents

Start with **Program Orchestrator** and let it route bounded work to the specialist owner. The complete roster, ownership, handoffs, and collaboration rules are maintained in [AGENTS.md](AGENTS.md).

### Agent tool policy

The harness is repository-first:

- All agents read canonical artifacts and use repository search before seeking external information.
- No custom agent has command-execution access.
- Only **ADR Proposal Partner** and **Sizing and FinOps Partner** have web access.
- ADR web access is restricted to current, material product, service, region, quota, lifecycle, security, support, licensing, or standards evidence missing from the repository.
- Sizing web access is restricted to current pricing, meters, SKUs, licensing, commercial terms, regions, and service limits missing from the repository.
- Web-enabled agents use authoritative sources, record URL/date/finding/limitation, and never submit repository or sensitive content in an external query.
- **Cloud Security Reviewer** is read-only.

The machine-readable policy lives in [architecture-harness.json](architecture-harness.json), and the validator rejects excessive agent permissions.

### Example agent prompts

Start or resume the program:

```text
Assess the current repository state. Identify open changes, blocked assumptions,
ready tasks, missing evidence, and the next recommended phase task.
```

Develop one design concern:

```text
Design the event-driven integration concern for REQ-012.
Cover normal, duplicate, delayed, unauthorized, failed dependency, replay,
and recovery behavior. Keep the design product-independent and identify ADRs.
```

Map a target architecture:

```text
Map the accepted integration design to credible Azure service alternatives.
Compare Event Hubs, Service Bus, and other relevant patterns against ordering,
delivery, replay, throughput, identity, network, operations, cost, and exit needs.
Do not accept the decision.
```

Define capability realization:

```text
For every in-scope capability, define whether it is bought, configured, built,
reused, integrated, or retired. Identify required products, tiers, licenses,
custom functional building blocks, ADRs, dependencies, operating owners,
effort inputs, cloud-cost drivers, and unresolved gaps.
```

Plan implementation:

```text
Convert the accepted vertical slice into an implementation-ready handoff.
Define user stories, functional building blocks, dependencies, guardrails,
environment and release plans, code-generation contexts, planned tests,
expected evidence, receiving repository, and change-feedback path.
Do not generate code or execute implementation.
```

Prepare a gate:

```text
Prepare the G3 readiness recommendation. Assess every criterion against current
evidence, distinguish designed from demonstrated behavior, and leave the actual
gate decision to the named authority.
```

Assemble the final delivery:

```text
Build the architecture-validated scenario. Trace every in-scope scenario step
to objectives, behavior, capabilities, realization strategy, required products
or custom building blocks, delivery effort, cloud/service cost, operating
ownership, external evidence, and explicit conditions. Do not claim that the
scenario has been implemented.
```

## Day-to-day task workflow

For every task:

1. Read [architecture-harness.json](architecture-harness.json), governance, the owning phase plan, direct inputs, open changes, and relevant gate record.
2. Confirm the phase `mayStartAfter` condition and direct task dependencies.
3. Set the task to `Ready` or `Blocked`.
4. Assign the accountable role and expected output.
5. Define completion and evidence before authoring.
6. Set the task to `In progress`.
7. Update the canonical artifact first.
8. Update summaries, links, plans, and registers only when needed.
9. Run the smallest relevant validation.
10. Link evidence and set `Complete with evidence`, or record the exact blocker.

Do not mark a task complete because its file exists.

## Canonical ownership and evidence

Each material statement has one owner:

```text
source or assumption
  -> goal, objective, and scope
  -> requirement and design
  -> capability, architecture, and ADR
  -> implementation item, building block, context, and planned test
  -> external evidence or explicit evidence gap
  -> presentation claim
```

Other artifacts summarize and link rather than copy the detail.

Use the evidence classes consistently:

| Class | Meaning |
|---|---|
| Source fact | Directly supported by a cited source |
| Assumption | Unverified and assigned a validation action |
| Target | Desired measurable state, not an achieved result |
| Proposal | Candidate direction awaiting decision |
| Accepted decision | Choice recorded by the named authority |
| Designed | Specified but not executed |
| Demonstrated | Executed under stated conditions by a cited downstream or external source |
| Operational evidence | Observed in the intended live operating context by a cited external source |
| Future commitment | Planned work with ownership and dependencies |

## Architecture decisions

Use [03-architecture/36-architecture-decision-process.md](03-architecture/36-architecture-decision-process.md) when a choice:

- changes a trust, tenant, organization, region, jurisdiction, data, identity, or decision-authority boundary;
- selects a strategic platform, store, runtime, AI model, integration, security, deployment, or operating pattern;
- materially affects security, privacy, reliability, performance, scale, cost, portability, or operations;
- creates long-lived coupling, migration cost, concentration, duplication, or debt; or
- establishes an exception or supersedes an accepted decision.

To create an ADR:

1. Add a decision question to [03-architecture/decisions/README.md](03-architecture/decisions/README.md).
2. Copy [03-architecture/decisions/adr-template.md](03-architecture/decisions/adr-template.md).
3. Compare at least two credible alternatives and retain, defer, or do nothing when meaningful.
4. Evaluate mandatory constraints before weighted preferences.
5. Record current evidence, limitations, consequences, implementation conditions, validation, fallback, and revisit triggers.
6. Keep `## Decision` empty while the ADR is `Proposed`.
7. Let only the named decision authority set `Accepted`, `Rejected`, or `Deferred`.
8. Propagate the decision to affected design, architecture, backlog, tests, sizing, operations, risks, and claims.

Never rewrite an accepted ADR to fit a later choice. Create a new ADR and supersede the old one after the new decision is accepted.

## Responding to changed inputs

Do not restart the entire project when an input changes.

1. Add a `CHG-NNN` row to [01-preparation/16-change-impact-register.md](01-preparation/16-change-impact-register.md).
2. Record the canonical source, old meaning, and new meaning.
3. Follow direct identifiers and links.
4. Identify affected tasks, decisions, tests, evidence, risks, estimates, procedures, gates, and claims.
5. Mark only affected tasks `Replay required`.
6. Update the canonical source first.
7. Re-run the affected tasks in dependency order.
8. Revalidate evidence and reassess impacted gates.
9. Close the change after affected owners review the reconciliation.

Example:

```text
The transaction peak assumption changed from 500 to 2,000 events per second.
Assess the impact, create CHG-NNN, identify the smallest replay set, and list
the NFRs, ADRs, sizing tests, costs, operating procedures, and gates to recheck.
```

Preserve unaffected accepted work and historical gate decisions.

## Running a gate review

A gate is a human decision supported by evidence, not an automated status and not a document-completeness check.

For G0-G7:

1. Read the phase exit criteria.
2. Verify the manifest's `exitGateRequires`.
3. Check open changes, assumptions, ADRs, dependencies, risks, tests, and evidence.
4. Classify criteria as ready, ready with conditions, blocked, not evidenced, or not applicable with rationale.
5. Record a readiness recommendation in [01-preparation/17-gate-register.md](01-preparation/17-gate-register.md).
6. Leave the decision, authority, and date unchanged until the actual authority acts.
7. Append the real outcome to the gate decision history.

Agents can prepare recommendations. They cannot invent approval or accepted residual risk.

## Identifiers

Use stable identifiers to connect artifacts. Common examples are:

- `SCN-001`, `ASM-003`, `GOAL-001`, `OBJ-001`, and `SCP-001`
- `REQ-001`, `DES-001`, `NFR-001`, and `CAP-001`
- `REAL-001`, `PROD-001`, `ADR-001`, `RISK-001`, and `DEP-001`
- `IMP-001`, `FBB-001`, `CTX-001`, and `HND-001`
- `EFF-001`, `COST-001`, `EVID-001`, and `CLAIM-001`
- `TASK-DES-01`, `TASK-ARC-01`, and other phase task IDs
- `TEST-IMP-001`, `TEST-SIZE-001`, and `TEST-OPS-001`

The complete registry is in [architecture-harness.json](architecture-harness.json). Do not renumber accepted records or reuse retired decision IDs.

## Customizing a fork

Safe customizations include:

- replacing the Microsoft cloud candidate list with another cloud ecosystem;
- adding domain-specific design artifacts under the owning phase;
- adding assurance, privacy, regulatory, safety, or model-risk roles and artifacts;
- extending identifier prefixes in [architecture-harness.json](architecture-harness.json);
- adding specialist agents or skills for recurring project workflows; and
- adding specialist context templates for downstream repositories without adding their source, infrastructure, pipelines, or executable tests.

When adding or removing a required starter artifact:

1. identify its canonical owner;
2. update the owning phase plan;
3. update `requiredArtifacts` or `optionalArtifacts` in [architecture-harness.json](architecture-harness.json);
4. update links and agent instructions;
5. run the validator; and
6. document any changed gate or replay behavior.

Avoid creating a root document when a phase folder already owns the content.

The prototype/spike template and the separate presentation pattern, functional, and operating-model views are optional. A fork may remove them without failing validation; the phase plans retain their optional handoff points.

## Working without GitHub Copilot

The harness does not require an AI agent. A team can use the same process manually:

1. select the next ready task from the phase plan;
2. assign the accountable role;
3. update the canonical artifact;
4. review against the completion check;
5. attach review evidence, expected evidence, or cited external evidence;
6. run validation; and
7. prepare the gate recommendation.

Agents accelerate discovery, consistency checking, and drafting. Human owners remain responsible for facts, architecture decisions, risk acceptance, and gates.

## Repository map

```text
.github/
  agents/       Role-based Copilot agents
  skills/       Portable architecture workflows
  workflows/    Harness validation
00-framing/     Vision, assumptions, scenario, and goals
01-preparation/ Objectives, scope, governance, changes, gates, and risks
02-design/      Product-independent design and requirements
03-architecture/Capabilities, realization, products, topology, NFRs, and ADRs
04-implementation/Planning, stories, building blocks, contexts, and handoff
05-sizing/      Delivery effort, workload/cloud cost, and validation plan
06-operations/  Operating model, procedure specifications, rollout, continuity
07-presentation/Validated scenario, value, architecture, operations, and claims
scripts/        Repository validation
```

## Deliberate limits

This starter does not contain:

- a preselected reference architecture;
- production-ready infrastructure or application code;
- approved owners, accepted decisions, or gate outcomes;
- legal, regulatory, privacy, or compliance conclusions;
- production data, credentials, or cloud configuration;
- demonstrated test, scale, resilience, cost, or operating evidence; or
- a promise that every project needs every candidate technology.

Add project-specific assurance and delivery controls when the scenario, industry, data, jurisdictions, organization, or risk profile requires them.
