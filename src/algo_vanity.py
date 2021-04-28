import argparse
import time
import signal
import sys
import os
import multiprocessing
from multiprocessing import Process, Queue, Value, Lock
from algosdk import account, mnemonic

# generates accounts and looks for a match for the provided pattern.
# queue and count are shared variables that can be updated from a
# subprocess
def find_address(pattern, queue, count):

    while True:
        with count.get_lock():
            count.value += 1

        # generate an account using algosdk
        private_key, address = account.generate_account()

        if address.startswith(pattern):
            queue.put((address, private_key))
            break

# handler for user ctrl-c action
def signal_handler(sig, frame):
    print("")
    print("No match in " + str(count.value) + " attempts and " + get_running_time() + " seconds")
    terminate_processes()
    sys.exit(1)

# calculate and format running time
def get_running_time():
    running_time = time.time() - start_time
    running_time_str = str(round(running_time, 2)) # float formatted to string with 2 decimal places
    return running_time_str

# cleanup spawned processes
def terminate_processes():
    for p in jobs:
        p.terminate()

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("pattern", type=str, help="Pattern to Look for at the start of an algorand address.")
    pattern = p.parse_args().pattern

    num_processors = multiprocessing.cpu_count()
    print("Detected " + str(num_processors) + " cpu(s)")

    start_time = time.time()
    count = Value('i', 0)
    queue = Queue()
    jobs = []

    # spawn number of address search processes equal to the number of processors on the system
    for i in range(num_processors):
        p = Process(target=find_address, args=(pattern, queue, count))
        jobs.append(p)
        p.start()

    signal.signal(signal.SIGINT, signal_handler) # capture ctrl-c so we can report attempts and running time

    address, private_key = queue.get() # this will return once one of the spawned processes finds a match
    if (address):
        print("Found a match for " + pattern + " after " + str(count.value) + " tries in " + get_running_time() + " seconds")
        print("Address: ", address)
        print("Private key: ", mnemonic.from_private_key(private_key))

    terminate_processes()
