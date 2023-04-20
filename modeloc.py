# def solution(segements):

#     segements.sort()
#     print(segements)
#     pts = 0
#     prevst, preved = segements[0]
#     for st, ed in segements[1:]:
#         if st >= preved:
#             prevst = st
#             preved = ed
#             pts += 1
#         else:
#             prevst = st
#             preved = max(ed, preved)

#     return pts
def solution(segments):
    # Sort segments based on their right endpoints
    segments.sort(key=lambda x: x[1])
    print(segments)
    count = 0
    last_point = float('-inf')

    for segment in segments:
        if last_point < segment[0] or last_point > segment[1]:
            count += 1
            last_point = segment[1]

    return count

test1 = [[-1, 3],[-5, -3],[3, 5],[2,4],[-3,-2],[-1, 4],[5,5]]
solution(test1) # Output: 3

# TS
# modelling trading division
# 3 tiers, modelling trading / engineerong / corp
# equity / macro
# derivative realative value
# fixed income/ potfolio workflow
# forecast model/ risk model
# HM - hackerrank 3Q math/data 3hr
# 1 phone HM - technical
# 2 half day onsite virtual