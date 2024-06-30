from itertools import islice
from typing import Any, List, Iterable


def batches(iterable: Iterable[Any], batch_size: int) -> Iterable[List[Any]]:
    iterator = iter(iterable)

    while True:
        batch = list(islice(iterator, batch_size))

        if not batch:
            return

        yield batch
