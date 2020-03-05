from collections import deque

def solution(bridge_length, weight, truck_weights):
    sec = 0
    bridge = deque([])
    truck_weights = deque(truck_weights)
    
    for truck in truck_weights:
        while truck:
            if len(bridge) == bridge_length:
                bridge.pop()
            
            if sum(bridge) + truck <= weight:
                bridge.appendleft(truck)
                truck = 0
                sec += 1
            else:
                bridge.appendleft(0)
                sec += 1
            # print(sec, bridge)
                
    sec += bridge_length

    # print(sec)
    return sec


if __name__ == '__main__':
    solution(2, 10, [7,4,5,6])