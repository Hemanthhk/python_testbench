#Import the actual file and call the method inside the file
# import mymodule
# mymodule.func_in_module()

#import only necessary methods required and use them
from mymodule1 import func_in_module
func_in_module()

#Importing the class and creating obj to refer the methods inside the class
from mymodule import SampleModule

my_obj = SampleModule()
my_obj.func_in_module()