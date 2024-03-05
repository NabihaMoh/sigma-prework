from datetime import datetime


def calculate_age(today, input):
    difference = ((today - input).days//365)
    return difference


def main():
    user_input = input("Please enter a date (DD/MM/YYYY): ")
    todays_date = datetime.now().date()

    user = datetime.strptime(user_input, "%d/%m/%Y").date()

    age = calculate_age(todays_date, user)

    print(f"The age between the current dat and the given date is {age}")


main()
