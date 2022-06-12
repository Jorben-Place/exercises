def format_grades(grades):
    def average(ns):
        return round(sum(ns)/ len(ns))
    return "\n".join(f'{name}: {average(grades)}' for name, grades in grades.items())