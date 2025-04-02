#!/bin/bash

echo "🚀 Booting PKRD Blockchain Modules..."

# Module 1: zk-RingCT Privacy
echo "🔐 Starting zk-RingCT Privacy..."
python3 ~/Desktop/Khan10/zkRingCT/zk_ringct_core.py &

# Module 2: AI Consensus
echo "🧠 Starting AI Consensus Engine..."
python3 ~/Desktop/Khan10/AI_Consensus/ai_consensus_core.py &

# Module 3: Genesis Integrity Watchdog
echo "🛡 Launching Genesis Watchdog..."
python3 ~/Desktop/Khan10/GenesisMonitor/genesis_watchdog.py &

# Module 4: Geth Node with Founder Wallet
echo "⚙️  Launching PKRD Node..."
docker run --rm -it \
  -v ~/PKRD_GETH_DATA:/root/.ethereum \
  ethereum/client-go:v1.13.15 \
  --datadir /root/.ethereum \
  --networkid 98765 \
  --http --http.addr "0.0.0.0" --http.port 8545 \
  --http.api personal,eth,net,web3,miner,clique \
  --http.vhosts="*" \
  --allow-insecure-unlock \
  --unlock 0x6a517CCcf02eE802FAfDd0b9E3AC9ab039ccd465 \
  --password /root/.ethereum/password.txt \
  --mine --miner.etherbase 0x6a517CCcf02eE802FAfDd0b9E3AC9ab039ccd465 \
  --ipcdisable \
  console
