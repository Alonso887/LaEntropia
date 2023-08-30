import datetime, random

def random_birthdays(num_of_bdays):
    bdays = []
    for i in range(num_of_bdays):
        start_date = datetime.date(2023,1,1)
        rand_days = datetime.timedelta(random.randint(0,364))
        rand_birthdays = start_date + rand_days
        bdays.append(rand_birthdays)
    return bdays
def check_coincidence():
    if len(bdays) == len(set(bdays)):
        return None
    else:
        for i,birthdayA in enumerate(bdays):
            for k,birthdayB in enumerate(bday[i+1]):
                return birthdayA
      