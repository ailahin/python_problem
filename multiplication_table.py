def multiplication_table(number):
    value=  1
    while value<=10:
        multiplication= value*number
        print(value, 'x', number, '=', value*number ) #each time shows the result of Multiplication that's why e put inside the while loop.
        value=value+1
        
    return multiplication

print("final result:",multiplication_table(5))

