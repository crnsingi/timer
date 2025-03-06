# Import the time module: This allows you to use the sleep() function to pause the execution of the program for a specified number of seconds

## Input the countdown time: The user is asked to input the length of the countdown in seconds

## Convert the input to an integer: Since input is read as a string, we convert it to an integer using the int() function

## Define the countdown function: This function will take the time (in seconds) as input and count down to zero, printing the time left in minutes and seconds

## Use a while loop: The loop runs until t reaches zero

## Calculate minutes and seconds using divmod(): The divmod() function returns the quotient and remainder when dividing by 60 (i.e., minutes and seconds)

## Print the time in a formatted way: The formatted string ensures that both minutes and seconds are displayed in two-digit format (e.g., 00:59). '{:02d}:{:02d}'

## Overwrite the previous output: The end='\r' argument in the print() function allows the program to overwritethe previous line of output rather than printing a new line

## Pause the program for one second: The time.sleep(1) function pauses the program for one second betweeneach countdown iteration

## Decrement the time: After each iteration, t is decremented by 1 to move the countdown forward

## Print a final message: After the countdown reaches zero, the program prints "Fire in the hole!!"  to signify the end of the countdown