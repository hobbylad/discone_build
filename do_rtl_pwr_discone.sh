#!/bin/sh
rtl_power -f 25M:1700M:1M -i 1m -g  0 -1 discone_25_1700_1M_g00.csv  > cap_discone.txt
rtl_power -f 25M:1700M:1M -i 1m -g 10 -1 discone_25_1700_1M_g10.csv >> cap_discone.txt
rtl_power -f 25M:1700M:1M -i 1m -g 20 -1 discone_25_1700_1M_g20.csv >> cap_discone.txt
rtl_power -f 25M:1700M:1M -i 1m -g 30 -1 discone_25_1700_1M_g30.csv >> cap_discone.txt
rtl_power -f 25M:1700M:1M -i 1m -g 40 -1 discone_25_1700_1M_g40.csv >> cap_discone.txt
rtl_power -f 25M:1700M:1M -i 1m -g 50 -1 discone_25_1700_1M_g50.csv >> cap_discone.txt

