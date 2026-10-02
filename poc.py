#!/usr/bin/python3

import redis
import time

def main():
    # Establish connection to local Redis instance running on default port 6379
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    print("PROOF OF CONCEPT - Key-Value")
    print("\n")

    # ----------------------------------------------------
    # 1. CREATE Operation (String Data Type)
    # ----------------------------------------------------
    # Inserts a standard key-value pair into Redis
    r.set("user:1", "Betty",)
    print(f"Create: Key 'user:1' created with the value: {r.get('user:1')}")

    # ----------------------------------------------------
    # 2. UPDATE Operation (Overwriting Existing Key)
    # ----------------------------------------------------
    # Overwrites the value associated with 'user:1'
    r.set("user:1", "Kevin")
    print(f"Update: Key 'user:1' updated: {r.get('user:1')}")

    # ----------------------------------------------------
    # 3. HASH Structure (Complex Field-Value Pairs)
    # ----------------------------------------------------
    # Stores a dictionary structure under a single key ('user:2:info')
    r.hset("user:2:info", mapping={
        "email": "Thomas@holberton.com",
        "role": "swe",
        "age": "1337"
    })
    print(f"Hash: info updated for 'user:1:info' : {r.hgetall("user:1:info")}")

    # ----------------------------------------------------
    # 4. TTL (Time-To-Live) & Expiration Mechanisms
    # ----------------------------------------------------
    # Sets 'user:3' with an automated expiration timer of 10 seconds (ex=10)
    r.set('user:3', 'Karine', ex=10)
    print(f"TTL: Value with 10 seconds TTL for 'user:3' : {r.get('user:3')}")

    # Pause execution for 7 seconds to check active countdown
    time.sleep(7)
    print(f"TTL: 'user:3' remaining time : {r.ttl('user:3')} seconds")

    # Pause execution for 4 more seconds (total 11s) to demonstrate automatic deletion
    time.sleep(4)
    print(f"TTL: 'user:3' is active ? : {r.get('user:3')}")

    # ----------------------------------------------------
    # 5. DELETE Operation (Manual Key Purging)
    # ----------------------------------------------------
    # Retrieve Hash content before removal
    print(f"Delete: Data to delete: {r.hgetall('user:2:info')}")

    # Remove the key 'user:2:info' from memory
    r.delete('user:2:info')

    # Confirm key deletion (returns an empty dictionary {})
    print(f"Delete: After deletion: {r.hgetall('user:2:info')}")


main()
