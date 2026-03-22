# MoCKA Perpetual Mechanism

MoCKA is not a static system or ecosystem.
It is a perpetual mechanism.

# Architecture

<p align="center">
  <a href="docs/images/mocka_overview.svg">
    <img src="docs/images/mocka_overview.svg" width="800">
  </a>
</p>

### Governance Layer

This layer defines the governance mechanism of MoCKA.

MoCKA continuously transforms external inputs into internal driving force through a cyclic architecture composed of:

- Insert (input acquisition and admission control)
- Storage (ledger and institutional memory)
- Runtime (knowledge execution and processing)
- Audit (verification, validation, and control)

These components do not form a simple processing pipeline.
They establish a governance structure that determines what is accepted, preserved, executed, and validated within the system.

This mechanism is analogous to a self-winding mechanical watch.
External events act as motion input.
The system converts that motion into stored energy, enabling continuous operation.

Even under partial failure, knowledge circulation does not stop.
Through a dual-path architecture called Shadow Movement, the system maintains operation by transitioning into a reduced but stable mode.

MoCKA is therefore not just a system, but a perpetual governance mechanism for verifiable knowledge.

<p align="center">
  <a href="docs/images/mocka_governance_layer_perpetual_mechanism.svg">
    <img src="docs/images/mocka_governance_layer_perpetual_mechanism.svg" width="800">
  </a>
</p>

## MoCKA Perpetual Mechanism Framework

This repository is part of the MoCKA Perpetual Mechanism Framework for AI civilization research.
MoCKA studies AI civilization systems including governance, consensus and institutional memory, with a focus on verifiable and reproducible knowledge circulation.

#

Defines how decisions are made and controlled.

- execution_order_engine
- dispatcher
- meta_audit_engine
- preventive_rule_engine

## MOCKA_MovementStructure

Research Core
MoCKA

Civilization Theory
mocka-civilization

Knowledge System
mocka-knowledge-gate

Transparency Layer
mocka-transparency

Network Layer
mocka-outfield

Civilization Core (private)
mocka-core-private

# MoCKA Insight System

Verifiable AI Civilization Architecture

MoCKA is a research-grade architecture designed for verifiable reasoning, institutional memory, and resilient knowledge circulation.

# Architecture

MoCKA structures knowledge verification and memory preservation through layered components that maintain traceable reasoning and long-term reproducibility.

# Core Architecture Principle

MoCKA is built on a fail-safe design philosophy called Shadow Movement.
The system never assumes correctness. Every primary process is paired with an independent shadow verification path.
Even if the primary process fails, the circulation of knowledge does not stop. Instead, the system transitions into a Minimum Operating Capability mode designed to maintain approximately 75 percent operational capability.

This principle exists to avoid total system halt and to preserve knowledge circulation as the first priority.

Architecture principle reference
docs/SHADOW_MOVEMENT_PRINCIPLE.md

# Shadow Movement Architecture

## MoCKA Dual Movement Architecture

Primary Movement and Shadow Movement operate as a dual-heart architecture.
The primary path maintains full research execution capability, while the shadow path preserves knowledge circulation through independent verification.

Primary Movement
Main research execution path.

Shadow Movement
Independent verification path that preserves circulation when failures occur.

MoCKA uses a dual movement architecture conceptually similar to a mechanical clock with a redundant escapement.

# Repositories

| Layer              | Role                           | Repository                                         |
| ------------------ | ------------------------------ | -------------------------------------------------- |
| MoCKA Core         | Research gate and execution    | https://github.com/m-sirius-k/MoCKA                |
| Knowledge Gate     | Institutional memory layer     | https://github.com/m-sirius-k/MoCKA-KNOWLEDGE-GATE |
| Transparency       | Audit and public verification  | https://github.com/m-sirius-k/mocka-transparency   |
| External Brain     | External knowledge integration | https://github.com/m-sirius-k/mocka-external-brain |
| Civilization Layer | Governance philosophy          | https://github.com/m-sirius-k/mocka-civilization   |
| Core Private       | Operational layer              | Internal repository                                |

# Research Workflow

Experiment → Experiment Registry → Research Gate → Verification → Research Map

This workflow is a process for recording, verifying, and structuring research activities as they occur,
and transforming them into verifiable knowledge.

Since hypotheses, experimental conditions, procedures, and verification results are all systematically stored,
the data remains in a state that allows third parties to reproduce the results using the exact same procedures.

# Technical Backbone

MoCKA includes an automated verification framework called Research Gate.
Research Gate continuously validates the architecture across several dimensions:

- system structure
- research registry integrity
- documentation consistency
- audit artifacts and verification evidence

Verification Status
RESEARCH_RUN OK
Verification controls executed: 20
All verification checks passed

### Research Gate Verification

MoCKA includes an automated verification framework called **Research Gate**.  
It continuously validates the architecture across four domains:

- System integrity
- Research process integrity
- Documentation consistency
- Audit and evidence integrity

**Status:** `RESEARCH_RUN OK` — 20 verification checks passed.

