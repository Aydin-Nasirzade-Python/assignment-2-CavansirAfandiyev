#import libraries here

def main():
  month=input("Enter a month [ex. March]: ")
  day=int(input("Enter the day [ex. 12]: "))
  if 1<=day<31 or month=="January" or month=="February" or month=="March" or month=="April" or month=="May" or month=="June" or month=="July" or month=="August" or month=="September" or month=="October" or month=="November" or month=="December":
  if (month=="December" and day>=22) or (month=="January" and day<=19):
   print("Your zodiac sign is Capricorn")
  elif (month=="January" and day>=20) or (month=="February" and day<=18):
    print("Your zodiac sign is Aquarius")
  elif (month=="February" and 19<=day<=29) or (month=="March" and day<=20):
     print("Your zodiac sign is Pisces")
  elif (month=="March" and day>=21) or (month=="April" and day<=19):
     print("Your zodiac sign is Aries")
   elif (month=="April" and 20<=day<=30) or (month=="May" and day<=20):
      print("Your zodiac sign is Taurus")
   elif (month=="May" and day>=21) or (month=="June" and day<=20):
      print("Your zodiac sign is Gemini")
   elif (month=="June" and 21<=day<=30) or (month=="July" and day<=22):
      print("Your zodiac sign is Cancer")
   elif (month=="July" and day>=23) or (month=="August" and day<=22):
     print("Your zodiac sign is Leo")
   elif (month=="August" and day>=23) or (month=="September" and day<=22):
     print("Your zodiac sign is Virgo")
   elif (month=="September" and 23<=day<=30) or (month=="October" and day<=22):
     print("Your zodiac sign is Libra")
   elif (month=="October" and day>=23) or (month=="November" and day<=21):
     print("Your zodiac sign is Scorpion")
   elif (month=="November" and 22<=day<=30) or (month=="December" and day<=21):
     print("Your zodiac sign is Sagittarius")
   else:
     print("Either a month or a day is invalid!")
  pass

if __name__ == "__main__":
  main()
