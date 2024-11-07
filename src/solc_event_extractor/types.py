from typing import List
from dataclasses import dataclass


@dataclass
class ContractInput:
    """
    Represents an input parameter for a contract function or event.

    Attributes:
        name (str): Name of the input parameter
        type (str): Data type of the input parameter
        indexed (bool, optional): Whether the input is indexed (for events)
    """
    name: str = ''
    type: str = ''
    indexed: bool = False


@dataclass
class ContractEvent:
    """
    Represents a contract event with its details.

    Attributes:
        name (str): Name of the event
        signature (str): Full signature of the event
        inputs (List[ContractInput]): Input parameters of the event
    """
    name: str
    signature: str
    inputs: List[ContractInput]


@dataclass
class ContractFunction:
    """
    Represents a contract function with its details.

    Attributes:
        name (str): Name of the function
        signature (str): Full signature of the function
        inputs (List[ContractInput]): Input parameters of the function
        outputs (List[ContractInput]): Output parameters of the function
        stateMutability (str): State mutability of the function
    """
    name: str
    signature: str
    inputs: List[ContractInput]
    outputs: List[ContractInput]
    stateMutability: str
