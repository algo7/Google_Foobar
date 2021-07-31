def solution(xs):

    # When there is no panel in the array
    if len(xs) == 0:
        return str(0)

    # When there is only one panel and the panel is draning power
    if len(xs) == 1 and abs(xs[0]) != xs[0]:
        return str(xs[0])

    # Keep panels whose abs power value is smaller than or equal to 1000 and is an int
    xs = [ele for ele in xs if
          ele <= 1000
          and abs(ele) <= 1000
          and ele % 1 == 0]

    # Separate power-draining and funcitoning panels
    # Panel with 0 power is ignored
    powerDraningPanels = [num for num in xs if num < 0]
    functioningPanels = [num for num in xs if num > 0]

    # Wave stabilizer
    if len(powerDraningPanels) % 2 != 0:
        # Sort from smallest to largest
        powerDraningPanels.sort()
        # Pop the largest number (the less negative one)
        powerDraningPanels.pop()

    # Calculate the max power output
    if functioningPanels or powerDraningPanels:
        maxPower = 1
        for panel in functioningPanels + powerDraningPanels:
            maxPower *= panel

        return str(maxPower)

    return str(0)


# print(solution([5, -10]))  # -50
# print(solution([0, 0, 0, 0]))  # 0
# print(solution([2, 0, 2, 2]))  # 8
# print(solution([2, -3, 1, 0, -5]))  # 30
print(solution([-2, -3, 4, -5]))  # 60
# print(solution([-2, -3, 100]))  # 600
# print(solution([-5, -5, -5, -5]))  # 625
# print(solution([0, 0, -5]))  # 0
# print(solution([-1, -1, 0]))  # 1
# print(solution([-2]))  # -2
# print(solution([-4, 0]))  # 0

# def solution1(xs):

#     # When there is no panel in the array
#     if len(xs) == 0:
#         return str(0)

#     # Take the 1st 50 panels if there are more than 50
#     if len(xs) > 50:
#         xs = xs[:50]

#     # Keep panels whose abs power value is smaller than or equal to 1000 and is an int
#     xs = [ele for ele in xs if
#           ele <= 1000
#           and abs(ele) <= 1000
#           and ele % 1 == 0]

#     # Extract power-draning panel (power output < 0)
#     powerDranings = []
#     for panel in xs:
#         if panel < 0:
#             powerDranings.append(panel)

#     # Wave stabilizer
#     stablizerQueue = []
#     stablized = []
#     if len(powerDranings) != 1 and len(powerDranings) != 0 and len(powerDranings) % 2 != 0:
#         # Find abs of all power-draning panels
#         for panel in powerDranings:
#             stablizerQueue.append(abs(panel))
#         try:
#             # Find the first max
#             stablized.append(max(stablizerQueue))
#             stablizerQueue.remove(max(stablizerQueue))
#             # Find the 2nd max
#             stablized.append(max(stablizerQueue))
#             stablizerQueue.remove(max(stablizerQueue))
#         except:
#             pass
#         # Keep only positive values in the original panels array without 0s
#         xs = [ele for ele in xs if ele > 0]
#         # Add the stablized panels to the original panels array
#         xs = xs+stablized

#     # Keep only non-0 panels
#     xs = [ele for ele in xs if ele > 0 or ele < 0]
#     # If nothing is left in the array then return 0
#     if len(xs) == 0:
#         return str(0)
#     if len(xs) == 1 and abs(xs[0]) != xs[0]:
#         return str(0)
#     # Find the max power
#     maxPower = 1
#     for i in xs:
#         maxPower *= i

#     return str(maxPower)


# def solution2(xs):
#     # calculate the max power output of the array
#     maxPower = 1
#     for i in xs:
#         if i != 0:
#             maxPower = maxPower*i

#     # Convert the result to string
#     return str(maxPower)


# print(solution2([2, 0, 2, 2, -8000]))
# print(solution2([2, -3, 1, 0, -5]))
# print(solution2([-2, -3, 4, -5]))


# def solution3(xs):
#     # When there is no panel in the array
#     if len(xs) == 0:
#         return str(0)
#     # Take the 1st 50 panels if there are more than 50
#     if len(xs) > 50:
#         xs = xs[:50]
#     # Keep panels whose power value is smaller than or equal to 1000 and is an int
#     xs = [ele for ele in xs if
#           ele <= 1000
#           and abs(ele) <= 1000
#           and ele % 1 == 0]

#     # Extract power-draning panel (power output < 0 and >=-1000)
#     powerDranings = []
#     for panel in xs:
#         if panel < 0:
#             powerDranings.append(panel)

#     # Wave stabilizer
#     stablizerQueue = []
#     stablized = []
#     if len(powerDranings) != 1 and len(powerDranings) != 0:
#         for panel in powerDranings:
#             stablizerQueue.append(abs(panel))
#         # Find the first max
#         stablized.append(max(stablizerQueue))
#         stablizerQueue.remove(max(stablizerQueue))
#         # Find the 2nd max
#         try:
#             stablized.append(max(stablizerQueue))
#             stablizerQueue.remove(max(stablizerQueue))
#         except:
#             pass

#         for panel in stablized:
#             xs.remove(-panel)

#         xs = xs+stablized

#         xs = [ele for ele in xs if ele > 0]

#     maxPower = 1
#     for panel in xs:
#         maxPower = maxPower*panel

#     return str(maxPower)


# print(solution3([2, 0, 2, 2]))
# print(solution3([2, -3, 1, 0, -5]))
# print(solution3([-2, -3, 4, -5]))
# print(solution3([5, -10]))
# print(solution3([-2, -3, 100]))
