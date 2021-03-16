#!/bin/bash

if [ $# -eq 0 ]
   then
     echo "...blablas"
#    exit
fi

if [ -z "$2" ]
  then
    echo "blablas"
#   exit
fi    

if [[ "$1" =~ ^[0-9]+$ ]] ; then 
   echo "blabla"
   else echo "first argument must be an integer"
#  exit
fi


# with municipality name
#wget -nc -O FVGareacodes.csv "http://overpass-api.de/api/interpreter?data=%5Bout%3Acsv%28%22ref%3AISTAT%22%2C%22name%22%3Bfalse%3B%22%2C%22%29%5D%3Barea%5B%22name%22%3D%22Friuli%20Venezia%20Giulia%22%5D%2D%3E%2Ea%3Brelation%5B%22admin%5Flevel%22%3D%228%22%5D%28area%2Ea%29%3Bout%3B%0A"

# just ref:ISTAT
wget -nc -O FVGareacodes.csv "http://overpass-api.de/api/interpreter?data=%5Bout%3Acsv%28%22ref%3AISTAT%22%3Bfalse%29%5D%3Barea%5B%22name%22%3D%22Friuli%20Venezia%20Giulia%22%5D%3Brelation%5B%22admin%5Flevel%22%3D%228%22%5D%28area%29%3Bout%3B%0A"

#remove leading zeroes
sed -i -e 's/^0*//' FVGareacodes.csv

rm parte_generale.htm
while read -r line
do
    areacode="$line"
    wget -O - "https://pianiemergenza.protezionecivile.fvg.it/municipalities/$areacode/sections/a_parte_generale" > tmp.htm
    ./node_modules/html2csv/bin/html2csv.js tmp.htm
    mkdir -p $areacode
    mv ??.csv $areacode/.
done < "FVGareacodes.csv"

find . -name '05.csv' -exec cat {} \; > AreeAttesa.csv
find . -name '05.csv' -exec cat {} \; > EdificiStrategici.csv

