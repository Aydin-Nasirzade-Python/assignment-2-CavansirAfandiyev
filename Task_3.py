#import libraries here

def main():
  'n=int(input("Enter the wavelength in nm: "))
  if n<380 or n>750:
    print("Invalid input!")
  elif n<450:
    print("The relevant color is Violet")
  elif n<495:
    print("The relevant color is Blue")
  elif n<570:
    print("The relevant color is Green")
  elif n<590:
    print("The relevant color is Yellow")
  elif n<620:
    print("The relevant color is Orange")
  else:
    print("The relevant color is Red")
  pass

if __name__ == "__main__":
  main()
