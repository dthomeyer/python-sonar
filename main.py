# main.py

def say_hello(name):
    """
    A simple function to greet a person.
    There is a small intentional issue here for Sonar demo purposes (unused variable).
    """
    greeting = f"Hello, {name}!"
    unused_variable = 42 # This line is here to trigger a SonarLint warning
    print(greeting)
    return greeting

if __name__ == "__main__":
    # Example usage
    say_hello("World")
