#!/usr/bin/python3

import sys, getopt, random, os

def usage():
  print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]"
        + " \n \n" +
        "Generate a secure, memorable password using the XKCD method \n \n" +
        "optional arguments: \n"
        "\t -h, --help \t show this help message and exit \n" +
        "\t -w WORDS, --words WORDS \n" +
        "\t\t\t include WORDS words in the password (default=4) \n" +
        "\t -c CAPS, --caps CAPS  capitalize the first letter of CAPS "
        + "random words \n" +
        "\t\t\t (default=0) \n" +
        "\t -n NUMBERS, --numbers NUMBERS \n" +
        "\t\t\t insert NUMBERS random numbers in the password \n" +
        "\t\t\t (default=0) \n"
        "\t -s SYMBOLS, --symbols SYMBOLS \n" +
        "\t\t\t insert SYMBOLS random symbols in the password \n" +
        "\t\t\t (default=0)")

def assessInt(arg, errMsg):
  if arg.isdigit():
    return int(arg)
  else:
    print(errMsg)
    sys.exit(1)



def passGen(words, caps, nums, sym):
  og = open("words.txt")
  file = og.readlines()
  total = len(file)
  allSym = ["~","!","@","#","$","%","^","&","*",".",":",";"]
  allNum = ["0","1","2","3","4","5","6","7","8","9"]
  fin = []
  pwd = ""

  for _ in range(words):
    fin.append(file[random.randint(0, total - 1)].lower())
  for _ in range(caps):
    ind = random.randint(0, len(fin) - 1)
    curr = fin[ind]
    while(curr[0].isupper()):
      ind = random.randint(0, len(fin) - 1)
      curr = fin[ind]
    fin[ind] = curr.capitalize()
  for _ in range(sym):
    fin.insert(random.randint(0, len(fin)),
               allSym[random.randint(0, len(allSym) - 1)])
  for _ in range(nums):
    fin.insert(random.randint(0, len(fin)),
               allNum[random.randint(0, len(allNum) - 1)])
  for word in fin:
    pwd = pwd + word.rstrip('\n')
  return pwd

def main(argv):
  words = 4
  nums = 0
  sym = 0
  caps = 0

  try:
    opts, args = getopt.getopt(argv,"hw:c:n:s:",
                               ["help","words=","caps=","numbers=","symbols="])
  except getopt.GetoptError:
    print('Invalid input, try using --help')
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit(0)
    elif opt in ("-w", "--words"):
      words = assessInt(arg, "Words input must be a natural number")
    elif opt in ("-n", "--numbers"):
      nums = assessInt(arg, "Numbers input must be a natural number")
    elif opt in ("-c", "--caps"):
      caps = assessInt(arg, "Caps input must be a natural number")
      if (caps > words):
        print("Number of caps cannot exceed words")
        sys.exit(1)
    elif opt in ("-s", "--symbols"):
      sym = assessInt(arg, "Symbols input must be a natural number")

  print(passGen(words, caps, nums, sym))

if __name__ == "__main__":
  main(sys.argv[1:])