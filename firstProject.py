import datetime
import uuid

class BikeRentalShop:

    def __init__(self, stock=0):
        self.stock = stock
        # Create a log of all active rentals
        # All will follow a generic pattern: rental time | number of bikes rented | rental type | rental ID
        self.rentals_log = {}

    def displayStock(self):
        if self.stock > 0:
            print("We currently have {} bikes available for rental!").format(self.stock)
            return self.stock
        else:
            print("We don't currently have any bikes available for rental - please check again soon!")
            return None

    def validateStock(self, num):
        if num <= 0:
            # Number validation check
            print("Number must be positive and greater than zero!")
            return None
        elif num > self.stock:
            # Requested amount of bikes exceeds stock levels
            print("Sorry, we only have {} bike(s) available for rental - you requested {}").format(self.stock, num)
            return False
        else:
            print("{} Bikes accepted for rental!").format(num)
            return True

    def hourlyRental(self, num):
        if self.validateStock(num):

            # Calculate rental time
            now = datetime.datetime.now()
            time = now.time()

            # Generate a unique rental ID
            rental_id = uuid.uuid4()

            # Store the rentals in the rentals dictionary
            self.rentals_log[rental_id] = (now, num, "hourly", rental_id)

            print("You have rented {} bike(s) on an hourly basis starting today at {}").format(num, time)
            print("The fee is £4 per hour for bike usage")
            print("Please quote this rental code upon returning your bike(s): {}".format(rental_id))

            self.stock -= num
            return now
    
    def dailyRental(self, num):
        if self.validateStock(num): 

            now = datetime.datetime.now()
            time = now.time()

            # Generate a unique rental ID
            rental_id = uuid.uuid4()

            # Store the rentals in the rentals dictionary
            self.rentals_log[rental_id] = (now, num, "daily", rental_id)

            print("Accepted! You have rented {} bike(s) on a daily basis starting today at {}").format(num, time)
            print("The fee is £20 per day for bike usage")
            print("Please quote this rental code upon returning your bike(s): {}".format(rental_id))

            self.stock -= num
            return now

    def weeklyRental(self, num):
        if self.validateStock(num): 
            now = datetime.datetime.now()
            time = now.time()

            # Generate a unique rental ID
            rental_id = uuid.uuid4()

            # Store the rentals in the rentals dictionary
            self.rentals_log[rental_id] = (now, num, "weekly", rental_id)

            print("Accepted! You have rented {} bike(s) on a daily basis starting today at {}").format(num, time)
            print("The fee is £30 per week for bike usage")
            print("Please quote this rental code upon returning your bike(s): {}".format(rental_id))

            self.stock -= num
            return now

    def returnRental(self, rental_ref_code):
        # Use the rentals log to return and calculate the bill for the customer
        cust_rental = self.rentals_log[rental_ref_code]

        # Unpack the cust rental tuple 
        rental_dateTime = cust_rental[0]
        now_dateTime    = datetime.datetime.now()
        
        bikes_rented = cust_rental[1]
        rental_type  = cust_rental[2]

        # Use a switch to perform the necessary billing calculations


