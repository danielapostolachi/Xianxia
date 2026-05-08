class EventManager:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, event, data):
        for obs in self.observers:
            obs.update(event, data)