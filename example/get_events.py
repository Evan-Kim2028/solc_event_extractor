from solc_event_extractor.parser import extract_contract_details
from pprint import pprint


def main():
    """
    Main function to demonstrate contract metadata extraction and event config generation.
    """
    contract_url = 'https://raw.githubusercontent.com/Uniswap/v3-core/refs/heads/main/contracts/interfaces/pool/IUniswapV3PoolEvents.sol'
    details = extract_contract_details(contract_url, version='0.7.1')

    if details:
        # Debug: Print raw details first
        print("Raw Contract Details:")
        pprint(details)

        # Check if events exist
        events = details.get('events', [])
        print(f"\nNumber of Events Found: {len(events)}")

        if not events:
            print("No events found in the contract!")
            return

        print("\nGenerated Event Configs:")
        # Pretty print the generated configurations
        pprint(events)
    else:
        print("Failed to extract contract details.")


# Call main directly if script is run
if __name__ == "__main__":
    main()
