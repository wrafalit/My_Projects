# age = input("What is your current age?")

# Example Input:  56
# Example Output: You have 12410 days, 1768 weeks, and 408 months left.

# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
end = 90
age = 36
def waitbutwhy(age):
    left_months = (90 - int(age)) * 12
    left_weeks = (90 - int(age)) * 52
    left_days = (90 - int(age)) * 365
    print(f'You have {left_days}, {left_weeks} weeks, and {left_months} left.')

def board(age):
    x_mark = 'X '
    o_mark = 'O '
    age_left = end - age
    list_board = []
    for i in range(end):
        if i <= age:
            list_board.append(x_mark)
        else:
            list_board.append(o_mark)
    print(list_board)
    for p in range(len(list_board),10):
        print(list_board[::10])
    print(''.join(list_board))

board(age)

# a = "Birth> "+"X " *10
# b = "       "+"X " *10 +'\n'
# c = "       "+"X " *10 +' <Death'
# print(a)
# print(b*7+c)