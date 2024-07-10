import random
import time

class Car:
    def __init__(self, model, wheel_model):
        self.model = model
        self.wheel_model = wheel_model
        self.fuel = 100  # Starting fuel level
        self.levels = {
            "mud": {"max_laps": 6, "fuel_consumption": 10},
            "thar": {"max_laps": 8, "fuel_consumption": 8},
            "snow": {"max_laps": 10, "fuel_consumption": 10},
            "f1": {"max_laps": 12, "fuel_consumption": 12}
        }
        self.score = 0
        self.coin = 0
        self.car_color = None

    def select_color(self):
        self.car_color = input(f"Select the color for your {self.model}: ").strip()

    def start_race(self, track_name):
        if not self.car_color:
            self.select_color()

        if track_name in self.levels:
            print(f"Setting up {track_name.upper()} level for {self.model} with {self.wheel_model} wheels and {self.car_color} color")
            print("======RACE STARTS, GOOD LUCK!!======")
            max_laps = self.levels[track_name]["max_laps"]
            fuel_consumption = self.levels[track_name]["fuel_consumption"]
            self.run_race(track_name, max_laps, fuel_consumption)
        else:
            print("Invalid track selection.")

    def run_race(self, track_name, max_laps, fuel_consumption):
        laps_completed = 0
        while True:
            laps = int(input("Enter the number of laps you want to race: "))
            if laps <= max_laps:
                for lap in range(1, laps + 1):
                    print(f"Lap {lap} started...")
                    time.sleep(1)  # Simulate lap completion time
                    self.handle_random_event()  
                    print(f"Lap {lap} completed")
                    laps_completed += 1
                self.score += laps_completed * 100  
                self.coin += laps_completed * 10  
                print("You Won! Race completed")
                print("__________GAME OVER!!________")
                break
            else:
                print("Your laps exceed the limit.")

        self.fuel -= laps_completed * fuel_consumption

    def handle_random_event(self):
        event = random.choice(["Rain", "Power-up", "Speed Breaker", "Gold Coin"])
        if event == "Rain":
            print("It starts raining! Using Car Wiper.")
            self.fuel -= 5
        elif event == "Power-up":
            print("You found a power-up! Bonus points.")
            self.score += 10
        elif event == "Speed Breaker":
            print("You found a Speed Breaker! Car Slows Down, Brake applied.")
            self.fuel -= 2
        elif event == "Gold Coin":
            print("Woo hoo! You found a gold coin!.")
            self.coin += 20

    def refuel(self):
        if self.fuel <= 0:
            input_fuel = input("Sorry, you are out of fuel. Do you want to refill? (Yes/No): ").strip().lower()
            if input_fuel == "yes":
                self.fuel = 100  # Refill the fuel tank
                print("Your tank is filled.")
                return True
            elif input_fuel == "no":
                print("====Exiting the game.====")
                return False
        return True

  
