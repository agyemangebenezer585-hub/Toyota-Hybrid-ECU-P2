class ToyotaHybridECU:
    def __init__(self):
        self.battery_soc = 80

    def decide_mode(self, speed_kmh, accelerator, battery_soc):
        if battery_soc < 20:
            return "PETROL ONLY + CHARGING"
        elif speed_kmh < 30 and battery_soc > 40:
            return "EV MODE - Electric Only"
        elif speed_kmh < 60 and accelerator < 50:
            return "HYBRID MODE - Engine + Motor"
        elif accelerator > 80:
            return "POWER MODE - Both at Max"
        else:
            return "PETROL MODE"

    def regenerative_braking(self, is_braking, battery_soc):
        if is_braking:
            return f"Regen Braking ON - Battery {battery_soc}% -> {battery_soc+5}%"
        return "No Braking"

ecu = ToyotaHybridECU()
print(ecu.decide_mode(20, 30, 70))
print(ecu.regenerative_braking(True, 70))
