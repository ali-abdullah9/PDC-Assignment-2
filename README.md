# Distributed Chat Application (Vector Clock and Matrix Clock Implementation)

## Overview

This assignment demonstrates message passing in distributed systems utilizing two key causal ordering mechanisms: Vector Clocks (BSS/SES Protocols) and Matrix Clocks. The application simulates multiple chat processes exchanging messages, ensuring causal consistency.

## Files Included

- **`chat_process.py`**: Implements the chat participants using vector clocks for the BSS/SES protocols.
- **`main.py`**: Executes the simulation by instantiating chat processes and managing their concurrent interactions.
- **`MatrixClock-Protocol.py`**: Implements Matrix Clocks to manage comprehensive causal ordering in message exchanges.

## How to Run

### Prerequisites
- Python 3.x installed.

### Running Vector Clock Implementation

Navigate to the directory and execute:
```bash
python main.py
```

### Running Matrix Clock Implementation

Navigate to the directory and execute:
```bash
python MatrixClock-Protocol.py
```

## Expected Output

### Vector Clock Example:
```
Process 0 sent message 'Hi' to Process 1 | VC: [1, 0, 0]
Process 1 delivered 'Hi' from Process 0 | Updated VC: [1, 1, 0]
...
```

### Matrix Clock Example:

```
Process 0 sent 'Hello' to Process 1
Matrix Clock: [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

Process 1 delivered 'Hello' from Process 0
Updated Matrix Clock for Process 1: [[1, 0, 0], [1, 1, 0], [0, 0, 0]]
...
```

## Explanation of Output

- **Sending Messages**: The message sent by a process includes its current vector or matrix clock.
- **Delivering Messages**: The receiving process updates its clock accordingly and prints the updated clock upon message delivery.
- **Buffering**: Messages arriving out of causal order are buffered until they meet delivery conditions.

## Concepts Covered

- **Vector Clocks**: Used by BSS/SES protocols to establish partial ordering of events.
- **Matrix Clocks**: A more comprehensive representation capturing detailed causality between multiple processes.
- **Buffering Mechanism**: Temporarily stores messages that cannot be immediately delivered to preserve causal ordering.

## References

- Coulouris, G., Dollimore, J., Kindberg, T., & Blair, G. (2011). *Distributed Systems: Concepts and Design (5th Edition)*. Pearson Education.
- Lamport, L. (1978). *Time, clocks, and the ordering of events in a distributed system.* Communications of the ACM.
- Birman, K., Schiper, A., & Stephenson, P. (1991). *Lightweight causal and atomic group multicast.* ACM Transactions on Computer Systems.
- Schiper, A., Eggli, J., & Sandoz, A. (1989). *A new algorithm to implement causal ordering.* Lecture Notes in Computer Science.

---

**Author:** Ali Abdullah
**Date:** March 2025

