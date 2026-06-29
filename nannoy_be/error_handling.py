# Create a script that intentionally triggers a TypeError inside a nested function call. Run it and identify which file and line caused the error versus which line initiated the sequence.
# Modify the script to pass a None value into a function that expects a list, forcing an AttributeError. Practice identifying the exact object that lacked the expected attribute.
# Experiment with deep recursion (e.g., a function that calls itself 2000 times). Observe the RecursionError traceback and identify how Python truncates long call stacks.

def main(a , b): 
    a = 10
    b = "abc"
    return a + b 
if __name__ == "__main__":
    main(a,b)   

def main()     