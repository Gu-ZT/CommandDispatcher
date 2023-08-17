from typing import Callable, Coroutine, Any

from command.command_source import S
from command.command_context import CommandContext

Command = Callable[[CommandContext[S]], Coroutine[Any, Any, Any]]
