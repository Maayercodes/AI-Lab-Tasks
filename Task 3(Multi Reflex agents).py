class MultiReflexAgent:
    def __init__(self, temp, humidity=None):
        self.desired_temp = temp
        self.desired_humidity = humidity
        self.current_temp = None
        self.current_humidity = None
    def percept(self, temp, humidity=None):
        self.current_temp = temp
        if humidity is not None:
            self.current_humidity = humidity
    def act(self):
        actions = []
        if self.current_temp > self.desired_temp:
            actions.append("Turn off the heater")
        elif self.current_temp < self.desired_temp:
            actions.append("Turn on the heater")
        else:
            actions.append("Keep the heater unchanged")
        if self.current_humidity is not None:
            if self.current_humidity > self.desired_humidity:
                actions.append("Turn on the dehumidifier")
            elif self.current_humidity < self.desired_humidity:
                actions.append("Turn off the dehumidifier")
            else:
                actions.append("Humidity is optimal")
        return " and ".join(actions)
agent = MultiReflexAgent(temp=22, humidity=50)
rooms = {
    "Living room": (28, 40),
    "Bedroom": (18, 55),
    "Kitchen": (32, 60)
}
for room, (temp, humidity) in rooms.items():
    agent.percept(temp, humidity)
    print(f"{room} (Temp: {temp}, Humidity: {humidity}) ==> {agent.act()}")






