def filter_detections(detections, threshold=0.80):

    accepted = []

    for detection in detections:

        if detection["confidence"] >= threshold:

            accepted.append(detection)

    return accepted


def calculate_average_confidence(detections):

    if not detections:
        return 0

    total = 0

    for detection in detections:

        total += detection["confidence"]

    return total / len(detections)


# Simulated AI model predictions

predictions = [
    {"vehicle": "Toyota", "confidence": 0.95},
    {"vehicle": "Honda", "confidence": 0.65},
    {"vehicle": "BMW", "confidence": 0.91},
    {"vehicle": "Audi", "confidence": 0.55},
    {"vehicle": "Suzuki", "confidence": 0.85}
]


# Process predictions

accepted_vehicles = filter_detections(predictions)

average_confidence = calculate_average_confidence(
    accepted_vehicles
)


print("Accepted Vehicles:")

for vehicle in accepted_vehicles:
    print(vehicle["vehicle"], vehicle["confidence"])


print("Average Confidence:", average_confidence)