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

Note library was generated with python 3.12.5 version, so earlier python versions might not be compatible.

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

## Example output:
```Raw Contract Details:
{'events': [ContractEvent(name='Burn',
                          signature='Burn(indexed address owner, indexed int24 '
                                    'tickLower, indexed int24 tickUpper, '
                                    'uint128 amount, uint256 amount0, uint256 '
                                    'amount1)',
                          inputs=[ContractInput(name='owner',
                                                type='address',
                                                indexed=True),
                                  ContractInput(name='tickLower',
                                                type='int24',
                                                indexed=True),
                                  ContractInput(name='tickUpper',
                                                type='int24',
                                                indexed=True),
                                  ContractInput(name='amount',
                                                type='uint128',
                                                indexed=False),
                                  ContractInput(name='amount0',
                                                type='uint256',
                                                indexed=False),
                                  ContractInput(name='amount1',
                                                type='uint256',
                                                indexed=False)]),
            ContractEvent(name='Collect',
                          signature='Collect(indexed address owner, address '
                                    'recipient, indexed int24 tickLower, '
                                    'indexed int24 tickUpper, uint128 amount0, '
                                    'uint128 amount1)',
                          inputs=[ContractInput(name='owner',
                                                type='address',
                                                indexed=True),
                                  ContractInput(name='recipient',
                                                type='address',
                                                indexed=False),
                                  ContractInput(name='tickLower',
                                                type='int24',
                                                indexed=True),
                                  ContractInput(name='tickUpper',
                                                type='int24',
                                                indexed=True),
                                  ContractInput(name='amount0',
                                                type='uint128',
                                                indexed=False),
                                  ContractInput(name='amount1',
                                                type='uint128',
                                                indexed=False)]),
                                                ....
                                                
]
}```