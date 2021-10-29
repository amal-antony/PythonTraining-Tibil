#USer Defined Ezxceptions
'''
We can name own exceptions by creating a new exception class.
Exceptions need to be derived from the Exception class, either directly or indirectly
'''

print("\n\nExample 1-To print error\n")
class Error(Exception):
    # Error is derived class for Exception, but
    # Base class for exceptions in this module
    pass


class TransitionError(Error):

    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex

        # Error message thrown is saved in msg
        self.msg = msg


try:
    raise (TransitionError(2, 3 * 2, "Not Allowed"))

# Value of Exception is stored in error
except TransitionError as error:
    print('Exception occured: ', error.msg)


#2
print("\n\nExample 2-Guess number\n")

class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")