from Xianxia.RepertoireLogic.observer import Observer


class LifestealPassive(Observer):
    def update(self, event, data):
        if event == "damage_dealt":
            user = data["attacker"]
            user.hp += data["damage"] * 0.2