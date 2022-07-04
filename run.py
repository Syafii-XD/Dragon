import os, platform, dmbf

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from dmbf import Main

    Main()

elif bit == '32bit':

    from dmbf import Main

    Main()
