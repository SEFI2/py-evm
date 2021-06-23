from typing import (
    Type,
)

from eth.rlp.blocks import BaseBlock
from eth.vm.forks.frontier import (
    FrontierVM,
)
from eth.vm.state import BaseState

from .blocks import NogasBlock
from .headers import (
    compute_nogas_difficulty,
    configure_nogas_header,
    create_nogas_header_from_parent,
)
from .state import NogasState


class NogasVM(FrontierVM):
    # fork name
    fork = 'nogas'

    # classes
    block_class: Type[BaseBlock] = NogasBlock
    _state_class: Type[BaseState] = NogasState

    # Methods
    create_header_from_parent = staticmethod(create_nogas_header_from_parent)  # type: ignore
    compute_difficulty = staticmethod(compute_nogas_difficulty)    # type: ignore
    configure_header = configure_nogas_header
