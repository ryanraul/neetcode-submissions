"""
time_target = (target - position) / speed


- create a dictionary to store the cars speed
    - key: car_start_postion
    - value: car_speed
- sort the position array in reverse order

- iterate through the cars (position) in reverse order
    - append the current car in the stack

    - calculate the time to reach target
        - formula: time_target = (target - start_postion) / car_speed
    - if its greater than the top car in the stack
        - it means they will collide at some time, so pop this car in the stack
    - oterwhise continue

"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = 0
        cars_speed = {}
        positions_sorted = sorted(position, reverse = True)
        stack_fleets = []

        for i,s in enumerate(speed):
            cars_speed[position[i]] = s
        
        for i, car in enumerate(positions_sorted):
            if not stack_fleets:
                stack_fleets.append(car)
                continue

            front_car = stack_fleets[-1]
            time_target_front = (target - front_car) / cars_speed[front_car]
            time_target_current = (target - car) / cars_speed[car]
            if time_target_current <= time_target_front:
                continue

            stack_fleets.append(car)

        return len(stack_fleets)    

      
