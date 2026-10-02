# Peer Learning Day: Key-Value Store (Redis)

This repository contains the research summary and Proof of Concept (POC) for the **Key-Value Data Model** using **Redis**, developed as part of the Holberton School Peer Learning Day (PLD).

---

## 📋 Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Environment Setup](#environment-setup)
5. [Proof of Concept (POC)](#proof-of-concept-poc)
6. [Key Concepts Covered](#key-concepts-covered)

---

## 🎯 Overview

The goal of this project is to explore and demonstrate the fundamentals of **Key-Value databases** compared to traditional relational models (RDBMS). Using **Redis**, an in-memory key-value data store, we showcase core CRUD operations, complex data types (Hashes), automated data eviction using Time-To-Live (TTL), and manual key deletion.

---

## 📁 Project Structure

```
.
├── README.md               # Project documentation and setup guide
├── RESEARCH_SUMMARY.md     # In-depth theoretical research on Key-Value stores
└── poc.py                  # Python script demonstrating Redis capabilities
```

---

## 🛠️ Prerequisites

Ensure you have the following installed on your system:
- **Docker**
- **Python 3.x**
- **pip**

---

## 🚀 Environment Setup

### 1. Launch Redis with Docker
To isolate the database environment, run an official Redis Alpine container mapped to default port `6379`:

```bash
docker run -d --name redis-pld -p 6379:6379 redis:alpine
```

Verify that the container is active:
```bash
docker ps
```

### 2. Install Python Dependencies
Install the official Python Redis client (`redis-py`). If you encounter managed environment restrictions (PEP 668), use either a virtual environment or the system override flag:

```bash
pip install redis --break-system-packages
```

---

## 💻 Proof of Concept (POC)

To execute the demonstration script, ensure the Docker container is running, then execute:

```bash
python3 poc.py
```

### Script Workflow:
1. **Connection**: Establishes a TCP connection to the Redis server running on `localhost:6379`.
2. **CREATE & UPDATE**: Assigns and overwrites simple string values using `SET` and `GET`.
3. **HASH**: Demonstrates complex object-like structures using `HSET` and retrieves all fields via `HGETALL`.
4. **TTL & Expiration**: Sets a key with an explicit expiration time (`ex=10`), monitors remaining TTL with `TTL`, and verifies automatic purging after timeout.
5. **DELETE**: Manually removes keys from memory using `DELETE` and validates immediate deletion.

---

## 💡 Key Concepts Covered

- **In-Memory Storage & $O(1)$ Complexity**: Instant read/write access bypassing disk I/O bottlenecks.
- **Schemaless Data Modeling**: Dynamic storage without predefined table structures or strict data types.
- **Data Eviction (TTL)**: Automatic memory management for sessions, tokens, and temporary cache.
- **Hashes vs. Strings**: Efficient representation of structured entity attributes under a single parent key.

---

## 👥 Contributors

* **RebornLPB**: [github.com/RebornLPB](https://github.com/RebornLPB)
* **HeroFactory16**: [github.com/HeroFactory16](https://github.com/HeroFactory16)
* **Jean**: [github.com/tanacohid](https://github.com/tanacohid)
