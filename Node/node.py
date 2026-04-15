"""
PrivacyNet Lab - node.py
========================
Phase 1: Two-node encrypted communication.
Node A encrypts a message and sends it to Node B.
Node B decrypts and prints what it can see.

Educational use only — runs entirely on localhost.
"""

import socket  #It is a way to create network connection in python. It works like 
                       #a telephone; one side calls and other side picks up 

import threading   # Normally python works one thing at a time top to bottom but here
                            #when node A sends node b needs to listen it at the same time
                            #so threading is used to make both work at the same time creating two hands

import os            #here is it only used for os.urandom(16) to create a random 16 bytes using the os randomness function

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad  # AES -> Advance Encrption Standard. Is used as the encryption algorithm in this project
                                      #AES requires the data to be in the chunks of 16 bytes. for expample: If the message is 37 bytes
                                       #the padding (pad) fills it to 48 bits (3 chunks of 16 bytes) and while unpadding (unpad) it will remove the 
                                       #unnecessery bytes afetr decryption.

import hashlib   #used to turn plain password to 32 bytes; the size requires for the key of AES-256
                    #Secure Hash Algorithm - SHA-256 is used which provides excatly 32 bytes regradless the input lenght


# ── Config ───────────────────────────────────────────────────────────────────
NODE_A_PORT = 5001
NODE_B_PORT = 5002
HOST        = "127.0.0.1"

# Shared key (in Phase 2 this will be exchanged via Diffie-Hellman)
# For now both nodes know the same key — keep it simple
RAW_KEY = "privacynet-phase1-key"
KEY     = hashlib.sha256(RAW_KEY.encode()).digest()  # 32 bytes = AES-256


# ── Encryption helpers ───────────────────────────────────────────────────────
def encrypt(message: str, key: bytes) -> bytes:
    """Encrypt a message using AES-256 CBC mode."""
    iv     = os.urandom(16)                          # random initialisation vector
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct     = cipher.encrypt(pad(message.encode(), AES.block_size))
    return iv + ct                                   # prepend IV so receiver can decrypt


def decrypt(data: bytes, key: bytes) -> str:
    """Decrypt an AES-256 CBC message."""
    iv     = data[:16]                               # first 16 bytes = IV
    ct     = data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()


# ── Node B — the receiver ────────────────────────────────────────────────────
def run_node_b():
    """
    Node B listens for incoming encrypted traffic.
    It only knows its own decryption key.
    It prints exactly what it can see — demonstrating node isolation.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, NODE_B_PORT))
    server.listen(1)

    print(f"\n[Node B] Listening on {HOST}:{NODE_B_PORT}")
    print("[Node B] Waiting for incoming encrypted traffic...\n")

    conn, addr = server.accept()
    print(f"[Node B] Connection received from: {addr[0]}:{addr[1]}")
    print(f"[Node B] --- What this node can see ---")

    data = conn.recv(4096)
    print(f"[Node B] Raw encrypted bytes received : {data.hex()[:60]}...")

    try:
        plaintext = decrypt(data, KEY)
        print(f"[Node B] Decrypted message            : {plaintext}")
    except Exception as e:
        print(f"[Node B] Decryption failed: {e}")

    print(f"[Node B] --- End of node view ---\n")
    conn.close()
    server.close()


# ── Node A — the sender ──────────────────────────────────────────────────────
def run_node_a(message: str):
    """
    Node A encrypts a message and sends it to Node B.
    Node A does not know what Node B will do with it.
    """
    import time
    time.sleep(0.5)  # give Node B time to start listening

    print(f"[Node A] --- What this node can see ---")
    print(f"[Node A] Original message   : {message}")

    encrypted = encrypt(message, KEY)
    print(f"[Node A] Encrypted (hex)    : {encrypted.hex()[:60]}...")
    print(f"[Node A] Sending to Node B at {HOST}:{NODE_B_PORT}...\n")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, NODE_B_PORT))
    client.send(encrypted)
    client.close()

    print(f"[Node A] --- End of node view ---\n")


# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  PrivacyNet Lab — Phase 1: Two-Node Encrypted Comms")
    print("=" * 55)

    message = "Hello from Node A — this is encrypted!"

    # Run Node B in a background thread, Node A in main thread
    thread_b = threading.Thread(target=run_node_b)
    thread_b.start()

    run_node_a(message)

    thread_b.join()

    print("=" * 55)
    print("  Demo complete.")
    print("  Next step: add a third node and strip one layer each.")
    print("=" * 55)
