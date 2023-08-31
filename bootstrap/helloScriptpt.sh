#! /bin/bash



zdcf_fname=zdcf95_v2.2.f90
zdcf=zdcf95
direct=/Users/tekanombonani/Desktop/bootstrap

if [[ -f "$zdcf_fname" ]] && [[ -d "$direct" ]]
then
    echo "directory or file exists"

else
    echo "directory or file does not exist"
   
fi

curdir=$(pwd)
for file in ./LC{0..10};
do
  if [ -d "$file" ]
then
    cp [ -f "$zdcf95" ] "$file"
    cd "$file" && ./zdcf95 && cd "$curdir"
  fi
done






