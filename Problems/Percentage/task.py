def get_percentage(number, round_digits=0):
    if round_digits == 0:
        round_digits = None
    percentage = round(number * 100, round_digits)
    return "{}%".format(percentage)
