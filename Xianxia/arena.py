class Arena:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Arena, cls).__new__(cls)
            print("Arena created")
        return cls._instance

    @staticmethod
    def start_battle(player, boss):
        print(f"Battle Start! {player.name} VS {boss.name}\n")

        turn = 1
        while player.is_alive() and boss.is_alive():
            print(f"--- Turn {turn} ---")

            # Player attacks
            ability, dmg = player.attack()
            print(f"{player.name} uses {ability} for {dmg} damage!")
            boss.take_damage(dmg)
            print(f"{boss.name} HP: {boss.get_hp()}\n")
            if not boss.is_alive():
                print(f"{boss.name} is defeated!")
                break

            # Boss attacks
            ability, dmg = boss.attack()
            print(f"{boss.name} uses {ability} for {dmg} damage!")
            player.take_damage(dmg)
            print(f"{player.name} HP: {player.get_hp()}\n")
            if not player.is_alive():
                print(f"{player.name} is defeated!")
                break

            turn += 1