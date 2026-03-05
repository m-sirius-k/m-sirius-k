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
| MoCKA Core | Research gate and execution | https://github.com/nsjpkimura-del/MoCKA |
| Knowledge Gate | Institutional memory | https://github.com/nsjpkimura-del/MoCKA-KNOWLEDGE-GATE |
| Transparency | Audit and public proof | https://github.com/nsjpkimura-del/mocka-transparency |
| External Brain | External knowledge integration | https://github.com/nsjpkimura-del/mocka-external-brain |
| Civilization | Governance philosophy | https://github.com/nsjpkimura-del/mocka-civilization |
| Core Private | Operational layer | private repository |

---

# Research Workflow

![Research Workflow](docs/images/mocka_workflow.svg)

Experiment → Experiment Registry → Research Gate → Verification → Research Map

実験 → 実験登録 → Research Gate → 検証 → Research Map

---

# Technical Backbone

## English

MoCKA includes an automated verification system called **Research Gate**.

Research Gate verifies the ecosystem across:

system structure  
research process registration  
documentation integrity  
audit evidence

Verification Status

RESEARCH_RUN: OK  
Verification controls executed: 20  
All verification checks passed

Meaning

The MoCKA ecosystem has successfully passed twenty independent verification controls and is operational as a research system.

---

## 日本語

MoCKA には **Research Gate** と呼ばれる自動検証システムが組み込まれています。

Research Gate は以下の項目を検証します。

システム構造  
研究プロセス登録  
ドキュメント整合性  
監査証跡

検証結果

RESEARCH_RUN: OK  
検証項目数: 20  
すべての検証に成功

意味

MoCKA エコシステムは 20 の検証項目を通過した研究システムであり、正常に稼働していることを示しています。

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
doctor_sha_note_upsert  
canon_notes_integrity  

</details>

---

# Quick Demo

## English

This demo shows how the Research Gate verification works and what it proves.

The demo runs a verification routine across the MoCKA ecosystem.

It checks:

system structure  
repository integrity  
research registry consistency  
documentation validity  
audit artifact presence

Verification Flow

Run verification command  
→ execute verification controls  
→ aggregate results  
→ print final verdict

Local command

powershell -ExecutionPolicy Bypass -File MoCKA/tools/mocka_research_run.ps1

Expected result

RESEARCH_RUN: OK

Interactive demo venue

Open Demo Arena

DEMO_ARENA.md

---

## 日本語

このデモは Research Gate 検証システムが  
何を行い、何を証明するのかを示すものです。

このコマンドは MoCKA エコシステム全体に対して  
検証処理を実行します。

検証内容

システム構造  
リポジトリ整合性  
研究登録情報  
ドキュメント整合性  
監査証跡

検証フロー

コマンド実行  
→ 検証項目実行  
→ 結果集約  
→ 最終判定表示

実行コマンド

powershell -ExecutionPolicy Bypass -File MoCKA/tools/mocka_research_run.ps1

期待される結果

RESEARCH_RUN: OK

体験デモ

DEMO_ARENA.md