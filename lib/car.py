#Notice that we are requiring lib/vehicle.py. That is because our Car class will need access to the Vehicle class 
#and will therefore need access to the file that contains that class.

from vehicle import Vehicle

class Car(Vehicle):
    #overwrite the inherited go() method with one specific to Car.
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
        # to see original from parent
        #return super().go()

car = Car(20,5)
print(car.go())


'''
We use Vehicle as an argument for the Car class to note that Car inherits from Vehicle. Run the test suite again 
and you'll see that you are passing a number of tests for the Car class.

Wow! We didn't write anything in our Car class but instances of Car class inherit all of the Vehicle attributes 
and methods and therefore have access to them.

'''

'''
We're still failing the go() test however. Looks like the test is expecting the go() method on an individual car to 
return the phrase: "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!". This is different than the return value of the go() method 
that we inherited from the Vehicle class.

Let's overwrite the inherited go() method with one specific to Car.

'''