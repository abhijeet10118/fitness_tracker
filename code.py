import csv
from datetime import datetime

# MET values for different exercises
MET_VALUES = {
    "Running": 8.0,
    "Cycling": 7.0,
    "Swimming": 6.0,
    "Weightlifting": 3.5,
    "Yoga": 2.5,
    "Jumping Rope": 10.0,
    "Push-ups": 3.8,
    "Sit-ups": 4.0,
    "Squats": 5.0,
    "Plank": 3.0
}

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to get user's BMI
def get_user_bmi():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))
            if weight > 0 and height > 0:
                bmi = calculate_bmi(weight, height)
                print(f"Your BMI is: {bmi:.2f}")
                return weight, height
            else:
                print("Please enter positive values for weight and height.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Function to calculate calories burned using MET values
def calculate_calories_burned(exercise_name, duration, weight):
    if exercise_name in MET_VALUES:
        met_value = MET_VALUES[exercise_name]
        # Convert duration from minutes to hours
        duration_hours = duration / 60
        # Calculate calories burned
        calories_burned = met_value * weight * duration_hours
        return calories_burned
    else:
        return None

# Function to display exercises
def display_exercises():
    print("Here are 10 different exercises you can do:")
    for i, exercise in enumerate(MET_VALUES.keys(), 1):
        print(f"{i}. {exercise}")
    print("Enter 0 to exit.")

# Function to get exercise choice
def get_exercise_choice():
    while True:
        try:
            choice = int(input("Enter the number of the exercise you did (1-10, or 0 to exit): "))
            if 0 <= choice <= 10:
                return choice
            else:
                print("Please enter a number between 1 and 10, or 0 to exit.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get duration
def get_duration(exercise_name):
    while True:
        try:
            duration = float(input(f"Enter the duration (in minutes) for {exercise_name}: "))
            if duration >= 0:
                return duration
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to save data to CSV
def save_to_csv(date, exercise_name, duration, calories_burned):
    with open("exercise_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, exercise_name, duration, calories_burned])

# Main function
def main():
    exercises = list(MET_VALUES.keys())
    
    # Get user's weight and height to calculate BMI
    print("Let's calculate your BMI first!")
    weight, height = get_user_bmi()
    
    while True:
        # Display the list of exercises
        display_exercises()
        
        # Get the user's choice of exercise
        choice = get_exercise_choice()
        
        # Exit the program if the user enters 0
        if choice == 0:
            print("Exiting the program. Goodbye!")
            break
        
        # Get the exercise name based on the choice
        exercise_name = exercises[choice - 1]
        
        # Get the duration for the chosen exercise
        duration = get_duration(exercise_name)
        
        # Calculate calories burned using MET values
        calories_burned = calculate_calories_burned(exercise_name, duration, weight)
        if calories_burned is not None:
            print(f"\nYou burned approximately {calories_burned:.2f} calories doing {exercise_name} for {duration} minutes.")
        else:
            print("\nCould not calculate calories burned for the selected exercise.")
        
        # Save the data to a CSV file
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_to_csv(current_date, exercise_name, duration, calories_burned)
        
        # Display the result
        print("Great job! Keep up the good work!\n")

if __name__ == "__main__":
    main()
