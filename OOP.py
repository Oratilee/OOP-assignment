# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self._storage = storage  # Encapsulated attribute (protected)
        self.__battery_capacity = battery_capacity  # Fully encapsulated attribute (private)
    
    # Method to display basic info
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self._storage}GB")
        print(f"Battery Capacity: {self.__battery_capacity}mAh")
    
    # Method to simulate a phone call (Polymorphism in action)
    def make_call(self, number):
        print(f"Dialing {number}... Call in progress...")
    
    # Method to access private battery capacity (encapsulation)
    def get_battery_capacity(self):
        return self.__battery_capacity

# Inheritance: Smartphone -> AdvancedSmartphone
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, camera_quality, is_5g_supported):
        super().__init__(brand, model, storage, battery_capacity)
        self.camera_quality = camera_quality  # Additional attribute for advanced smartphone
        self.is_5g_supported = is_5g_supported  # Additional attribute for advanced smartphone
    
    # Method overriding (Polymorphism): Overriding make_call method
    def make_call(self, number):
        print(f"Making a video call to {0123456789} with high-definition video quality...")

    # Additional method specific to AdvancedSmartphone
    def display_advanced_features(self):
        print(f"Camera Quality: {self.camera_quality} MP")
        print(f"5G Supported: {'Yes' if self.is_5g_supported else 'No'}")

# Create objects for both Smartphone and AdvancedSmartphone
basic_phone = Smartphone("Nokia", "3310", 16, 1500)
advanced_phone = AdvancedSmartphone("Samsung", "Galaxy S21", 128, 4000, 108, True)

# Display information for basic smartphone
print("Basic Smartphone Info:")
basic_phone.display_info()
basic_phone.make_call("123-456-7890")

# Display information for advanced smartphone
print("\nAdvanced Smartphone Info:")
advanced_phone.display_info()
advanced_phone.make_call("123-456-7890")
advanced_phone.display_advanced_features()

# Accessing private attribute via getter method
print(f"\nBattery Capacity of Advanced Smartphone: {advanced_phone.get_battery_capacity()}mAh")
