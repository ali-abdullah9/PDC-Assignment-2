import threading
import time
import random

class Process:
    def __init__(self, id, num_processes):
        """
        Initialize a process with an ID, the number of processes, a vector clock, and a message buffer.
        """
        self.id = id
        self.num_processes = num_processes
        self.vector_clock = [0] * num_processes
        self.buffer = []
        self.lock = threading.Lock()

    def send_message(self, recipient):
        """
        Send a message to another process, updating the sender's vector clock.
        """
        with self.lock:
            self.vector_clock[self.id] += 1
            timestamped_message = (self.id, self.vector_clock.copy())
            print(f"Process {self.id} sent message to Process {recipient.id}: {timestamped_message}")
            recipient.receive_message(timestamped_message)

    def receive_message(self, timestamped_message):
        """
        Receives a message and checks if it can be delivered immediately or needs to be buffered.
        """
        with self.lock:
            sender_id, timestamp = timestamped_message
            if self.can_deliver(timestamp):
                self.deliver_message(sender_id, timestamp)
            else:
                print(f"Process {self.id} buffered message from Process {sender_id}: {timestamped_message}")
                self.buffer.append(timestamped_message)

    def can_deliver(self, timestamp):
        """
        Determines if the received message can be immediately delivered based on the vector clock logic.
        """
        for i in range(self.num_processes):
            if i == self.id:
                if self.vector_clock[i] + 1 != timestamp[i]:
                    return False
            else:
                if self.vector_clock[i] < timestamp[i]:
                    return False
        return True

    def deliver_message(self, sender_id, timestamp):
        """
        Delivers the message and updates the vector clock.
        """
        print(f"Process {self.id} delivered message from Process {sender_id}: {timestamp}")
        for i in range(self.num_processes):
            self.vector_clock[i] = max(self.vector_clock[i], timestamp[i])
        self.check_buffer()

    def check_buffer(self):
        """
        Checks buffered messages to see if they can now be delivered.
        """
        for buffered_msg in self.buffer[:]:
            if self.can_deliver(buffered_msg[1]):
                self.buffer.remove(buffered_msg)
                self.deliver_message(*buffered_msg)

def simulate_processes(num_processes, num_messages):
    """
    Simulates multiple processes communicating using vector clocks.
    """
    processes = [Process(i, num_processes) for i in range(num_processes)]

    def process_behavior(process):
        for _ in range(num_messages):
            recipient = random.choice([p for p in processes if p.id != process.id])
            process.send_message(recipient)
            time.sleep(random.uniform(0.1, 0.5))

    threads = [threading.Thread(target=process_behavior, args=(process,)) for process in processes]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    simulate_processes(num_processes=3, num_messages=5)
