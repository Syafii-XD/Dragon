import os, Crack

if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("Crack").main()
   except Exception as e:
       exit(str(e))
