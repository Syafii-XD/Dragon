import os, platform, dmbf_enc

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from dmbf_enc import Main

    Main()

elif bit == '32bit':

    from dmbf_enc import Main

    Main()
