def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
print(count_upper_case("Hello World"))

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("ABfff") == 2, "Two Upper Case"

print("All tests have passed")