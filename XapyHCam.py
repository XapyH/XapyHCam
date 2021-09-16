# -*- coding: utf-8 -*-
import List
from List.it import *
from List.us import *
from List.fr import *
from List.de import *
from List.tr import *
import requests,re,os

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"



def main():
    os.system('clear')
    print("{}        ____ ").format(r)
    print("   _[]_/____\__n_ ")
    print("  |_____.--.__()_|")
    print("  |V   //# \\\    |")
    print("{}  |I   \\\__//    | ").format(w)
    print("  |P    '--'     | ")
    print("{}  '--------------'------------.  ").format(r,w)
    print("{}  | {}Coder     : {}XapyH {}       | ").format(r,w,r,w,r,ir,reset,w)
    print("{}  | {}Instagram : {}@harun.st10 {} |").format(r,w,w,w,lgray,w)
    print("{}  '---------------------------'  ").format(r,w)
    print ("  {}[ 1 ] {}Turkiye").format(r,w)
    print ("  {}[ 2 ] {}Almanya").format(r,w)
    print ("  {}[ 3 ] {}Italya").format(r,w)
    print ("  {}[ 4 ] {}Fransa").format(r,w)
    print ("  {}[ 5 ] {}Amerika Birlesik Devletleri").format(r,w)
    print ("  {}[ 0 ] {}Cikis").format(r,w)
    print ""
    select = input("\033[1;31m[ \033[1;37mNumarayı Girin \033[1;31m]\033[1;37m> ")
    filtering(select)



def filtering(pilih):
    if pilih == 1:
        Türkiye()
    elif pilih == 2:
        Almanya()
    elif pilih == 3:
        Italya()
    elif pilih == 4:
        Fransa()
    elif pilih == 5:
        AmerikaBirlesikDevletleri()
    elif pilih == 0:
        print (r+"Cikis ..."+w)
        os.sys.exit()
    else:
        print (r+"Cikis ..."+w)
        os.sys.exit()

if __name__ == '__main__':
    main()
