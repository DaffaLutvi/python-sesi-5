import random

def main():
    choices = ["batu", "gunting", "kertas"]
    player_choice = input("Masukkan pilihan Anda (batu/gunting/kertas): ").lower()
    
    if player_choice not in choices:
        print("Pilihan tidak valid. Silakan pilih batu, gunting, atau kertas.")
        return

    computer_choice = random.choice(choices)
    print(f"Pilihan komputer: {computer_choice}")

    if player_choice == computer_choice:
        print("Hasilnya seri!")
    elif (player_choice == "batu" and computer_choice == "gunting") or \
         (player_choice == "gunting" and computer_choice == "kertas") or \
         (player_choice == "kertas" and computer_choice == "batu"):
        print("Anda menang!")
    else:
        print("Komputer menang!")

if __name__ == "__main__":
    main()
