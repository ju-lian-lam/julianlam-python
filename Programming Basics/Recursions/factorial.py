def fact(n)->int:
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
# end function

print(fact(5))

# A recursive routine has three essential characteristics:
    # A stopping coniditon or base case must be included which when met means that the routine will not call itself and will start to "unwind"
    # For input values other than the stopping condition, the routine must call itself
    # The stopping condition must be reached after a finite number of calls