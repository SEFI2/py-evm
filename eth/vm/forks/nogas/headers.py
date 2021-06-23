from eth.vm.forks.petersburg.headers import (
    compute_difficulty,
)
from eth.vm.forks.berlin.headers import (
    configure_header,
    create_header_from_parent,
)


compute_nogas_difficulty = compute_difficulty(9000000)

create_nogas_header_from_parent = create_header_from_parent(
    compute_nogas_difficulty
)
configure_nogas_header = create_header_from_parent(compute_nogas_difficulty)
