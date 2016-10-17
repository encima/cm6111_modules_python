import city
import city_module
from city_module import another_city

print(city.name)
print("This city has {0} people".format(city.pop))
print(city_module.name)
another_city.print_name()
