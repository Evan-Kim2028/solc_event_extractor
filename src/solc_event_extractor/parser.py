import requests
import os
import tempfile
import solcx
import urllib.parse
from typing import Dict, List, Optional, Union

from solc_event_extractor.types import ContractInput, ContractEvent, ContractFunction


def extract_contract_details(
    contract_source: str,
    version: str = '0.8.26'
) -> Optional[Dict[str, List[Union[ContractEvent, ContractFunction]]]]:
    """
    Extract metadata (events and functions) from a Solidity contract.

    Args:
        contract_source (str): URL or local file path of the Solidity contract
        version (str, optional): Solidity compiler version. Defaults to '0.8.26'

    Returns:
        Optional dictionary with 'events' and 'functions' or None if extraction fails

    Raises:
        FileNotFoundError: If local contract file does not exist
        requests.RequestException: If contract URL cannot be downloaded
    """
    try:
        # Determine if source is a URL or local file path
        if contract_source.startswith(('http://', 'https://')):
            # URL handling
            response = requests.get(contract_source)
            response.raise_for_status()

            # Use URL-based filename
            parsed_url = urllib.parse.urlparse(contract_source)
            filename = os.path.basename(parsed_url.path) or 'contract.sol'

            # Create temporary file
            with tempfile.NamedTemporaryFile(mode='w', prefix=filename, suffix='.sol', delete=False) as temp_file:
                temp_file.write(response.text)
                temp_file_path = temp_file.name
        else:
            # Local file path handling
            if not os.path.exists(contract_source):
                raise FileNotFoundError(
                    f"Contract file not found: {contract_source}")

            temp_file_path = contract_source

        try:
            # Install and set Solidity compiler version
            if version not in solcx.get_installed_solc_versions():
                solcx.install_solc(version)
            solcx.set_solc_version(version)

            # Compile contract
            compiled_sol = solcx.compile_files(
                [temp_file_path],
                output_values=['abi', 'bin']
            )

            # Process contract details
            # Take the first (and typically only) contract from the compilation
            contract_name = list(compiled_sol.keys())[0]
            abi = compiled_sol[contract_name]['abi']

            # Extract Events
            events = [
                ContractEvent(
                    name=event['name'],
                    signature=f"{event['name']}({', '.join([f'{"indexed " if inp.get("indexed", False) else ""}{
                        inp["type"]} {inp.get("name", "")}'.strip() for inp in event.get("inputs", [])])})",
                    inputs=[
                        ContractInput(
                            name=inp.get('name', ''),
                            type=inp['type'],
                            indexed=inp.get('indexed', False)
                        ) for inp in event.get('inputs', [])
                    ]
                )
                for event in abi if event['type'] == 'event'
            ]

            # Extract Functions
            functions = [
                ContractFunction(
                    name=func['name'],
                    signature=f"{func['name']}({','.join(
                        inp['type'] for inp in func.get('inputs', []))})",
                    inputs=[
                        ContractInput(
                            name=inp.get('name', ''),
                            type=inp['type']
                        ) for inp in func.get('inputs', [])
                    ],
                    outputs=[
                        ContractInput(
                            name=out.get('name', ''),
                            type=out['type']
                        ) for out in func.get('outputs', [])
                    ],
                    stateMutability=func.get('stateMutability', '')
                )
                for func in abi if func['type'] == 'function'
            ]

            # Return a clean dictionary with just events and functions
            return {
                'events': events,
                'functions': functions
            }

        finally:
            # Clean up the temporary file
            os.unlink(temp_file_path)

    except requests.RequestException as e:
        print(f"Error downloading contract: {e}")
        return None
    except Exception as e:
        print(f"Compilation error: {e}")
        return None
