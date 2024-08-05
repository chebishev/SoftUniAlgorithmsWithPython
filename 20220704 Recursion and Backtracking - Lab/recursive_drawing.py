def draw(number):
    if number <= 0:
        return
    print("*" * number)
    draw(number - 1)
    print("#" * number)


number = int(input())

draw(number)

# test input 2
# test input 5
