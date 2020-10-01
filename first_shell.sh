#!/bin/sh
#list contents of "Desktop"
cd ~/Desktop
ls

#find all the fasta files/folders
locate *fasta

#for all the files in ~/Data, replace Atha_ with Athaliana
cd ~/Data

for file in `dir -d *.fasta`; do
  echo $file
  new_file=`echo "$file" |sed 's/.fasta/_v2.fasta/'`
  sed 's/Atha_/Athaliana/g' $file > $new_file
done
