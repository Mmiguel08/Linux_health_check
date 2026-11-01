# Server Health Monitoring Agent

A lightweight Linux Server Monitoring Agent developed in Python using the `psutil` library. The application collects essential system health metrics, providing visibility into CPU performance, memory utilization, disk usage, and network statistics.

## Overview

The Server Health Monitoring Agent collects system performance information from a Linux environment and displays the results in the terminal.

The current implementation has been tested in a WSL2 Ubuntu environment, successfully collecting CPU, memory, disk, and network interface information.

## Features

### 1. CPU Monitoring

- CPU utilization percentage.
- Number of logical CPU cores.
- System load averages (1, 5 and 15 minutes).
- CPU context switches.
- CPU interrupts.

### 2. Memory Monitoring

- Total memory.
- Available memory.
- Used memory.
- Free memory.

### 3. Disk Monitoring

- Disk device identification.
- Mount point.
- Filesystem type.
- Total disk capacity.
- Used disk space.
- Available disk space.
- Disk utilization percentage.

### 4. Network Monitoring

- Total packets sent.
- Total packets received.
- Input errors.
- Output errors.
- Input packet drops.
- Output packet drops.
- Network interface identification.
- IPv4 addresses.
- IPv6 addresses.
- MAC addresses.

## Technologies

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| psutil | System resource monitoring |
| socket | Network address identification |
| Linux / WSL2 | Testing environment |

## Project Structure

```text
server-health-monitor/
│
├── server_agent.py
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/server-health-monitor.git
cd server-health-monitor
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the environment

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install psutil
```

## Usage

Run the monitoring agent:

```bash
python3 server_agent.py
```

## Test Environment

The following results were collected during an actual execution in a WSL2 Ubuntu environment.

### CPU Metrics

| Metric | Collected Value |
|---|---:|
| CPU Usage | 0.2% |
| Logical CPUs | 8 |
| Load Average (1 min) | 0.0 |
| Load Average (5 min) | 0.000488 |
| Load Average (15 min) | 0.0 |
| CPU Context Switches | 3,848,900 |
| CPU Interrupts | 3,612,947 |

### Memory Metrics

| Metric | Collected Value |
|---|---:|
| Total Memory | 7.45 GiB |
| Available Memory | 6.65 GiB |
| Used Memory | 6.44 GiB |
| Free Memory | 88 MiB |

### Disk Metrics

| Metric | Collected Value |
|---|---|
| Device | /dev/sdd |
| Mount Point | / |
| Filesystem | ext4 |
| Total Capacity | 1006.5 GiB |
| Used Space | 5.22 GiB |
| Free Space | 950.4 GiB |
| Usage Percentage | 0.5% |

Additional detected mount:

| Metric | Value |
|---|---|
| Device | /dev/sdd |
| Mount Point | /mnt/wslg/distro |
| Filesystem | ext4 |

### Network Metrics

#### Traffic Statistics

| Metric | Collected Value |
|---|---:|
| Packets Sent | 1,171 |
| Packets Received | 5,170 |
| Input Errors | 0 |
| Output Errors | 0 |
| Input Drops | 0 |
| Output Drops | 2 |

#### Detected Network Interfaces

| Interface | IPv4 Address | IPv6 Address |
|---|---|---|
| lo | 127.0.0.1, 10.255.255.254 | ::1 |
| eth0 | 172.18.104.198 | fe80::215:5dff:fe00:e9ec |
| docker0 | 172.17.0.1 | Not assigned |

#### MAC Addresses

| Interface | MAC Address |
|---|---|
| lo | 00:00:00:00:00:00 |
| eth0 | 00:15:5d:00:e9:ec |
| docker0 | ca:46:52:a6:ae:f1 |

## Project Objectives

- Develop practical Python system monitoring skills.
- Understand Linux resource utilization.
- Explore network interface statistics.
- Learn how to retrieve operating system metrics programmatically.
- Build a foundation for centralized infrastructure monitoring.


## License

This project is intended for educational and research purposes.

---

**Author:** Moises Miguel

**Technologies:** Python | Linux | Networking | System Monitoring | Cybersecurity