import datetime


class PharmacyBillingSystem:
    def __init__(self):
        # Medicine inventory with price and stock
        self.medicines = {
            "Paracetamol": {"price": 20, "stock": 50},
            "Amoxicillin": {"price": 50, "stock": 30},
            "Cough Syrup": {"price": 80, "stock": 20},
            "Vitamin C": {"price": 30, "stock": 40},
            "Ibuprofen": {"price": 25, "stock": 25}
        }

        self.cart = {}

    def show_medicines(self):
        print("\nAvailable Medicines:")

        for name, info in self.medicines.items():
            print(
                f"{name} - Rs.{info['price']} "
                f"(Stock: {info['stock']})"
            )

    def add_to_cart(self, medicine, quantity):
        if medicine in self.medicines:

            if quantity <= self.medicines[medicine]["stock"]:
                self.cart[medicine] = (
                    self.cart.get(medicine, 0) + quantity
                )

                self.medicines[medicine]["stock"] -= quantity

                print(
                    f"Added {quantity} x {medicine} to cart."
                )

            else:
                print("Not enough stock available!")

        else:
            print("Medicine not available!")

    def generate_bill(self):
        print("\n--- Pharmacy Bill ---")

        total = 0

        for medicine, quantity in self.cart.items():
            price = self.medicines[medicine]["price"] * quantity

            print(
                f"{medicine} x {quantity} = Rs.{price}"
            )

            total += price

        # Apply 10% discount if total is greater than Rs.200
        discount = 0

        if total > 200:
            discount = total * 0.10

        print(f"Discount (10%): -Rs.{discount:.2f}")

        # Calculate 5% GST
        gst = (total - discount) * 0.05

        print(f"GST (5%): Rs.{gst:.2f}")

        # Calculate final amount
        final_amount = total - discount + gst

        print("---------------------")
        print(f"Total Amount: Rs.{final_amount:.2f}")
        print("---------------------")

        # Save bill to file
        with open("pharmacy_bill.txt", "a") as f:

            f.write(
                f"\nBill Date: {datetime.datetime.now()}\n"
            )

            for medicine, quantity in self.cart.items():

                price = self.medicines[medicine]["price"] * quantity

                f.write(
                    f"{medicine} x {quantity} = Rs.{price}\n"
                )

            f.write(f"Discount: Rs.{discount:.2f}\n")
            f.write(f"GST: Rs.{gst:.2f}\n")
            f.write(
                f"Final Amount: Rs.{final_amount:.2f}\n"
            )
            f.write("---------------------\n")

        print("Bill saved to pharmacy_bill.txt")
        print("Thank you for visiting!")


# Main Program
pharmacy = PharmacyBillingSystem()

while True:

    print("\n1. Show Medicines")
    print("2. Add to Cart")
    print("3. Generate Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))

    except ValueError:
        print("Please enter a valid number between 1 and 4.")
        continue

    if choice == 1:

        pharmacy.show_medicines()

    elif choice == 2:

        med = input("Enter medicine name: ")

        try:
            qty = int(input("Enter quantity: "))

            pharmacy.add_to_cart(med, qty)

        except ValueError:
            print("Quantity must be a number!")

    elif choice == 3:

        pharmacy.generate_bill()

    elif choice == 4:

        print("Exiting system. Goodbye!")
        break

    else:

        print("Invalid choice! Please enter 1-4.")