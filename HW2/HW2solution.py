def calculate_ticket_price(age, is_weekend, has_coupon):
    """
    Calculates the ticket price for an amusement park based on age,
    weekend status, and discount coupons.
    
    Inputs:
      age: integer representing person's age
      is_weekend: boolean (True if weekend, False if weekday)
      has_coupon: boolean (True if they have a coupon)
      
    Outputs:
      final_price: numeric ticket price (or -1 for invalid age)
    """
    # Check for invalid age first
    if age < 0:
        print("Invalid age!")
        return -1

    # Step 1: Find base price by age
    if age < 12:
        price = 10
    elif age >= 65:
        price = 12
    else:
        price = 20

    # Step 2: Add weekend surcharge (except for seniors)
    if is_weekend and age < 65:
        price += 5

    # Step 3: Apply coupon discount
    if has_coupon:
        price -= 3

    # Ensure price doesn't go below 0
    if price < 0:
        price = 0

    return price




def main():
    print("--- Amusement Park Ticket Calculator ---")

    # 1. Ask for age
    user_age = int(input("Enter visitor age: "))

    # 2. Ask if it is a weekend
    weekend_input = input("Is it a weekend? (yes/no): ")
    is_weekend = weekend_input == "yes"

    # 3. Ask if they have a coupon
    coupon_input = input("Do you have a coupon? (yes/no): ")
    has_coupon = coupon_input == "yes"

    # 4. Calculate total price
    final_price = calculate_ticket_price(user_age, is_weekend, has_coupon)

    # 5. Print the result
    if final_price != -1:
        print(f"\nYour total ticket price is: ${final_price}")

main()
