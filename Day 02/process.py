detections = [
    {"vehicle": "Toyota", "confidence": 0.95},
    {"vehicle": "Honda", "confidence": 0.65},
    {"vehicle": "BMW", "confidence": 0.91},
    {"vehicle": "Audi", "confidence": 0.55},
    {"vehicle": "Suzuki", "confidence": 0.85}
]

for detection in detections:

    if detection["confidence"] >= 0.80:

        print(
            detection["vehicle"],
            "Accepted:",
            detection["confidence"]
        )

    else:

        print(
            detection["vehicle"],
            "Rejected:",
            detection["confidence"]
        )