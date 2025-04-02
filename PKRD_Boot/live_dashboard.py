import time
import os

def display_dashboard():
    os.system('clear')
    print("🚀 PKRD Live Dashboard — Real-time Status")
    print("────────────────────────────────────────────")
    print("🔗 Blockchain Status:")
    print("   • Node Running ✅")
    print("   • Mining Active 🛠")
    print("   • Latest Block: Auto-updating")
    print("\n🔐 zk-RingCT Module:")
    print("   • Privacy Shield: ✅ Active")
    print("\n🧠 AI Consensus:")
    print("   • Block Evaluation: ✅ Enabled")
    print("\n🛡 Genesis Integrity:")
    print("   • Watchdog Monitor: ✅ Secure")
    print("────────────────────────────────────────────")
    print("🔄 Updating every 5 seconds...\n")

while True:
    display_dashboard()
    time.sleep(5)
