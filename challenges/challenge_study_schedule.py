def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0

    for period in permanence_period:
        if not all(isinstance(time, int) for time in period):
            return None

        if period[0] <= target_time <= period[1]:
            counter += 1

    return counter
