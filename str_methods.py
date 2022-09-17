test = "abracadabra"

print(test.count("a"))

print(test.count("ab"))

test_one = "A\tBrown\tQuick\tFox"

print(test_one.expandtabs(1))

test_two = "The man on the moon"

print(test_two.find("man"))
print(test_two.find("woman"))

test_three = "123 is the order of things"

for i in test_three:
    print(i.isalnum(), end=" ")

print("\n")

test_four = "123 is the order of things"

for k in test_four:
    print(k.isalpha(), end=" ")