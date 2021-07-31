from math import sqrt


def solution(totalMaterial):
    # Initialize the list
    solarPanelProduced = []
    # Check if cutting is required
    if sqrt(totalMaterial)-int(sqrt(totalMaterial)) == 0:
        solarPanelProduced.append(totalMaterial)
        return solarPanelProduced
    else:
        # The cutting process
        while totalMaterial != 0:
            # Calculate the area of the panel to be cut
            solarPanel = int(sqrt(totalMaterial))**2
            # Cut the materials
            totalMaterial = totalMaterial-solarPanel
            # Add the solar panel to the list
            solarPanelProduced.append(solarPanel)
            # If the leftover materials are to little
            if totalMaterial < 1:
                break

        return solarPanelProduced


print(solution(0))
print(solution(12))
print(solution(15324))
print(solution(100))
print(solution(1000))
