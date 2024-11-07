# Solc Event Extractor
Solc Event Extractor is a Python library for extracting metadata (events and functions) from Solidity contracts. It allows you to parse Solidity source files or URLs pointing to Solidity code and retrieve detailed information about contract events and functions.

# Features
* Extracts events and functions from Solidity contracts.
* Supports both local files and URLs.
* Handles different Solidity compiler versions.
* Provides detailed metadata including inputs, outputs, and state mutability.

# Installation
You can install the library via pip:

`bash
uv pip install solc-event-extractor
`

# Usage
In order to use the library, provide a raw github contract path or filepath to a .sol file. Make sure that the correct solidity version is also selected. 
```python
from solc_event_extractor import extract_contract_details

contract_source = 'path/to/your/contract.sol'
details = extract_contract_details(contract_source, version='0.8.26')

if details:
    print("Events:")
    for event in details['events']:
        print(f" - {event.name}: {event.signature}")

    print("\nFunctions:")
    for function in details['functions']:
        print(f" - {function.name}: {function.signature}")
else:
    print("Failed to extract contract details.")
```