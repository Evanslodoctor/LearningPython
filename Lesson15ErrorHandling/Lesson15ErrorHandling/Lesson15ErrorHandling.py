try:
    # Code that might raise an exception
    result = 10 / 1  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # Handle specific exception
    print("Error: {}".format(e))
except Exception as e:
    # Handle a more general exception
    print("General Error: {}".format(e))
else:
    # Code to be executed if the try block does not raise an exception
    print("No exception occurred.")
finally:
    # Code that will be executed no matter what
    print("This will be executed regardless of whether there was an exception.")
