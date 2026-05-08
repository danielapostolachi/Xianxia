class DamageHandler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, attacker, target, damage):
        if self.next_handler:
            return self.next_handler.handle(attacker, target, damage)
        return damage
