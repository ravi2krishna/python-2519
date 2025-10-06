# using user defined modules

import my_module # ModuleNotFoundError: No module named 'my_module'
import my_module_two

print(my_module.name)
print(my_module_two.name)