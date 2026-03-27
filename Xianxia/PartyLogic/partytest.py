# select_enemy_party.py
from Xianxia.boss import Boss
from Xianxia.PartyLogic.enemypartybuilder import EnemyPartyBuilder


def select_boss_from_list(boss_templates):
    """Prompt the user to select a boss from existing templates"""
    print("\nAvailable Bosses:")
    for idx, boss in enumerate(boss_templates, start=1):
        print(f"{idx}. {boss.name} (HP: {boss.get_hp()}, Attacks: {', '.join(boss._attacks)})")

    while True:
        try:
            choice = int(input("Select a boss by number: "))
            if 1 <= choice <= len(boss_templates):
                return boss_templates[choice - 1]
            else:
                print("Invalid selection.")
        except ValueError:
            print("Enter a number corresponding to the boss.")


def main():
    # Existing boss templates
    spades_boss = Boss("Rui Tsukikage", 500, ["Male Manipulation", "Female Manipulation", "AI Manipulation"])
    diamonds_boss = Boss("Akise Kaminaga", 400, ["Raccoon Rashes", "Identity Theft"])
    clubs_boss = Boss("Deko Mitsuharu", 450, ["Butterfly Bites", "Brain Damage"])

    boss_templates = [spades_boss, diamonds_boss, clubs_boss]

    print("=== Enemy Party Builder ===")
    party_name = input("Enter party name: ")

    # How many bosses to add
    while True:
        try:
            num_bosses = int(input("How many bosses (1-4)? "))
            if 1 <= num_bosses <= 4:
                break
            else:
                print("Number must be between 1 and 4")
        except ValueError:
            print("Please enter a valid number")

    selected_bosses = []
    for i in range(num_bosses):
        print(f"\n--- Select Boss {i + 1} ---")
        boss = select_boss_from_list(boss_templates)
        selected_bosses.append(boss)

    # Build enemy party using the builder (will clone automatically)
    enemy_party = EnemyPartyBuilder() \
        .set_name(party_name) \
        .add_auto_members(selected_bosses) \
        .set_leader() \
        .build()

    print("\n=== Enemy Party Created ===")
    enemy_party.show_party()


if __name__ == "__main__":
    main()