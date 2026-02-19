# =========================
# Base Class: Device
# =========================

class Device:
    def __init__(self, name, price, stock, warranty_period):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def display_info(self):
        print(self)

    def __str__(self):
        return (f"{self.name} | Price: ${self.price} | "
                f"Stock: {self.stock} | Warranty: {self.warranty_period} months")

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount


# =========================
# Smartphone Class
# =========================

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return (super().__str__() +
                f" | Screen: {self.screen_size}\" | Battery: {self.battery_life}h")

    def make_call(self):
        print(f"{self.name} is making a call...")

    def install_app(self):
        print(f"Installing app on {self.name}...")


# =========================
# Laptop Class
# =========================

class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return (super().__str__() +
                f" | RAM: {self.ram_size}GB | CPU: {self.processor_speed}GHz")

    def run_program(self):
        print(f"{self.name} is running a program...")

    def use_keyboard(self):
        print(f"Typing on {self.name} keyboard...")


# =========================
# Tablet Class
# =========================

class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return (super().__str__() +
                f" | Resolution: {self.screen_resolution} | Weight: {self.weight}g")

    def browse_internet(self):
        print(f"{self.name} is browsing the internet...")

    def use_touchscreen(self):
        print(f"Using touchscreen on {self.name}...")


# =========================
# Cart Class
# =========================

class Cart:
    def __init__(self):
        self.items = []  # list of tuples (device, amount)
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            print(f"{amount} x {device.name} added to cart.")
        else:
            print("Not enough stock available.")

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device:
                self.items.remove(item)
                self.total_price -= device.price * amount
                print(f"{device.name} removed from cart.")
                return
        print("Device not found in cart.")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        print("\n===== CART =====")
        if not self.items:
            print("Cart is empty.")
        else:
            for device, amount in self.items:
                print(f"{device.name} x {amount}")
            print(f"Total Price: ${self.total_price}")

    def checkout(self):
        if not self.items:
            print("Cart is empty.")
            return

        for device, amount in self.items:
            if not device.is_available(amount):
                print(f"Not enough stock for {device.name}.")
                return

        for device, amount in self.items:
            device.reduce_stock(amount)

        print("\n===== RECEIPT =====")
        for device, amount in self.items:
            print(f"{device.name} x {amount}")
        print(f"Total paid: ${self.total_price}")
        print("Purchase successful!")

        self.items.clear()
        self.total_price = 0


# =========================
# Main Application
# =========================

def main():
    devices = [
        Smartphone("iPhone 14", 999, 10, 24, 6.1, 20),
        Smartphone("Samsung S23", 899, 15, 24, 6.5, 22),
        Smartphone("Xiaomi 13", 699, 20, 12, 6.3, 25),
        Smartphone("Google Pixel 8", 799, 8, 24, 6.2, 24),

        Laptop("MacBook Pro", 1999, 5, 12, 16, 3.2),
        Laptop("Dell XPS 15", 1499, 7, 12, 16, 3.0),
        Laptop("HP Spectre", 1399, 6, 12, 8, 2.8),
        Laptop("Lenovo ThinkPad", 1299, 9, 12, 16, 3.1),

        Tablet("iPad Pro", 799, 12, 12, "2048x1536", 470),
        Tablet("Samsung Tab S8", 699, 10, 12, "2560x1600", 500),
        Tablet("Huawei MatePad", 499, 11, 12, "1920x1200", 480),
        Tablet("Lenovo Tab P11", 399, 14, 12, "2000x1200", 490)
    ]

    cart = Cart()

    while True:
        print("\n====== ELECTRONIC STORE ======")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            print("\n===== AVAILABLE DEVICES =====")
            for i, device in enumerate(devices):
                print(f"{i + 1}. {device}")

            try:
                index = int(input("Select device number to add: ")) - 1
                amount = int(input("Enter quantity: "))
                cart.add_device(devices[index], amount)
            except (ValueError, IndexError):
                print("Invalid selection.")

        elif choice == "2":
            cart.print_items()

        elif choice == "3":
            cart.checkout()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
