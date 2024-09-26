import json
import random
import threading

#da comment
def display_battlemenu():
    print("=== Time For Battle! ===")
    print("1. Check")
    print("2. Attack")
    print("3. Check Inventory")
    print("4. Use Item")
    print("5. Run")
    print("============================")

def battle(attacks):  # Accept attacks as an argument
    with open('enemy.json', 'r') as json_file:  # Getting the enemy file
        enemy_list = json.load(json_file)

    # Select a random enemy from the list
    enemy = random.choice(enemy_list)
    enemy_name = enemy['name']
    enemy_health = enemy['health']
    enemy_attack = enemy['attack']

    while enemy_health > 0:  # Battle menu loop
        display_battlemenu()
        action_choice = input("Choose an action (1-5): ")

        if action_choice == '1':
            print(f"Looks like it's {enemy_name} and it has {enemy_health} health...")

        elif action_choice == '2':
            print(f"You have {attacks} available")  # Display available attacks

            # Pass enemy_health to attack_state and get updated health back
            enemy_health = attack_state(attacks, enemy_health)  

            # Check if the enemy has been defeated
            if enemy_health <= 0:
                print(f"You defeated {enemy_name}!")

        elif action_choice == '3':
            print("Checking inventory...")
            # Implement inventory check logic here

        elif action_choice == '4':
            print("What item would you like to use?")
            # Implement item use logic here

        elif action_choice == '5':
            print("Attempting to run...")
            break  # Exit the battle menu

        else:
            print("Invalid action. Please try again.")

def attack_state(attacks, enemy_health):
    global user_input
    user_input = None

    def get_user_input():
        global user_input
        user_input = input("Enter attack within 10 seconds!: ")

    # Start a thread to get user input
    input_thread = threading.Thread(target=get_user_input)
    input_thread.start()
    
    # Wait for the user to input or timeout after 10 seconds
    input_thread.join(timeout=10)

    if input_thread.is_alive():
        print("Time is up! You didn't choose an attack.")
    else:
        # Extract the available attack names and their corresponding damage values
        attack_dict = {attack['name'].lower(): attack['number'] for attack in attacks}

        # Check if the input is a valid attack
        if user_input and user_input.lower() in attack_dict:
            attack_name = user_input.lower()
            damage = attack_dict[attack_name]

            # Strong or weak attack logic
            if user_input.isupper():
                print(f"Strong attack chosen: {user_input}.")
                enemy_health -= damage  # Full damage for strong attack
            elif user_input.islower():
                print(f"Weak attack chosen: {user_input}.")
                enemy_health -= damage // 2  # Half damage for weak attack

            print(f"Enemy now has {enemy_health} health.")
        else:
            print("Invalid attack. Choose a valid attack next time.")

    return enemy_health  # Return updated enemy health