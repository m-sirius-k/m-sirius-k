# MoCKA Demo Arena

Executable demonstrations for the MoCKA ecosystem.

This page allows visitors to run a live verification directly from GitHub.

---

# Run Live Demo

Open the workflow page and press **Run workflow**.

https://github.com/nsjpkimura-del/nsjpkimura-del/actions/workflows/portal_verify.yml

This launches the verification system on GitHub servers.

---

# Live Result

After execution, open the run log.

https://github.com/nsjpkimura-del/nsjpkimura-del/actions

Expected result

RESULT: PASS

or

RESULT: FAIL

---

# Break Test

Purpose

Experience failure detection.

How to run

1 Edit README.md  
2 Remove one required section heading  
3 Commit and push  
4 Run the workflow again

Expected result

FAIL with missing section report.

---

# Repair Test

Purpose

Verify recovery after repair.

How to run

1 Restore the deleted section heading  
2 Commit and push  
3 Run workflow again

Expected result

PASS

---

# Local Reproduction

Optional local verification.

Run

cd C:\Users\sirok\mocka-ecosystem\nsjpkimura-del
python tools\portal_verify.py

Expected result

PASS

---

# Verification Domains

System Integrity

Portal structure requirements.

Documentation Integrity

Entry pages remain verifiable.

Audit Evidence

GitHub workflow logs provide execution evidence.
