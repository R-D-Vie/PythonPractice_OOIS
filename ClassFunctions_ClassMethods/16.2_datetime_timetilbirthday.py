import datetime

#date of birth in question
birthday = datetime.date(1989, 4, 30)
print("Birthday: ", birthday)

#today's date as comparison
today = datetime.date.today()
print("Today's date: ", today)

#understand if the birthday already happened
#know if the current month is equal to the birth month
#if it is, if the day already passed
if(
    today.month == birthday.month
    and today.day >= birthday.day
    or today.month > birthday.month
):
    nextBirthdayYear = today.year + 1
else:
    nextBirthdayYear = today.year

#build date for birthday
nextBirthday = datetime.date(
    nextBirthdayYear, birthday.month, birthday.day
)

print("Next birthday: ", nextBirthday)

#calculate date of next birthday - current date
diff = nextBirthday - today

print("Days left until next birthday: ", diff.days)
    

#Resources:
#https://www.youtube.com/watch?v=jUbqCPMnmDQ
