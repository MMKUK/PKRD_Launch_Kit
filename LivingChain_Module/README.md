# Living Chain Protocol

The Living Chain Protocol is a core resilience system for the PKRD Blockchain. It ensures the blockchain remains alive, healthy, and self-healing over time, without centralized oversight.

## Features

- 🔁 Heartbeat: Periodic health pings to check blockchain liveness
- 🛠️ Auto-repair: Auto-verifies state consistency and rebuilds broken chains
- ⛓️ Blockwatch: Detects stalled chains or unexpected halts
- 🧠 Optional hooks for AI oversight

## Usage

1. Run the `install.sh` script to install this module.
2. Execute `living_chain.py` to start heartbeat monitoring.
