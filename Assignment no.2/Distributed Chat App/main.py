# Import the ChatProcess class to simulate chat participants
from chat_process import ChatProcess
# Import threading to allow concurrent execution of chat processes
import threading

# Main function to start the simulation
def main():
    # Define how many chat processes (participants) to simulate
    num_processes = 3

    # Create chat processes with unique IDs and total number of processes
    processes = [ChatProcess(i, num_processes) for i in range(num_processes)]

    # List to hold thread references for parallel execution
    threads = []

    # Start each chat process in a separate thread
    for p in processes:
        # Create a thread for the current process, passing all other processes as potential recipients
        t = threading.Thread(target=p.run, args=([r for r in processes if r.id != p.id],))
        threads.append(t)  # Add thread to the list
        t.start()          # Start thread execution

    # Wait for all threads to complete before exiting
    for t in threads:
        t.join()

# Entry point of the Python script
if __name__ == "__main__":
    main()
