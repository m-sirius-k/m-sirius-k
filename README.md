# MoCKA Ecosystem

Verifiable AI Civilization Architecture

MoCKA is a research-grade AI ecosystem designed for verifiable AI reasoning, institutional memory, and transparent governance.

MoCKA は、検証可能な AI 推論、制度的記憶、透明なガバナンスを目的として設計された研究エコシステムです。


---

# Architecture

![MoCKA Architecture](docs/images/mocka_architecture.svg)


---

# Repositories

| Layer | Role | Repository |
|------|------|-----------|
| **MoCKA Core** | Research gate and execution system | https://github.com/nsjpkimura-del/MoCKA |
| **Knowledge Gate** | Institutional memory layer | https://github.com/nsjpkimura-del/MoCKA-KNOWLEDGE-GATE |
| **Transparency** | Audit and public verification layer | https://github.com/nsjpkimura-del/mocka-transparency |
| **External Brain** | External knowledge integration | https://github.com/nsjpkimura-del/mocka-external-brain |
| **Civilization** | Governance philosophy and institutional design | https://github.com/nsjpkimura-del/mocka-civilization |
| **Core Private** | Operational private layer | private repository |


---

# Research Workflow

![Research Workflow](docs/images/mocka_workflow.svg)


Experiment  
Individual research execution.

Experiment Registry  
Structured registration of experiments.

Research Gate  
Verification system that evaluates ecosystem integrity.

Verification  
Automated checks across system structure, research processes, documentation, and audit evidence.

Research Map  
Human-readable map of research artifacts and relationships.


Workflow

Experiment → Experiment Registry → Research Gate → Verification → Research Map


---

# Technical Backbone

MoCKA includes an automated verification system called **Research Gate**.

This system executes verification controls to ensure that the ecosystem is structurally consistent, research processes are valid, documentation is complete, and audit evidence exists.

Research Gate Status

Verification controls executed : 20  
Verification result            : All checks passed  
System state                   : Operational


This indicates that the ecosystem has successfully passed all verification controls defined in the Research Gate.


---

# Verification Architecture


## 1 System Integrity Verification

Purpose  
Ensure the ecosystem structure matches the design specification.

Controls

ecosystem_doctor_integrity  
ecosystem_structure_scan  
canon_directory_integrity  
artifact_directory_integrity  
repo_entrypoints_present  
repo_git_clean_check  
repo_license_presence  

Detailed verification specification  
docs/verification/system_integrity.md


---

## 2 Research Process Verification

Purpose  
Ensure research experiments are properly registered and reproducible.

Controls

experiments_minimum_coverage  
research_registry_schema  
research_map_registry_integrity  
research_runner_selfcheck  

Detailed verification specification  
docs/verification/research_process.md


---

## 3 Documentation Verification

Purpose  
Ensure documentation provides navigability and institutional terminology consistency.

Controls

readme_role_vocab_integrity  
readme_research_entry_presence  
docs_link_audit  

Detailed verification specification  
docs/verification/documentation.md


---

## 4 Audit and Evidence Verification

Purpose  
Ensure all research operations produce traceable and auditable artifacts.

Controls

gpg_signing_config_present  
doctor_script_presence  
doctor_artifact_schema  
doctor_emit_json_artifact  
doctor_sha_note_upsert  
canon_notes_integrity  

Detailed verification specification  
docs/verification/audit_evidence.md


---

# Quick Demo

Run the verification system locally.

powershell -ExecutionPolicy Bypass -File MoCKA/tools/mocka_research_run.ps1


Expected output

RESEARCH_RUN: OK


This indicates that all verification controls have successfully passed.


---

# Concept

MoCKA is an experimental architecture for building AI systems with verifiable reasoning and institutional governance.

Key ideas

Verifiable AI reasoning  
Institutional memory systems  
Transparent research governance


---

# Japanese Overview

MoCKA は単なるソフトウェアではなく、以下を目的とする研究アーキテクチャです。

検証可能な AI 推論  
制度的記憶システム  
透明な研究ガバナンス


---

# License

See repository license.
![Research Workflow](docs/images/mocka_workflow.svg)

