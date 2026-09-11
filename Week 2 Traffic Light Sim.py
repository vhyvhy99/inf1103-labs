import time

traffic_lights = [
    ("Green", "Go"),
    ("Yellow", "Slow Down"),
    ("Red", "Stop")
]
print("--- Traffic Light Simulation Started ---")
start_time = time.time()
duration = 10
index = 0
while time.time() - start_time < duration:
    color, message = traffic_lights[index]

    print(f"The light is {color} -> {message}")
    time.sleep(2)
    index = (index + 1) % len(traffic_lights)

print ("--- Simulation FInished ---")