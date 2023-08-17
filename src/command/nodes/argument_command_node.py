from typing import TypeVar

from command.nodes.command_node import CommandNode
from command.command_context import CommandContext
from command.arguments.argument_type import ArgumentType
from command.exceptions import ArgumentException
from command.command_source import S

T = TypeVar('T')


class ArgumentCommandNode(CommandNode[S, 'ArgumentCommandNode']):
    name: str
    arg_type: ArgumentType[T]

    def __init__(self, name: str, arg_type: ArgumentType[T]):
        self.name = name
        self.arg_type = arg_type

    def instanceof(self, node: str, context: CommandContext[S]) -> bool:
        try:
            arg = self.arg_type.parse(node)
            context.arguments[self.name] = arg
        except ArgumentException:
            return False
        return True