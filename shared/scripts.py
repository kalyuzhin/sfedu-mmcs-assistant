import asyncio
from glob import glob


async def process_tasks_by_batches(data: list, batch_size: int, func) -> list:
    result = []
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        result.extend(await asyncio.gather(*(func(item) for item in batch)))
    return result
