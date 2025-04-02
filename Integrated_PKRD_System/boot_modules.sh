#!/bin/bash

echo "🔧 Booting all PKRD Modules..."
echo "➡️  Starting zk-RingCT..."
python3 ~/Desktop/Khan10/zkRingCT/zk_ringct_core.py

echo "➡️  Starting AI Consensus..."
python3 ~/Desktop/Khan10/AI_Consensus/ai_consensus_core.py

echo "➡️  Starting Genesis Watchdog..."
python3 /usr/local/pkrd/genesis_monitor/genesis_watchdog.py

echo "✅ All PKRD Modules executed."
