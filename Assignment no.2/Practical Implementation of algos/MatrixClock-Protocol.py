import threading
import random
import time

class MatrixProcess:
    def __init__(self, pid, total_processes):
        """
        Initialize a process with a unique ID, total number of processes, and necessary structures.
        """
        self.pid = pid
        self.total_processes = total_processes
        # Initialize matrix clock with zeros
        self.matrix_clock = [[0]*total_processes for _ in range(total_processes)]
        # Buffer to store messages that can't yet be delivered
        self.buffer = []
        # Lock for thread-safe operations
        self.lock = threading.Lock()

    def increment_clock(self):
        """Increment the local process's own logical clock."""
        self.matrix_clock[self.pid][self.pid] += 1

    def send_message(self, recipient, message):
        # Increment local clock before sending message
        self.increment_clock()
        # Create message packet
        msg_packet = {
            'matrix_clock': [row[:] for row in self.matrix_clock],
            'sender': self.pid,
            'message': message
        }
        print(f"Process {self.pid} sent '{message}' to Process {recipient.pid}\nMatrix Clock: {msg_packet['matrix_clock']}\n")
        recipient.receive_message(msg_packet)

    def receive_message(self, msg_packet):
        # Lock to ensure thread safety when modifying the clock and buffer
        with self.lock:
            # Check if the message can be delivered immediately
            if self.can_deliver(msg_packet):
                self.deliver(msg_packet)
                # Check buffer to see if other messages can now be delivered
                self.check_buffer()
            else:
                # Buffer the message for later delivery
                self.buffer.append(msg_packet)
                print(f"Process {self.pid} buffered message '{msg_packet['message']}' from Process {msg_packet['sender']}\n")

    def can_deliver(self, msg_packet):
        sender = msg_packet['sender']
        sender_clock = msg_packet['matrix_clock']
        # Check delivery conditions based on matrix clock rules
        for k in range(self.total_processes):
            if k != sender:
                if sender_clock[k][sender] > self.matrix_clock[k][sender]:
                    return False
        if sender_clock[sender][sender] != self.matrix_clock[sender][sender] + 1:
            return False
        return True

    def deliver(self, msg_packet):
        # Log message delivery and update local matrix clock
        print(f"Process {self.pid} delivered '{msg_packet['message']}' from Process {msg_packet['sender']}\nMatrix Clock: {msg_packet['matrix_clock']}\n")
        self.update_clock(msg_packet['matrix_clock'])

    def update_clock(self, received_clock):
        # Update local matrix clock based on received message clock
        for i in range(self.total_processes):
            for j in range(self.total_processes):
                self.matrix_clock[i][j] = max(self.matrix_clock[i][j], received_clock[i][j])

    def check_buffer(self):
        # List to track delivered messages
        delivered_msgs = []
        # Check buffered messages for possible delivery
        for msg in self.buffer:
            if self.can_deliver(msg):
                self.deliver(msg)
                delivered_msgs.append(msg)
        # Remove delivered messages from buffer
        for msg in delivered_msgs:
            self.buffer.remove(msg)

    def can_deliver(self, msg_packet):
        sender = msg_packet['sender']
        sender_clock = msg_packet['matrix_clock']
        # Check if all necessary conditions are met for message delivery
        for k in range(self.total_processes):
            if k != sender:
                if sender_clock[k][sender] > self.matrix_clock[k][sender]:
                    return False
        if sender_clock[sender][sender] != self.matrix_clock[sender][sender] + 1:
            return False
        return True

    def send_message(self, recipient, message):
        # Send the message to the recipient
        self.increment_clock()
        msg_packet = {
            'sender': self.pid,
            'message': message,
            'matrix_clock': [row[:] for row in self.matrix_clock]
        }
        print(f"Process {self.pid} sent '{message}' to Process {recipient.pid}\nMatrix Clock: {msg_packet['matrix_clock']}\n")
        recipient.receive_message(msg_packet)

    def run(self, recipients):
        # Simulate sending messages randomly
        for _ in range(5):
            recipient = random.choice(recipients)
            message = f"Message from {self.pid}"
            self.send_message(recipient, message)
            time.sleep(random.uniform(0.2, 0.5))

def main():
    num_processes = 3
    # Create processes
    processes = [MatrixProcess(i, num_processes) for i in range(num_processes)]

    # Set recipients excluding the sender
    threads = [threading.Thread(target=p.run, args=(processes[:p.pid] + processes[p.pid+1:],)) for p in processes]

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
