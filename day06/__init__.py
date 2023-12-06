def calculate_distance_travelled(hold_time: int, time_allowed: int) -> int:
    time_moving = time_allowed - hold_time
    return time_moving * hold_time
