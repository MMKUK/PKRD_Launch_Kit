# Quantum-Resistant Ledger (QRL) Integration

This module integrates a quantum-resistant ledger using XMSS (eXtended Merkle Signature Scheme) to secure PKRD transactions.

## Features
- Quantum-safe digital signatures.
- Uses XMSS to secure account keys and transactions.
- Prevents vulnerabilities from quantum computing.

## Files
- `install.sh`: Installs dependencies.
- `qrl_engine.py`: Core engine for QRL operations.

## Usage
Run `install.sh` to install XMSS library and register the engine.# Quantum-Resistant Ledger Module (PKRD Blockchain)

## Overview
The Quantum-Resistant Ledger (QRL) module is designed to provide post-quantum security for the PKRD blockchain by implementing cryptographic techniques resistant to quantum computing attacks.

## Key Features
- **XMSS Signature Support**: Implements eXtended Merkle Signature Scheme.
- **Key Rotation**: Ensures cryptographic hygiene over long periods.
- **Quantum Attack Audit Log**: Monitors anomaly patterns potentially linked to quantum attempts.

## Benefits
- Protection from Shor’s and Grover’s algorithm attacks
- Secure messaging, signing, and validation
- Seamless integration with PKRD nodes

## Integration
This module works as an extension to your node. Use `install_qrl.sh` to add QRL to any active PKRD node. Requires Python 3.10+.
