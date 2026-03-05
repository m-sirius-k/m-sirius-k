@'
# MoCKA Demo Arena

Runnable verification environment for the MoCKA ecosystem.

README is the research portal.

Demo Arena is the execution environment.

---

# Quick Start (Minimal Demo)

This demo works even if the participant has never installed MoCKA.

---

## 1 Clone MoCKA

```powershell
cd $HOME
git clone https://github.com/nsjpkimura-del/MoCKA.git

Expected Result

MoCKA repository downloaded.

2 Enter Repository
cd $HOME\MoCKA

Expected Result

Repository directory opened.

3 Run Core Verification
python .\verify_all.py

Expected Result

Verification steps run.

Final line:

ALL CHECKS PASSED

Demo 2 Research Execution

Purpose

Run MoCKA research verification experiments.

Run Experiments
cd $HOME\MoCKA
powershell .\tools\run_experiments.ps1

Expected Result

Experiments execute successfully.

Demo 3 Documentation Verification

Purpose

Verify documentation integrity.

Run Documentation Audit
cd $HOME\MoCKA
python tools\audit_docs_links.py

Expected Result

All documentation links verified.

Demo 4 Audit Evidence Verification

Purpose

Verify cryptographic audit evidence.

Run Signature Verification
cd $HOME\MoCKA
.\verify.bat

Expected Result

Chain and signature verification succeed.

Final line:

OK: CHAIN_OK + SIGNATURE_OK

Full Ecosystem Demo (Advanced)

Requires the complete MoCKA ecosystem workspace.

Run Ecosystem Doctor
cd C:\Users\sirok\mocka-ecosystem
powershell .\ecosystem_doctor.ps1

Expected Result

All repositories scanned.

No structural errors.

Emit Machine Readable Audit Artifact
cd C:\Users\sirok\mocka-ecosystem
powershell .\ecosystem_doctor.ps1 -EmitJson

Expected Result

JSON audit artifact generated.

Structure

Demo Arena provides four verification layers.

1 Core Verification
2 Research Process
3 Documentation Integrity
4 Audit Evidence

The purpose of this page is to allow anyone to reproduce
MoCKA verification experiments.
'@ | Set-Content -Encoding UTF8 DEMO_ARENA.md


---

# 2 Git 登録

```powershell
cd C:\Users\sirok\mocka-ecosystem\nsjpkimura-del
git add DEMO_ARENA.md
git commit -m "Demo Arena: runnable verification demos"
git push origin main