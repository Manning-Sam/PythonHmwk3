# Square sum
# Create a function that given a list of integers, squares each number passed into it and 
# then sums the results together.
# Example Input: [1, 2, 2]
# Example Output: 9
# Explanation: 1^2 + 2^2 + 2^2 = 9

# Example Input: [3, 4, 5]
# Example Output: 50

def squares(*numbers):
    squares = []
    for num in numbers:
        squares.append(num**2)
    sum_squares = sum(squares)
    return sum_squares
print(squares(1,2,3))

numbers = [1,2,3]
sum_squares = sum([num**2 for num in numbers])
print(sum_squares)