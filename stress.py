import threading
import time
import sys
import os
import multiprocessing

stop_flag = False

def stress_worker():
    while not stop_flag:
        _ = sum(i * i for i in range(10000))

def run_stress(duration=10, threads=None):
    global stop_flag
    stop_flag = False

    if threads is None:
        threads = multiprocessing.cpu_count()

    print("\n" + "=" * 40)
    print("       CPU STRESS TEST")
    print("=" * 40)
    print(f"  Threads  : {threads}")
    print(f"  Duration : {duration}s")
    print(f"  CPU cores: {multiprocessing.cpu_count()}")
    print("=" * 40)
    print("\nRunning... Press Ctrl+C to stop early.\n")

    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=stress_worker, daemon=True)
        t.start()
        thread_list.append(t)

    try:
        for i in range(duration, 0, -1):
            print(f"  Time remaining: {i}s", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nStopped by user.")

    stop_flag = True
    for t in thread_list:
        t.join(timeout=1)

    print("\n" + "=" * 40)
    print("  Stress test complete.")
    print("=" * 40 + "\n")

if __name__ == "__main__":
    duration = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    threads = int(sys.argv[2]) if len(sys.argv) > 2 else None
    run_stress(duration, threads)
