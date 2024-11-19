def fibonacci_series(numbers):
    #series=[0, 1, 1, 2, 3, 5, 8, 13]
    series=[0, 1]
    new_series=2
    
    while new_series<=numbers:
        next_series= series[new_series-1]+ series[new_series-2]
        series.append(next_series)
        new_series= new_series+1
    return series
print(fibonacci_series(9))

#Moral story: the fibonachi N position is sum of two previous position.
