import copy
from eth.vm.forks.frontier.opcodes import (
    FRONTIER_OPCODES,
)

NOGAS_OPCODES = copy.deepcopy(FRONTIER_OPCODES)
