from car import Car

def car_race():
    car_models = ["thunderbolt", "blaze GT", "vortex 900", "neon Racer", "turbo Charger"]  # Car models for selection
    car_wheels = ["slick tires", "grooved tires", "soft compound tires", "hard compound tires", "studded tires"]  # Car wheels for selection
    total_score = 0
    total_coins = 0

    while True:
        model = input(f"Enter your car model from {car_models}: ").lower()
        if model in car_models:
            wheel_model = input(f"Enter your car wheel model from {car_wheels}: ").lower().strip()
            if wheel_model in car_wheels:
                car = Car(model, wheel_model)  
            else:
                print("Invalid wheel model selection.")
                continue
        else:
            print("Invalid car model selection.")
            continue

        user_input = input("Do you want to start the game? (Yes/No)").strip().lower()
        if user_input == 'yes':
            print("The types of roads available are MUD, THAR, SNOW, F1")
            track_name = input("Select the road type from the above list that you would like to play? ").strip().lower()

            if track_name in car.levels:  
                car.start_race(track_name)
            else:
                print("Invalid track selection.")

            if not car.refuel():  
                break

            total_score += car.score  
            total_coins += car.coin  

            print(f"Your total score : {total_score}")
            print(f"Your total number of coins collected : {total_coins}")

            user_continue = input("Would you like to continue? (Yes/No): ").strip().lower()
            if user_continue == "no":
                print(f"Your final total score is: {total_score}")
                print(f"Your final total number of coins collected is: {total_coins}")
                break
        elif user_input == 'no':
            print("====Exiting the game.====")
            break
        else:
            print("Invalid input. Please enter Yes or No.")

if __name__ == "__main__":
    car_race()
