# MoCKA Demo Arena

Verification and Experiment Environment

This page hosts runnable verification experiments for the MoCKA ecosystem.

README is the entry page.
Demo Arena is the execution environment.

---

# System Integrity Tests

## ecosystem_doctor_integrity

Purpose  
Verify full ecosystem integrity.

Run


cd C:\Users\sirok\mocka-ecosystem
powershell .\ecosystem_doctor.ps1


Expected Result

All repositories scanned  
No structural errors

---

## ecosystem_structure_scan

Purpose  
Verify ecosystem directory layout.

Run


cd C:\Users\sirok\mocka-ecosystem
powershell .\tools\structure_scan.ps1


Expected Result

Required directories detected

---

## repo_git_clean_check

Purpose  
Verify repository git state.

Run


cd C:\Users\sirok\mocka-ecosystem
git status


Expected Result

working tree clean

---

# Research Process Tests

## experiments_minimum_coverage

Purpose  
Verify research experiment coverage.

Run


cd C:\Users\sirok\mocka-ecosystem\MoCKA
powershell .\tools\run_experiments.ps1


Expected Result

All experiments executed

---

## research_registry_schema

Purpose  
Verify research registry schema.

Run


cd C:\Users\sirok\mocka-ecosystem\MoCKA
python tools\check_research_registry.py


Expected Result

Schema validation passes

---

# Documentation Verification

## readme_role_vocab_integrity

Purpose  
Verify terminology consistency.

Run


cd C:\Users\sirok\mocka-ecosystem\MoCKA
python tools\check_readme_vocab.py


Expected Result

No vocabulary violations

---

## docs_link_audit

Purpose  
Verify documentation links.

Run


cd C:\Users\sirok\mocka-ecosystem\MoCKA
python tools\audit_docs_links.py


Expected Result

All documentation links valid

---

# Audit Evidence Tests

## gpg_signing_config_present

Purpose  
Verify GPG signing configuration.

Run


gpg --list-secret-keys


Expected Result

Valid signing key detected

---

## doctor_emit_json_artifact

Purpose  
Verify machine-readable doctor output.

Run


cd C:\Users\sirok\mocka-ecosystem
powershell .\ecosystem_doctor.ps1 -EmitJson


Expected Result

JSON artifact generated

---

# Design

README explains the architecture.

Demo Arena proves the system works.

The arena provides reproducible verification of the MoCKA ecosystem.
