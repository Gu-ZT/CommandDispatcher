from command.command_source import S
from command.nodes.command_node import CommandNode
from command.command_context import CommandContext


class LiteralCommandNode(CommandNode[S, 'LiteralCommandNode']):
    literal: str

    def __init__(self, literal: str):
        self.literal = literal

    def instanceof(self, node: str, context: CommandContext[S]) -> bool:
        return node == self.literal
