# 🔐 Password Security Analyzer (Python)

A simple educational cybersecurity project written in Python that analyzes password strength based on common security best practices.

This project focuses on defensive security, not hacking or exploitation.

---

## 🎯 Project Goal

The purpose of this project is to understand:
- how applications validate passwords
- why weak passwords are dangerous
- how basic security policies are enforced in real systems

---

## 🛡️ Security Criteria Used

The password is analyzed using the following checks:

- Minimum length (12 characters)
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

---

## 📊 Strength Evaluation Logic

Each satisfied rule adds 1 point.

- 0–2 → Weak  
- 3–4 → Medium  
- 5 → Strong  

---

## ▶️ How to Run

```bash
python3 analyzer.py

password-analyzer/
├── analyzer.py
├── validators.py
└── README.md

⚠️ Disclaimer

This project is educational and defensive only.
It does not perform hacking, cracking, or illegal activities.


---

