def study_schedule(start_time, end_time, target_time):
    counter = 0
    if type(target_time) != int or target_time <= 0:
        return counter
    for index, time in enumerate(start_time):
        if time <= target_time <= end_time[index]:
            counter += 1
    return counter


start_time = [3, 4, 1, 2, 3, 5]
end_time = [5, 5, 3, 4, 3, 5]
target_time = 3
print(study_schedule(start_time, end_time, target_time))
