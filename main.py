import os
from dotenv import load_dotenv
import sys

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

def farewell(name):
    """Return a farewell message for the given name."""
    return f"Goodbye, {name}!"

def main():
    # Load environment variables from .env (if it exists)
    load_dotenv()

    # Get a default name from the .env file or use "World"
    default_name = os.environ.get("DEFAULT_NAME", "World")
    
    # If a name is provided as a command-line argument, use that; otherwise, use the default
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = default_name

    # Generate greeting and farewell messages
    greeting = greet(name)
    goodbye = farewell(name)

    # Print the messages
    print(greeting)
    print(goodbye)

if __name__ == "__main__":
    main()
