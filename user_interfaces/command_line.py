class CommandProcessor:
    def __init__(self, target_class):
        self.target = target_class()

    def process_command(self, command):
        # Split the command into method name and arguments
        parts = command.split()
        method_name = parts[0]
        args = parts[1:]

        # Check if the method exists in the target class
        if hasattr(self.target, method_name):
            method = getattr(self.target, method_name)

            # Call the method with the given arguments
            try:
                result = method(*args)
                return result
            except Exception as e:
                return f"Error executing command: {str(e)}"
        else:
            return f"Invalid command: {method_name} is not a valid method."

if __name__ == "__main__":
    # Example usage:
    class UserDefinedClass:
        def hello(self, name):
            return f"Hello, {name}!"

        def add(self, a, b):
            return int(a) + int(b)

    # Creating an instance of the CommandProcessor
    processor = CommandProcessor(UserDefinedClass)

    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() == "exit":
            break

        result = processor.process_command(user_input)
        print(result)
