from user_interfaces import command_line
from core import factory


if __name__ == "__main__":

    # Creating an instance of the CommandProcessor
    processor = command_line.CommandProcessor(factory.factory)

    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() == "exit":
            break

        result = processor.process_command(user_input)
        print(result)
