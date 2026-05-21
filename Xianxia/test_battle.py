# test_battle.py (put this in your root Xianxia folder)
from Xianxia.Factories.player_factory import PlayerFactory
from Xianxia.Factories.enemy_factory import EnemyFactory
from Xianxia.BattleLogic import Party
from Xianxia.BattleLogic.battle_session import BattleSession


if __name__ == "__main__":
    sou = PlayerFactory().build("sou")
    tara = EnemyFactory().build("tara_kane")

    player_party = Party(max_size=4)
    player_party.add_member(sou)

    enemy_party = Party(max_size=5)
    enemy_party.add_member(tara)

    session = BattleSession(player_party, enemy_party)
    session.start()