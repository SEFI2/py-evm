from eth.vm.forks.frontier.computation import (
    FRONTIER_PRECOMPILES
)
from eth.vm.forks.frontier.computation import (
    FrontierComputation,
)

from .opcodes import NOGAS_OPCODES

# MUIR_GLACIER_PRECOMPILES = ISTANBUL_PRECOMPILES
NOGAS_PRECOMPILES = FRONTIER_PRECOMPILES


class NogasComputation(FrontierComputation):
    """
    A class for all execution computations in the ``MuirGlacier`` fork.
    Inherits from :class:`~eth.vm.forks.constantinople.istanbul.IstanbulComputation`
    """
    # Override
    opcodes = NOGAS_OPCODES
    _precompiles = NOGAS_PRECOMPILES
