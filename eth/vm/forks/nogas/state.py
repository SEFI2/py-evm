from eth.vm.forks.frontier.state import (
    FrontierState
)

from .computation import NogasComputation


class NogasState(FrontierState):
    computation_class = NogasComputation
