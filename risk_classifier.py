def classify_student(marks_list):
    total = 0
    fail_count = 0

    for mark in marks_list:
        if mark < 50:
            fail_count += 1
        total += mark

    average = total / len(marks_list)

    if (average < 60) or (fail_count >= 2):
        status = "At-Risk"
    else:
        status = "Normal"

    return status


# Example run
marks = [55, 58, 62, 60]
print("Status:", classify_student(marks))
