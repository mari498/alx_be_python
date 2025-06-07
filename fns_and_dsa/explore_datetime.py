# File: fns_and_dsa/explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("\n📅 Current date and time:", formatted_date)
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user to enter a number of days, adds it to the current date, and displays the future date.
    """
    try:
        days_to_add = int(input("\n⏩ Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        print("🗓️ Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("❌ Please enter a valid integer for the number of days.")

def calculate_past_date(current_date):
    """
    OPTIONAL FEATURE: Calculates a past date by subtracting days from the current date.
    """
    try:
        days_to_subtract = int(input("\n⏪ Enter the number of days to subtract from the current date: "))
        past_date = current_date - timedelta(days=days_to_subtract)
        print("📆 Past date:", past_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("❌ Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    print("=== 📌 DateTime Module Exploration ===")
    current_date = display_current_datetime()
    calculate_future_date(current_date)

    # ❗Optional: Ask user if they want to calculate a past date
    choice = input("\nDo you also want to calculate a past date? (yes/no): ").strip().lower()
    if choice in ['yes', 'y']:
        calculate_past_date(current_date)
    print("\n✅ Done.")
