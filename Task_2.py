#import libraries here

def main():
 month=input("Enter name of the month [ex. June]: ")
day=int(input("Enter the day [ex. 5]: "))
if 0<day<=31:
    if month=="January" or (month=="December" and day>=21) or (month=="February" and day<=29) or (month=="March" and day<=19):
        print(f"{month} {day} is in Winter")
    elif (month=="March" and day>=20) or (month=="April" and day<=30) or month=="May" or (month=="June" and day<=20):
        print(f"{month} {day} is in Spring")
    elif (month=="June" and 21<=day<31) or (month=="July") or month=="August" or (month=="September" and day<=21):
        print(f"{month} {day} is in Summer")
    else:
        print(f"{month} {day} is in Fall") 

  
  pass

if __name__ == "__main__":
  main()