<details>
  <summary>View all 20 verification checks</summary>

1. **System Integrity Verification**
   - `ecosystem_doctor_integrity`
   - `ecosystem_structure_scan`
   - `canon_directory_integrity`
   - `artifact_directory_integrity`
   - `repo_entrypoints_present`
   - `repo_git_clean_check`
   - `repo_license_presence`

2. **Research Process Verification**
   - `experiments_minimum_coverage`
   - `research_registry_schema`
   - `research_map_registry_integrity`
   - `research_runner_selfcheck`

3. **Documentation Verification**
   - `readme_role_vocab_integrity`
   - `readme_research_entry_presence`
   - `docs_link_audit`

4. **Audit and Evidence Verification**
   - `gpg_signing_config_present`
   - `doctor_script_presence`
   - `doctor_artifact_schema`
   - `doctor_emit_json_artifact`
   - `doctor_sha_note_upsert`
   - `canon_notes_integrity`

</details>

Meaning
The architecture is structurally valid and capable of executing reproducible research processes.

# Verification Architecture

The following verification domains are used to validate the MoCKA architecture:

1. System Integrity Verification

- ecosystem_doctor_integrity
- ecosystem_structure_scan
- canon_directory_integrity
- artifact_directory_integrity
- repo_entrypoints_present
- repo_git_clean_check
- repo_license_presence

2. Research Process Verification

- experiments_minimum_coverage
- research_registry_schema
- research_map_registry_integrity
- research_runner_selfcheck

3. Documentation Verification

- readme_role_vocab_integrity
- readme_research_entry_presence
- docs_link_audit

4. Audit and Evidence Verification

- gpg_signing_config_present
- doctor_script_presence
- doctor_artifact_schema
- doctor_emit_json_artifact
- doctor_sha_note_upsert
- canon_notes_integrity

# MoCKA Vision

MoCKA aims to establish a Verifiable Knowledge Infrastructure for the AI era.
As AI systems generate increasing volumes of knowledge, MoCKA focuses on preserving integrity, traceability, and reproducibility for that knowledge.

MoCKA is a research architecture dedicated to the long-term preservation and governance of AI-generated knowledge.

# Status

Research Stage: Active Development

The architecture and verification framework are operational, and further expansion of the knowledge infrastructure is ongoing.

---

# 日本語版

## MoCKA Perpetual Mechanism

MoCKA は静的なシステムでも、単なるエコシステムでもありません。
MoCKA は 永続機構（Perpetual Mechanism） です。

## Architecture

<p align="center">
  <a href="docs/images/mocka_overview.svg">
    <img src="docs/images/mocka_overview.svg" width="800">
  </a>
</p>

MoCKA は、次の循環アーキテクチャを通じて外部入力を内部の駆動力へと継続的に変換します。

- Insert（入力取得）
- Storage（台帳と記憶の永続化）
- Runtime（知識処理エンジン群）
- Audit（検証と統制）

この機構は、自動巻き機構を備えた機械式時計に類似しています。
外部イベントが“振り”として入力され、システムはその運動を内部エネルギーへと変換します。
Shadow Movement と呼ばれる二重経路アーキテクチャにより、一部が故障しても知識循環は継続します。

MoCKA は「止まらない検証可能な知識機構」として設計されています。

<p align="center">
  <a href="docs/images/mocka_governance_layer_perpetual_mechanism.svg">
    <img src="docs/images/mocka_governance_layer_perpetual_mechanism.svg" width="800">
  </a>
</p>

## MoCKA 永続機構型AI文明研究基盤

このリポジトリは、AI 文明研究のための MoCKA 永続機構型研究フレームワーク の一部です。
MoCKA は、ガバナンス、合意形成、制度的記憶を含む AI 文明システムを対象に、検証可能かつ再現可能な知識循環に焦点を当てています。

### Governance Layer

Defines how decisions are made and controlled.

- execution_order_engine
- dispatcher
- meta_audit_engine
- preventive_rule_engine

## MOCKA_Movement構造

研究コア
MoCKA

文明理論
mocka-civilization

知識システム
mocka-knowledge-gate

透明性レイヤー
mocka-transparency

ネットワークレイヤー
mocka-outfield

文明コア（非公開）
mocka-core-private

## MoCKA Insight System

検証可能な AI 文明アーキテクチャ

MoCKA は、検証可能な推論、制度的記憶、知識循環の持続性を目的として設計された研究アーキテクチャです。

## アーキテクチャ

MoCKA は、推論履歴の追跡と長期的再現性を維持するための層構造アーキテクチャとして設計されています。

## コアアーキテクチャ原則

MoCKA は Shadow Movement と呼ばれるフェイルセーフ設計思想に基づいて構築されています。
MoCKA は「正しさを前提としない」設計を採用し、すべての主要プロセスには独立したシャドー検証経路が存在します。
そのため障害が発生した場合でも知識の循環は停止せず、Minimum Operating Capability（最低限稼働能力）を基準とした約 75％ の稼働能力を維持する設計となっています。

