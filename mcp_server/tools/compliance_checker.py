

def check_compliance(specifications, intended_use, location):
    response = {
        "compliance_status": "",
        "required_permits": [],
        "restrictions": []
    }
    weight = specifications.get("weight", 0)
    camera = specifications.get("camera", False)
# Weight Rule
    if weight > 25:
        response["compliance_status"] = "Non-Compliant"
        response["restrictions"].append("Drone weight exceeds 25kg limit.")
        return response
    # Location Rule
    if location.lower() in ["airport", "military", "border"]:
        response["compliance_status"] = "Restricted"
        response["required_permits"].append("Special Flight Permission")
        response["restrictions"].append("Operation in restricted zone.")
        return response
    # Intended Use Rule
    if intended_use.lower() == "commercial":
        response["required_permits"] = [
            "UIN Registration",
            "Remote Pilot License",
            "Insurance"
        ]
    else:
        response["required_permits"] = [
            "UIN Registration"
        ]

    # Camera Rule
    if camera:
        response["restrictions"].append(
            "Camera drones must follow privacy regulations."
        )

    response["compliance_status"] = "Compliant"

    return response