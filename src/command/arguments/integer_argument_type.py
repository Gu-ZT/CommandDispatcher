from command.arguments.argument_type import ArgumentType
from command.exceptions import ArgumentException


class IntegerArgumentType(ArgumentType[int]):
    def parse(self, reader: str) -> int:
        try:
            return int(reader)
        except ValueError:
            raise ArgumentException('argument is not a Integer')