これは、システムの完全停止を避け、知識循環を最優先で維持するための基本原理です。

アーキテクチャ原則の詳細
docs/SHADOW_MOVEMENT_PRINCIPLE.md

## Shadow Movement アーキテクチャ

MoCKA 二重ムーブメントアーキテクチャ

Primary Movement と Shadow Movement は、二重の心臓のようなアーキテクチャとして動作します。
Primary Movement は研究実行の主経路として 100％ の能力で動作し、Shadow Movement は独立した検証経路として知識循環を維持します。

Primary Movement
研究実行の主経路。

Shadow Movement
主経路に問題が発生した場合でも知識循環を維持する独立経路。

MoCKA は、冗長な脱進機を持つ機械式時計に概念的に類似した二重ムーブメント構造として設計されています。

## リポジトリ構成

| レイヤー           | 役割                             | リポジトリ                                         |
| ------------------ | -------------------------------- | -------------------------------------------------- |
| MoCKA Core         | Research Gate と実行系           | https://github.com/m-sirius-k/MoCKA                |
| Knowledge Gate     | 制度的記憶レイヤー               | https://github.com/m-sirius-k/MoCKA-KNOWLEDGE-GATE |
| Transparency       | 監査と公開検証                   | https://github.com/m-sirius-k/mocka-transparency   |
| External Brain     | 外部知識統合                     | https://github.com/m-sirius-k/mocka-external-brain |
| Civilization Layer | ガバナンス哲学・文明理論         | https://github.com/m-sirius-k/mocka-civilization   |
| Core Private       | オペレーションレイヤー（非公開） | 内部リポジトリ                                     |

## 研究ワークフロー

Experiment → Experiment Registry → Research Gate → Verification → Research Map

このワークフローは、研究行為をそのまま記録・検証・構造化し、
証明可能な知識へ変換するためのプロセスです。

仮説、実験条件、実行内容、検証結果のすべてが体系的に保存されるため、
第三者が同一手順で再現できる状態が維持されます。

## 技術的バックボーン

MoCKA には Research Gate と呼ばれる自動検証フレームワークが組み込まれています。
Research Gate は次の観点からアーキテクチャを継続的に検証します。

- システム構造
- 研究登録情報の整合性
- ドキュメント整合性
- 監査証跡および検証証拠

検証結果
RESEARCH_RUN OK
検証実行数: 20
すべての検証に成功

意味  
アーキテクチャは構造的に整合しており、再現可能な研究プロセスを実行できる状態にあります。

## 検証アーキテクチャ（日本語サマリ）

MoCKA アーキテクチャの整合性は、次の検証領域によって確認されます。

1. システム整合性検証
   - ecosystem_doctor_integrity
   - ecosystem_structure_scan
   - canon_directory_integrity
   - artifact_directory_integrity
   - repo_entrypoints_present
   - repo_git_clean_check
   - repo_license_presence

2. 研究プロセス検証
   - experiments_minimum_coverage
   - research_registry_schema
   - research_map_registry_integrity
   - research_runner_selfcheck

3. ドキュメント検証
   - readme_role_vocab_integrity
   - readme_research_entry_presence
   - docs_link_audit

4. 監査・証跡検証
   - gpg_signing_config_present
   - doctor_script_presence
   - doctor_artifact_schema
   - doctor_emit_json_artifact
   - doctor_sha_note_upsert
   - canon_notes_integrity

意味
アーキテクチャは構造的に整合しており、再現可能な研究プロセスを実行できる状態にあります。

## 検証アーキテクチャ

MoCKA アーキテクチャの整合性は、次の検証領域によって確認されます。

1. システム整合性検証

- ecosystem_doctor_integrity
- ecosystem_structure_scan
- canon_directory_integrity
- artifact_directory_integr integrity
- repo_entrypoints_present
- repo_git_clean_check
- repo_license_presence

2. 研究プロセス検証

- experiments_minimum_coverage
- research_registry_schema
- research_map_registry_integrity
- research_runner_selfcheck

3. ドキュメント検証

- readme_role_vocab_integrity
- readme_research_entry_presence
- docs_link_audit

4. 監査・証跡検証

- gpg_signing_config_present
- doctor_script_presence
- doctor_artifact_schema
- doctor_emit_json_artifact
- doctor_sha_note_upsert
- canon_notes_integrity

## MoCKA ビジョン

MoCKA は、AI 時代のための 検証可能な知識基盤（Verifiable Knowledge Infrastructure） を構築することを目標としています。
AI によって生成される知識量が増加する中で、その履歴・証明・再現性を維持する制度的基盤の整備にフォーカスしています。

MoCKA は、AI が生成する知識を長期的に保存し、統治するための研究アーキテクチャです。

## ステータス

Research Stage: Active Development

現在 MoCKA は研究開発段階にあり、アーキテクチャと検証フレームワークは稼働しています。
今後さらに知識基盤の拡張が進められます。
