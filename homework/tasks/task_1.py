import asyncio
from asyncio import Task
from typing import Callable, Coroutine, Any


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):
        result = await asyncio.create_task(f())
    elif isinstance(f, Task):
        result = await f
    elif isinstance(f, Coroutine):
        result = await asyncio.create_task(f)
    else:
        raise ValueError('invalid argument')

    return result
