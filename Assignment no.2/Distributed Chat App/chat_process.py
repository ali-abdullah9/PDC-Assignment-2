import threading  # For managing concurrent execution of processes
import time       # To simulate delays between sending messages
import random     # To select recipients randomly and randomize message intervals

# Class representing each chat participant/process using vector clocks for causal ordering
class ChatProcess:
    def __init__(self, process_id, total_processes):
        # Unique identifier for the current process
        self.id = process_id
        
        # Vector clock initialized to zero for all processes
        self.vector_clock = [0] * total_processes

        # Buffer for temporarily storing messages that can't yet be delivered
        self.buffer = []

        # List to keep track of delivered messages
        self.delivered = []

        # Lock to ensure thread safety during concurrent vector clock updates and message handling
        self.lock = threading.Lock()

    # Method to send a message from current process to another recipient
    def send_message(self, message, recipient):
        with self.lock:
            # Increment the sender's own entry in the vector clock
            self.vector_clock[self.id] += 1

            # Prepare the message packet including sender id, content, and current vector clock
            msg = {
                'sender': self.id,
                'message': message,
                'vector_clock': self.vector_clock.copy()
            }

            # Log the sending action
            print(f"Process {self.id} sent '{message}' to Process {recipient.id} | VC: {msg['vector_clock']}")

            # Send message to recipient
            recipient.receive_message(msg)

    def receive_message(self, msg):
        with self.lock:
            # Upon receiving, check if the message can be delivered according to causal ordering rules
            if self.can_deliver(msg['vector_clock']):
                # Deliver immediately if conditions are met
                self.deliver(msg)
            else:
                # Otherwise, buffer the message for later delivery
                print(f"Process {self.id} buffering message '{msg['message']}' from Process {msg['sender']}")
                self.buffer.append(msg)

    def can_deliver(self, msg_vc, sender=None):
        """
        Check if a message can be delivered:
        For all processes k ≠ sender, msg_vc[k] <= local vector clock[k]
        and sender's timestamp is exactly one more than local timestamp for sender.
        """
        sender = sender if 'sender' in locals() else self.id
        for i in range(len(msg_vc)):
            if i == sender:
                if msg_vc[i] != self.vector_clock[i] + 1:
                    return False
            else:
                if msg_vc[i] > self.vector_clock[i]:
                    return False
        return True

    def deliver(self, msg):
        # Extract message details
        sender = msg['sender']
        message = msg['message']

        # Update local vector clock with sender's information
        self.vector_clock[sender] += 1

        # Log the delivery of the message
        print(f"Process {self.id} delivered '{message}' from Process {sender} | Updated VC: {self.vector_clock}")

        # Check if buffered messages can now be delivered
        self.check_buffer()

    def check_buffer(self):
        # Check buffered messages for delivery
        delivered_msgs = []
        for msg in self.buffer:
            if self.can_deliver(msg['vector_clock']):
                # Deliver the buffered message
                self.deliver_message(msg)
                delivered_msgs.append(msg)
        
        # Remove delivered messages from buffer
        for msg in delivered_msgs:
            self.buffer.remove(msg)

    def deliver_message(self, msg):
        # Deliver buffered message and update the vector clock accordingly
        sender = msg['sender']
        message = msg['message']
        self.vector_clock[sender] += 1

        print(f"Process {self.id} delivered buffered message '{message}' from Process {sender} | VC: {self.vector_clock}")

    # Method defining the behavior of each process (sending messages at random intervals)
    def run(self, recipients):
        messages = ["Hi", "How are you?", "Ready?", "Yes!", "Let’s start!"]

        # Loop through a predefined list of messages
        for message in messages:
            # Randomly select recipient from available processes
            recipient = random.choice(recipients)

            # Send the message
            self.send_message(message, recipient)

            # Introduce random delay to simulate asynchronous communication
            time.sleep(random.uniform(0.2, 0.6))
