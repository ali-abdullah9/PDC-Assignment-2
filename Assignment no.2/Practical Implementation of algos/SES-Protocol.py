import threading
import random
import time

class Process:
    def __init__(self, pid, num_processes):
        """
        Initialize a process with a unique identifier and a vector clock.
        """
        self.pid = pid
        self.num_processes = num_processes
        self.vector_clock = [0] * num_processes
        self.lock = threading.Lock()

    def send_message(self, recipient):
        """
        Simulate sending a message to another process, incrementing the sender's vector clock.
        """
        with self.lock:
            self.vector_clock[self.pid] += 1
            timestamped_message = (self.pid, self.vector_clock.copy())
            print(f"Process {self.pid} sent message to Process {recipient.pid} with Vector Clock: {timestamped_message[1]}")
            recipient.receive_message(timestamped_message)

    def receive_message(self, timestamped_message):
        """
        Process receiving a message, updates its vector clock, and then delivers the message.
        """
        sender_id, received_clock = timestamped_message
        with self.lock:
            # Update vector clock based on received message
            for i in range(self.num_processes):
                self.vector_clock[i] = max(self.vector_clock[i], received_clock[i])
            self.vector_clock[self.pid] += 1
            self.deliver_message(sender_id, received_clock)

    def deliver_message(self, sender_id, timestamp):
        """
        Delivers a message and logs the event.
        """
        print(f"Process {self.pid} delivered message from Process {sender_id} with Vector Clock: {timestamp}")

def simulate_processes(num_processes, num_messages):
    processes = [MatrixProcess(i, num_processes) for i in range(num_processes)] # type: ignore

    def process_behavior(process):
        for _ in range(num_messages):
            recipient = random.choice([p for p in processes if p.pid != process.pid])
            process.send_message(recipient)
            time.sleep(random.uniform(0.1, 0.5))

    threads = []
    for process in processes:
        thread = threading.Thread(target=process_behavior, args=(process,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    simulate_processes(3, 5)
