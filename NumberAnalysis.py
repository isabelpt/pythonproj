numArray = []
odd = 0
even = 0

class Analyze:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def averageNum(self, numbers):
        print(f"Average: {sum(numbers) / len(numbers)}")

    def oddOrEvenMajority(self, numbers):
        global odd, even
        for number in numbers:
            if number % 2 == 0:
                even += 1
            elif number % 2 == 1:
                odd += 1
        print(f"Even: {even} \nOdd: {odd}\n")

# Album 1
debut = Analyze("Album 1", [1, 2, 3, 4, 5, 6])
print(debut.name)
debut.averageNum([1, 2, 3, 4, 5, 6])
debut.oddOrEvenMajority([1, 2, 3, 4, 5, 6])

# Album 2
# Album 3
# Album 4
# Album 5
# Album 6
# Album 7
# Album 8
# Favorite Songs
favs = Analyze("Favorites", [3, 21, 5, 8, 33, 12, 81, 270, 17, 356, 60, 12, 39, 26, 23, 280, 84, 16, 1, 13])
print(favs.name)
favs.averageNum([3, 21, 5, 8, 33, 12, 81, 270, 17, 356, 60, 12, 39, 26, 23, 280, 84, 16, 1, 13])
favs.oddOrEvenMajority([3, 21, 5, 8, 33, 12, 81, 270, 17, 356, 60, 12, 39, 26, 23, 280, 84, 16, 1, 13])
# All Songs
# Sort