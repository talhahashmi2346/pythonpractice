numbers = 17


def print_formatted(number):
    pad = len(str(bin(number))[2:])
    for i in range(1, number + 1):
        print(str(i).rjust(pad, ' '), end=" ")
        print(str(oct(i))[2:].rjust(pad, ' '), end=" ")
        print(str(hex(i))[2:].upper().rjust(pad, ' '), end=" ")
        print(str(bin(i))[2:].rjust(pad, ' '))



print_formatted(numbers)
