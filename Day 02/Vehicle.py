vehicles = [
    {"name": "Toyota Corolla", "confidence": 0.95},
    {"name": "Honda Civic", "confidence": 0.89},
    {"name": "Suzuki Alto", "confidence": 0.72},
    {"name": "BMW", "confidence": 0.98},
    {"name": "Audi", "confidence": 0.65}
]

for vehicle in vehicles:

    print("Vehicle:", vehicle["name"])
    print("Confidence:", vehicle["confidence"])
    print("----------------")