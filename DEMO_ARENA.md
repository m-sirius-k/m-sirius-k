# MoCKA Demo Arena

This page is a runnable demonstration.

No installation required.
The demo runs on GitHub Actions.

---

# Demo 1 Browser Demo

Purpose

Demonstrate that this research portal is verifiable.

How to run

Open the workflow page and click Run workflow.

Workflow URL

https://github.com/nsjpkimura-del/nsjpkimura-del/actions/workflows/portal_verify.yml

Expected Result

PASS and a verification log.

What it verifies

README and DEMO_ARENA structure requirements are satisfied.

---

# Demo 2 Break Test

Purpose

Let participants experience failure detection.

How to run

Edit README.md and delete one required section heading.
Commit and push.

Then run Demo 1 again.

Expected Result

FAIL with a precise missing section report.

---

# Demo 3 Repair Test

Purpose

Let participants experience recovery after repair.

How to run

Restore the deleted section heading.
Commit and push.

Then run Demo 1 again.

Expected Result

PASS.

---

# Demo 4 Local Optional Reproduction

Purpose

Run the same verification locally.

Run

cd C:\Users\sirok\mocka-ecosystem\nsjpkimura-del
python tools\portal_verify.py

Expected Result

PASS.

---

# Verification Domains

System Integrity

Portal structure and required sections are present.

Documentation Integrity

Entry pages remain consistent and verifiable.

Audit Evidence

GitHub Actions run logs serve as public execution evidence.
