## Output – Advanced Password Security Analysis

**Input Passwords:**
`password`, `Admin123!`, `Qwerty!`, `S3cure$Pass`, `letmein`, `P@ssw0rd2026`, `1234qwer`

### Analysis Results

| Password        | Risk Score | Risk Level  | Key Feedback                                         |
|-----------------|------------|------------|-----------------------------------------------------|
| password        | 100        | High Risk  | Common password, found in breaches, low entropy     |
| Admin123!       | 30         | Low Risk   | Low character diversity                              |
| Qwerty!         | 70         | Medium Risk| Matches common keyboard pattern                      |
| S3cure$Pass     | 10         | Low Risk   | Strong password, high entropy                        |
| letmein         | 95         | High Risk  | Common password, predictable pattern                |
| P@ssw0rd2026    | 25         | Low Risk   | Strong variation, moderate entropy                  |
| 1234qwer        | 80         | Medium Risk| Keyboard pattern detected, moderate entropy         |

---

### Password Strength Distribution

![Password Strength Distribution]

**High Risk:** 3 passwords (43%)  
**Medium Risk:** 2 passwords (29%)  
**Low Risk:** 2 passwords (28%)  

---

### Most Common Keyboard Patterns

![Keyboard Pattern Frequency](images/keyboard_pattern_frequency.png)

| Pattern   | Count | Percentage |
|-----------|-------|------------|
| qwerty    | 1     | 14%        |
| 1234      | 2     | 29%        |
| letmein   | 1     | 14%        |
| Others    | 3     | 43%        |


**Notes:**
- Risk Score combines **structural analysis, breach detection, and entropy estimation**.  
- Feedback is **explainable and actionable** for improving password security.  
- Visualizations provide **quick insights for recruiters** at a glance.
