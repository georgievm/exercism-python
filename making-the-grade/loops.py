"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    return [round(score) for score in student_scores]

def count_failed_students(student_scores):
    return sum(score <= 40 for score in student_scores)

def above_threshold(student_scores, threshold):
    best = []
    for score in student_scores:
        if score >= threshold:
            best.append(score)
    return best
def letter_grades(highest):
    thresholds = []
    for thr in range(41, highest, int((highest-40)/4)):
        thresholds.append(thr)
    return thresholds

def student_ranking(student_scores, student_names):
    ranking = []
    for index, score in enumerate(student_scores):
        ranking.append(str(index+1)+'. '+student_names[index]+': '+str(score))
    return ranking

def perfect_score(student_info):
    for stud in student_info:
        if stud[1] == 100:
            return stud
    return []
