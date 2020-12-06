def read_seat_list(input):
    with open(input) as file:
        return [int(line, 2) for line in file]

def find_seat(seats):
    return (len(seats) + 1) * (seats[0] + seats[-1]) / 2 - sum(seats)

if __name__ == "__main__":
    seats = read_seat_list("better_input.txt")
    print("Seat number", find_seat(seats))
