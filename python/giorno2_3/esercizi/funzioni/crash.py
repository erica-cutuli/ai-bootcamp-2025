def factorial(n):
    """Calculate the factorial of the given number"""
    # FIXME: this code has a bug!
    if n > 1:
        return n * factorial(n - 1) #aggiungo -1 così da evitare il loop infinito
    else:
        return 1


assert factorial(5) == 120
