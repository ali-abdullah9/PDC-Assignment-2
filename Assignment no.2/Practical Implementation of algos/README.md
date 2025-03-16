# Vector Clock Simulation

This repository contains a Python implementation of vector clocks, simulating message passing between multiple processes. Vector clocks are utilized to capture causal relationships in distributed systems.

## Overview

- **Processes** simulate message passing to each other.
- Vector clocks are maintained and updated to track message causality.
- Messages may be buffered if they cannot be immediately delivered due to causality constraints.

## Files

- `BSS-protocol.py`: The file contain code for Birman-Schiper-Stephenson (BSS) Protocol.
- `SES-protocol.py`: The file contain code for Schiper-Eggli-Sandoz (SES) Protocol.
- `MatrixClock-Protocol.py`: The file contain code for Matrix Clock Protocol.

## How to Run

### Prerequisites
- Python 3.x

### Running the Simulation

```bash
python BSS-protocol.py
```

The simulation will execute with a default setup of 3 processes exchanging 5 messages each.

## Customizing the Simulation
You can adjust the number of processes and messages by editing the following line in the `simulate_processes` function call:

```python
if __name__ == "__main__":
    simulate_processes(num_processes=3, num_messages=5)
```

Modify `num_processes` and `num_messages` to experiment with different scenarios.

## Output Explanation

- **Sent Messages**: Each process prints messages when it sends data to another process.
- **Delivered Messages**: Messages are delivered immediately if causality constraints are met.
- **Buffered Messages**: Messages that cannot be immediately delivered are buffered and delivered later once conditions are met.

Example output:
```
Process 0 sent message to Process 2: (0, [1, 0, 0])
Process 2 delivered message from Process 0: [1, 0, 0]
```

## Concepts
- **Vector Clock**: An array capturing the partial ordering of events in distributed systems.
- **Message Buffering**: Temporarily stores messages that cannot be immediately delivered due to ordering constraints.

## License

This project is open source and freely available to modify and distribute.
