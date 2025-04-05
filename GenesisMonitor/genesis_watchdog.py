import time
import hashlib
import os

# ✅ Path to the Genesis JSON file
GENESIS_PATH = os.path.expanduser("~/Desktop/Khan10/PKRD_Blockchain_Genesis.json")

# ✅ Path to saved valid hash
HASH_PATH = os.path.expanduser("~/Desktop/Khan10/GenesisMonitor/.genesis_hash")

def compute_file_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
            return hashlib.sha256(file_data).hexdigest()
    except FileNotFoundError:
       import time
import hashlib
import os

# ✅ Set the paths
GENESIS_PATH = os.path.expanduser("~/Desktop/Khan10/PKRD_Blockchain_Genesis.json")
HASH_PATH = os.path.expanduser("~/Desktop/Khan10/GenesisMonitor/.genesis_hash")

def compute_file_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
            return hashlib.sha256(file_data).hexdigest()
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return None

def check_genesis_integrity():
    print("🔎 Monitoring Genesis Block integrity...")
    current_hash = compute_file_hash(GENESIS_PATH)

    if not current_hash:
        print("❌ Could not read Genesis file.")
        return

    try:
        with open(HASH_PATH, "r") as f:
            known_hash = f.read().strip()
    except FileNotFoundError:
        print("❌ .genesis_hash file not found.")
        return

    if current_hash != known_hash:
        print("⚠️ Genesis block has been tampered!")
    else:
        print("✅ Genesis block integrity verified.")

if __name__ == "__main__":
    while True:
        check_genesis_integrity()
        time.sleep(10)
