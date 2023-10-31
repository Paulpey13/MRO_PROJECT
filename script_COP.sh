#!/usr/bin/env bash

for FILE in $(ls ./donnees_cop/*)
do
  for SOL in 'choco' 'ace'
    do
      echo ''$FILE' '$SOL' CAS 1'
      time timeout 600s python3 ./COP/cop_cas1.py -data=$FILE -solver=$SOL -output=$FILE'_cas1'
      echo ''

      echo ''$FILE' '$SOL' CAS 2'
      time timeout 600s python3 ./COP/cop_cas2.py -data=$FILE -solver=$SOL -output=$FILE'_cas2'
      echo ''

      echo ''$FILE' '$SOL' CAS 2BIS'
      time timeout 600s python3 ./COP/cop_cas2BIS.py -data=$FILE -solver=$SOL -output=$FILE'_cas2BIS'
      echo ''

      echo ''$FILE' '$SOL' CAS 3'
      time timeout 600s python3 ./COP/cop_cas3.py -data=$FILE -solver=$SOL -output=$FILE'_cas3'
      echo ''
    done
done
