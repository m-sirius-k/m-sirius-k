# MoCKA Ecosystem

Verifiable AI Civilization Architecture

MoCKA is a research-grade AI ecosystem designed for verifiable reasoning, institutional memory, and transparent governance.

MoCKA は、検証可能な AI 推論、制度的記憶、透明なガバナンスを目的とする研究エコシステムです。

---

# Architecture

![MoCKA Architecture](docs/images/mocka_architecture.svg)

---

# Repositories

| Layer | Role | Repository |
|------|------|-----------|
| MoCKA Core | Research gate and execution | [nsjpkimura-del/MoCKA](https://github.com/nsjpkimura-del/MoCKA) |
| Knowledge Gate | Institutional memory | [nsjpkimura-del/MoCKA-KNOWLEDGE-GATE](https://github.com/nsjpkimura-del/MoCKA-KNOWLEDGE-GATE) |
| Transparency | Audit and public proof | [nsjpkimura-del/mocka-transparency](https://github.com/nsjpkimura-del/mocka-transparency) |
| External Brain | External knowledge integration | [nsjpkimura-del/mocka-external-brain](https://github.com/nsjpkimura-del/mocka-external-brain) |
| Civilization | Governance philosophy | [nsjpkimura-del/mocka-civilization](https://github.com/nsjpkimura-del/mocka-civilization) |
| Core Private | Operational layer | Private repository |

---

# Research Workflow

![Research Workflow](docs/images/mocka_workflow.svg)

Experiment -> Experiment Registry -> Research Gate -> Verification -> Research Map

---

# Technical Backbone

MoCKA includes an automated verification system called Research Gate.

Research Gate verifies the ecosystem across structural integrity, research process registration, documentation consistency, and audit evidence.

Verification Status

RESEARCH_RUN: OK  
Verification controls executed: 20  
All verification checks passed

Meaning

MoCKA Ecosystem is a research system that has passed twenty verification controls.

---

# Verification Architecture

<details>
<summary>1 System Integrity Verification</summary>

ecosystem_doctor_integrity  
ecosystem_structure_scan  
canon_directory_integrity  
artifact_directory_integrity  
repo_entrypoints_present  
repo_git_clean_check  
repo_license_presence  

</details>

<details>
<summary>2 Research Process Verification</summary>

experiments_minimum_coverage  
research_registry_schema  
research_map_registry_integrity  
research_runner_selfcheck  

</details>

<details>
<summary>3 Documentation Verification</summary>

readme_role_vocab_integrity  
readme_research_entry_presence  
docs_link_audit  

</details>

<details>
<summary>4 Audit and Evidence Verification</summary>

gpg_signing_config_present  
doctor_script_presence  
doctor_artifact_schema  
doctor_emit_json_artifact  
doctor_emit_json_artifact  
doctor_sha_note_upsert  
canon_notes_integrity  

</details>

---

# Quick Demo

## Purpose

This demo is not a research experiment.

It is a verification run that shows what the system does and what it proves.

It executes the Research Gate verification and confirms that the MoCKA ecosystem is operational and internally consistent.

## What the Demo Does

It verifies, end-to-end, that the ecosystem is ready for reproducible research.

It checks:

System structure  
Repository integrity  
Research registry consistency  
Documentation consistency  
Audit and evidence presence

## Flow

Run verification command  
-> execute verification controls (about 20)  
-> aggregate results  
-> print final verdict

## Option A: Local Verification Command

powershell -ExecutionPolicy Bypass -File MoCKA/tools/mocka_research_run.ps1

Expected result

RESEARCH_RUN: OK

## Option B: Interactive Demo Venue

Evaluators can use a separate demo venue page.

Demo venue

[Open Demo Arena](DEMO_ARENA.md)

If an interactive workflow is enabled, the demo venue links to it.

Interactive verification (Actions)

[Open Research Gate Demo Workflow](https://github.com/nsjpkimura-del/MoCKA/actions)

## What This Proves

The demo proves that the research infrastructure is operational.

It demonstrates that:

the research workflow is registered  
the repository structure is valid  
the verification system is functioning  
the ecosystem is ready for reproducible research