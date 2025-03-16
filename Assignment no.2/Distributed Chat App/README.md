# Distributed Chat Application (Using BSS/SES and Matrix Clocks)

This repository contains Python implementations demonstrating causal message ordering in distributed systems using two popular causal ordering algorithms:

- **Birman-Schiper-Stephenson (BSS) Protocol** / Schiper-Eggli-Sandoz (SES) Protocol (using vector clocks)
- **Matrix Clock Protocol** (using matrix clocks)

## Overview

The distributed chat application simulates message passing among multiple processes, ensuring causal ordering. Each process maintains its clock to track events and determine the order in which messages should be delivered. If messages arrive out of order, they're temporarily buffered and delivered when causal conditions are met.

## Files Included

### 1. BSS/SES Protocol Implementation
- `chat_process.py`
- `main.py`

**Purpose:**

Demonstrates message ordering using vector clocks, ensuring causally consistent message delivery among simulated chat participants.

**How to Run:**

1. Ensure Python 3 is installed.
2. Open a terminal in your project's directory.
3. Execute:

```bash
python main.py
```

## Expected Output (BSS/SES):

Example output:

```
Process 0 sent message 'Hi' to Process 1 | VC: [1, 0, 0]
Process 1 delivered 'Hi' from Process 0 | Updated VC: [1, 1, 0]
...
```

## Matrix Clock Protocol

**Files:**

- `process.py`
- `main.py`

**Purpose:**

Demonstrates a more comprehensive causal ordering mechanism using matrix clocks, enabling detailed tracking of message causality among multiple processes.

**How to Run:**

1. Ensure Python 3 is installed.
2. Navigate to the project directory in your terminal.
3. Run the application:

```bash
python main.py
```

**Expected Output (Sample):**

```
Process 0 sent 'Hello' to Process 1
Matrix Clock: [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

Process 1 delivered 'Hello' from Process 0
Updated Matrix Clock for Process 1: [[1, 0, 0], [1, 1, 0], [0, 0, 0]]
...
```

## Dependencies

No external libraries required (Python's built-in libraries `threading`, `random`, and `time` are used).

## Purpose and Use Cases

- Educational demonstration of causal ordering in distributed computing systems.
- Illustrating practical implementations of BSS/SES and Matrix Clocks protocols.
- Useful as a learning tool for understanding synchronization and message ordering in distributed applications.

## References

- [Vector Clocks (GeeksforGeeks)](https://www.geeksforgeeks.org/vector-clock-in-distributed-systems/)
- [Birman-Schiper-Stephenson Protocol](https://www.geeksforgeeks.org/birman-schiper-stephenson-protocol/)
- [Matrix Clock Explanation](https://users.ece.utexas.edu/~garg/dist/foundations.pdf)
- [Distributed Systems Concepts and Design - Coulouris](https://www.pearson.com/us/higher-education/program/Coulouris-Distributed-Systems-Concepts-and-Design-5th-Edition/PGM297462.html)

---

**Author:**
Ali Abdullah
```

