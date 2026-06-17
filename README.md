# cpu-stress-test

A simple Python CPU stress test tool using multithreading.

## Features

- Stress test CPU with multiple threads
- Customizable duration and thread count
- Auto-detects CPU core count
- No external dependencies

## Usage

```bash
# Default (10 seconds, all cores)
python stress.py

# Custom duration (30 seconds)
python stress.py 30

# Custom duration and thread count
python stress.py 60 4
```

## Example Output

```
========================================
       CPU STRESS TEST
========================================
  Threads  : 8
  Duration : 10s
  CPU cores: 8
========================================

Running... Press Ctrl+C to stop early.

  Time remaining: 3s

========================================
  Stress test complete.
========================================
```

## Requirements

- Python 3.x

## Warning

This tool will max out your CPU during the test. Make sure your system has adequate cooling.
