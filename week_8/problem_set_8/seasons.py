from datetime import datetime, date


def main():
    date_of_birth = input("Date of Birth: ")


def age_in_minutes(date_of_birth: str) -> str:
    dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
    now = datetime.now()
    elapsed = now - dob
    return int(elapsed.total_seconds() / 60)


def minutes_since_dob(date_of_birth):
    dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    now = date.today()
    elapsed = now - dob
    return int(elapsed.total_seconds() / 60)


if __name__ == "__main__":
    print(age_in_minutes("2000-08-25"))
    print(minutes_since_dob("2000-08-25"))
