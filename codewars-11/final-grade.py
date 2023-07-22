def final_grade(exam, projects):
    final_grade_ = 0
    if exam > 50 and projects >= 2:
        final_grade_ = 75
    if exam > 75 and projects >= 5:
        final_grade_ = 90
    if exam > 90 or projects > 10:
        final_grade_ = 100
    return final_grade_

