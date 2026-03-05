# MoCKA Demo Arena

Runnable verification environment for the MoCKA ecosystem.

README is the research portal.  
Demo Arena is the execution environment.

---

# Quick Start (Minimal Demo)

This demo works even if the participant has never installed MoCKA.

---

## 1 Clone MoCKA

Run

cd $HOME  
git clone https://github.com/nsjpkimura-del/MoCKA.git

Expected Result

MoCKA repository downloaded.

---

## 2 Enter Repository

Run

cd $HOME\MoCKA

Expected Result

Repository directory opened.

---

## 3 Run Core Verification

Run

python .\verify_all.py

Expected Result

Verification steps execute.

Final line:

ALL CHECKS PASSED

---

# Demo 2 Research Execution

Purpose

Run MoCKA research verification experiments.

Run

cd $HOME\MoCKA  
powershell .\tools\run_experiments.ps1

Expected Result

Research experiments executed.

---

# Demo 3 Documentation Verification

Purpose

Verify documentation integrity.

Run

cd $HOME\MoCKA  
python tools\audit_docs_links.py

Expected Result

All documentation links verified.

---

# Demo 4 Audit Evidence Verification

Purpose

Verify cryptographic audit evidence.

Run

cd $HOME\MoCKA  
.\verify.bat

Expected Result

Chain and signature verification succeed.

Final line:

OK: CHAIN_OK + SIGNATURE_OK

---

# Full Ecosystem Demo (Advanced)

Requires the complete MoCKA ecosystem workspace.

---

## Run Ecosystem Doctor

Run

cd C:\Users\sirok\mocka-ecosystem  
powershell .\ecosystem_doctor.ps1

Expected Result

All repositories scanned.  
No structural errors.

---

## Emit Machine Readable Audit Artifact

Run

cd C:\Users\sirok\mocka-ecosystem  
powershell .\ecosystem_doctor.ps1 -EmitJson

Expected Result

JSON audit artifact generated.

---

# Structure

Demo Arena provides four verification layers.

1 Core Verification  
2 Research Process  
3 Documentation Integrity  
4 Audit Evidence

The purpose of this page is to allow anyone to reproduce
MoCKA verification experiments.