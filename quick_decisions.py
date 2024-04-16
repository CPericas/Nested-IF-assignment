# TASK 1 - CODE CORRECTION
#attendees = int(input("Enter number of attendees: "))  
#venue = "large hall" if attendees > 100 else "conference room"
#print(venue)


# TASK 2 - VENUE SELECTION
#attendees = int(input("Enter number of attendees: "))  
#venue = "large hall" if attendees > 100 else "conference room"
#print(venue)
#entertainment = "audio system" if attendees >= 125 else "projector"
#print(entertainment)



# TASK 3 - CATERING CHOICES
attendees = int(input("Enter number of attendees: "))  
meal_choice = input("Would you like a vegetarian meal? Type yes or no: ")
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
entertainment = "audio system" if attendees >= 125 else "projector"
print(entertainment)
caterers = "Veggie Delight Caterers" if meal_choice == "yes" else "Gourmet Meals Caterers"
print(caterers)