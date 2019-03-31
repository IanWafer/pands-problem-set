# Ian Wafer 21-02-2019
# Solution to problem 1
# Calculate the integers between the input number and 0

x = int(input("Please enter a positive integer: "))  # User must input a value to sum up
ans = 0                                              # This will be used to sum up the correct figures and print the answer
i = 0                                                # This  ensures the first iteration is at 0 making the initial value 1 included 

if x <= 0:                                           # Value needs to be positive to create sum
   x = int(input("Negative numbers not accepted. Please enter a positive integer: ")) # Reminder for a positive value is required

assert x >= 0                                        # Check for true/false condition after x value input

while i <= x:                                        # This ensures the value of i does not inrease past the value of the input figure resulting in a loop 
    ans = ans + i                                    # Sum of iterations
    i = i + 1                                        # Move to next iteration until while condition not met

print(ans)                                           # When while condition not met print ans value
