# battle_session.py
import random
from Xianxia.BattleLogic.party import Party

class BattleSession:
    def __init__(self, player_party: Party, enemy_party: Party):
        self._player_party = player_party
        self._enemy_party = enemy_party
        self._turn_order = []
        self._round = 1
        self._status_timers = {}   # {entity: {status: turns_remaining}}
        self._dot_timers = {}      # {entity: {damage: turns_remaining}}
        self._is_over = False
        self._winner = None
        self._log_fn = print  # swappable logger

    # ── parties ──────────────────────────────────────────
    def get_player_party(self):
        return self._player_party

    def get_enemy_party(self):
        return self._enemy_party

    def add_enemy(self, entity):
        # called mid-fight e.g. summon_bees hook
        self._enemy_party.add_member(entity)
        self._insert_into_turn_order(entity)

    # ── turn order ───────────────────────────────────────
    def _roll_initiative(self):
        results = []
        all_combatants = (
            self._player_party.get_members() +
            self._enemy_party.get_members()
        )
        for entity in all_combatants:
            roll = random.randint(1, 20) + entity.speed
            results.append((entity, roll))

        # sort highest to lowest
        results.sort(key=lambda x: x[1], reverse=True)

        # handle ties with a coin flip
        results = self._resolve_ties(results)
        self._turn_order = [entity for entity, roll in results]

    def roll_initiative(self):
        self._roll_initiative()

    @staticmethod
    def _resolve_ties(results):
        final = []
        i = 0
        while i < len(results):
            # collect all entities with the same roll
            tied = [results[i]]
            while i + 1 < len(results) and results[i+1][1] == results[i][1]:
                i += 1
                tied.append(results[i])
            # coin flip — just shuffle tied entities
            if len(tied) > 1:
                random.shuffle(tied)
            final.extend(tied)
            i += 1
        return final

    def _insert_into_turn_order(self, entity):
        # mid-fight addition — insert based on speed roll
        roll = random.randint(1, 20) + entity.speed
        for i, e in enumerate(self._turn_order):
            if roll > e.speed:
                self._turn_order.insert(i, entity)
                return
        self._turn_order.append(entity)

    # ── status tracking ───────────────────────────────────
    def register_status_timer(self, entity, status_name, duration):
        if entity not in self._status_timers:
            self._status_timers[entity] = {}
        self._status_timers[entity][status_name] = duration

    def register_dot(self, entity, damage_per_turn, duration):
        if entity not in self._dot_timers:
            self._dot_timers[entity] = []
        self._dot_timers[entity].append({
            "damage": damage_per_turn,
            "duration": duration
        })

    def _tick_timers(self):
        for entity, statuses in list(self._status_timers.items()):
            for status, turns in list(statuses.items()):
                statuses[status] -= 1
                if statuses[status] <= 0:
                    del statuses[status]
                    if entity.status == status:
                        entity.status = "alive"
                        self._log_fn(f"✅ {entity.name} is no longer {status}!")

        for entity, dots in list(self._dot_timers.items()):
            for dot in dots:
                if entity.is_alive():
                    entity.take_damage(dot["damage"], "none")
                    self._log_fn(f"🔥 {entity.name} takes {dot['damage']} burn damage! ({entity.hp}/{entity.max_hp} HP)")
                dot["duration"] -= 1
            self._dot_timers[entity] = [d for d in dots if d["duration"] > 0]

    def _tick_cooldowns(self):
        for entity in self._player_party.get_members():
            if entity.skill and hasattr(entity.skill, 'tick_cooldown'):
                entity.skill.tick_cooldown()

# ── entity status ─────────────────────────────────────
    def check_entity_status(self, entity):
        if not entity.is_alive():
            if entity in self._turn_order:
                self._turn_order.remove(entity)
        # check boss phase transition
        from Xianxia.CombatEntities.boss import Boss
        if isinstance(entity, Boss):
            entity.check_phase_transition()

    def _check_win_condition(self):
        if self._player_party.all_dead():
            self._is_over = True
            self._winner = "enemies"
        elif self._enemy_party.all_dead():
            self._is_over = True
            self._winner = "players"

    # ── main loop ─────────────────────────────────────────
    def start(self):
        self._roll_initiative()
        self._log(f"⚔️ Battle starts! Round {self._round}")
        self._log(self._turn_order_summary())

        while not self._is_over:
            self._run_round()
            self._check_win_condition()
            if not self._is_over:
                self._round += 1
                self._log(f"\n🔄 Round {self._round} begins!")
                self._tick_timers()
                self._tick_cooldowns()

        self._log(f"\n🏆 {self._winner} win!")
        return self._winner

    def _run_round(self):
        for entity in list(self._turn_order):
            if not entity.is_alive():
                continue
            if entity.status == "stunned":
                self._log(f"⚡ {entity.name} is stunned and skips their turn!")
                continue
            self._log(f"\n➡️ {entity.name}'s turn")
            entity.act(self)
            self._check_win_condition()
            if self._is_over:
                break

    # ── logging ───────────────────────────────────────────
    # @staticmethod
    # def _log(message):
    #    print(message)  # swapped for Discord output later

    def _log(self, message):
        self._log_fn(message)

    def _turn_order_summary(self):
        names = [e.name for e in self._turn_order]
        return f"Turn order: {' → '.join(names)}"

    def check_win_condition(self):
        self._check_win_condition()

    def tick_timers(self):
        self._tick_timers()

    def tick_cooldowns(self):
        self._tick_cooldowns()

    @property
    def is_over(self):
        return self._is_over

    @property
    def turn_order(self):
        return self._turn_order

    @property
    def round(self):
        return self._round

    @round.setter
    def round(self, value):
        self._round = value

    @property
    def log_fn(self):
        return self._log_fn

    @log_fn.setter
    def log_fn(self, fn):
        self._log_fn = fn