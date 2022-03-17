# Ivan Chen <ichen42@stuy.edu>
# hw22
# worked with no one
# advised by no one

# task 3
def toCelsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

print("32F is", toCelsius(32), "C")
print("212F is", toCelsius(212), "C")
print("-212F is", toCelsius(-212), "C")

print("\n")

# task 4
def binetFib(n):
  return round(((( 1 + 5 ** (1/2) ) ** n - ( 1 - 5 ** (1/2) ) ** n / 2 )) / (2 ** n * 5 ** (1/2)))

print("7th fibonacci number:", binetFib(7))
print("10th fibonacci number:", binetFib(10))
