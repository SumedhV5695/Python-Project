# Python-Project
Alarm Clock using Tkinter in Python
Tkinter: Python offers multiple choices for developing a GUI (Graphical User Interface). Out of all the GUI strategies, tkinter is that the most ordinarily used technique. It’s a customary Python interface to the Tk GUI toolkit shipped with Python.

Winsound: The winsound module provides access to the essential sound-playing machinery provided by Windows platforms. It includes functions and a number of other constants. Beep the PC’s speaker.

time: Time module in Python provides varied time-related functions. This module comes with Python’s normal modules.

datetime: The main focus of datetime is to form it simpler to access attributes of the thing associated with dates, times, and time zones.

Step 1: Import Required Library
image

Step 2: Add Button, Labels, Frame, and option menus
Button
Button(Object Name, text=”Enter Text”,**attr)
Label
Label(Object Name, text=”Enter Text”, command=”Enter Command” , **attr)
Frame
Frame(Object Name, **attr)
Option Menu
OptionMenu(“Object Name”, “Data Type”, “list of value in form of tuple”, **attr)
We will create a three-option menu:-
Hours (00–24) Minutes (00–60) Seconds (00–60)
Time is in 24-hour time format.

Step 3: Make a function named alarm(), which performs alarm clock work.
Below is the full implementation:

Get hours, minutes, seconds value from the user
Wait for one second using time module
Get Current time using datetime module
Check if the current time is equal to set time; play sound using winsound module
Alarm Clock using Tkinter in Python Tkinter: Python offers multiple choices for developing a GUI (Graphical User Interface). Out of all the GUI strategies, tkinter is that the most ordinarily used technique. It’s a customary Python interface to the Tk GUI toolkit shipped with Python.

Step 4: Create 24 hr clock function
Step 5: Create 12 hr clock fucntion
Step 6 : Create Alarm Function
Step 7 : Loooping It.
Step 8: Adding images using PIL Module.
	Winsound: The winsound module provides access to the essential sound-playing machinery provided by Windows platforms. It includes functions and a number of other constants. Beep the PC’s speaker.
	time: Time module in Python provides varied time-related functions. This module comes with Python’s normal modules.
	datetime: The main focus of datetime is to form it simpler to access attributes of the thing associated with dates, times, and time zones.
Finished.
