# question 1

with open("names.txt", "w") as file:
    file.write("Ashish\nRaj\nPranjal\nRohit\nRam")

with open("names.txt", "r") as file:
    data = file.read()
    print(data)


# question 2
with open("log.txt", "a") as file:
    file.write("\nProgram run successfully")

with open("log.txt", "r") as file:
    data = file.read()
    print(data)

# question 3
list = [5, 10, 15, 20, 25]
print(list)
list = [val for val in list if val > 15]
print(list)

# question 4
import json
with open("cities.json", "r") as file:
    data = json.load(file)
    print(data)
    for key, value in data.items():
        print(f"{key} has a population of {value["Population"]}")
    

new_city = input("Enter a new city name: ")
population  = input("Enter population of city: ")

population = {"Population": population}
data.update({
    new_city:population
})
with open("cities.json", "w") as file:
    json.dump(data, file, indent=4, sort_keys=True)


# question 5

try:
    with open("data1.txt", "r") as file:
        data = file.read()
        print(data)
    
except FileNotFoundError as error:
    print(f"The error occurred is {error}")
else:
    print("An unknown error occurred")
finally:
    print("Program ends here")