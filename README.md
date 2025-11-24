# **Number Sequence Analysis – Task 1 & Task 2**
*A Python mini-project for sequence generation and positional digit extraction*

---

## 🚀 **Overview**
This repository contains two Python programs based on number-sequence patterns.  
The project demonstrates how simple logic, loops, and string manipulation can solve sequence-based computational problems.

---

## 📁 **Files in Repository**
| File | Description |
|------|-------------|
| **Task1.py** | Generates continuous number sequence until length ≥ *n* |
| **Task2.py** | Finds the digit at a specific position in the infinite sequence |
| **README.md** | Project documentation |

---

## 🔢 **Task 1 — Generate Continuous Sequence**

### **Objective**
Generate a continuous string:  
`123456789101112…`  
until its total length becomes at least **n**.

### **Code**
```python
n = int(input("Enter the required string length: "))

sequence = ""
num = 1

while len(sequence) < n:
    sequence += str(num)
    num += 1

print("Generated sequence:", sequence)
```

| Input | Output |
|-------|---------|
| `15` | `123456789101112` |
| `25` | `1234567891011121314151617` |




## 🔢 **Task 2 — Digit at a Specific Position**

### **Objective**
Given a position **pos**, determine which digit appears at that exact index in the infinite sequence:
`123456789101112131415…`

### **Code**
```python
pos = int(input("Enter the position: "))

sequence = ""
num = 1

while len(sequence) < pos:
    sequence += str(num)
    num += 1

result = sequence[pos - 1]

print("Digit at position", pos, "is:", result)
```

| Input | Output |
|-------|---------|
| `15` | `2` |
| `25` | `7` |


---

## 🧠 **Concepts Used**
- Looping structures  
- String concatenation  
- Incremental sequence building  
- Index-based access  
- Algorithmic reasoning  
- Handling dynamic string length  

---

## 📘 **Applications**
- Number pattern exploration  
- Digit-indexing and mathematical sequence problems  
- Beginner-level algorithm design  
- Strengthening Python fundamentals  
- Useful for coding assignments and logical puzzle solving  

---

## ✅ **Conclusion**
This project demonstrates how simple loops and string operations can be used to solve number-sequence problems efficiently.  
Both tasks provide clear examples of algorithmic thinking and Python implementation, making the project valuable for learning foundational programming concepts.







