#!/bin/bash
echo "[PKRD] Installing Quantum-Resistant Ledger module..."
mkdir -p ~/.pkrd/modules/quantum
cp quantum_ledger.py ~/.pkrd/modules/quantum/
echo "[PKRD] QRL module installed at ~/.pkrd/modules/quantum"
