#!/bin/sh
set -e

echo "------------------------------"
echo "tex"
echo "------------------------------"

cd ../tex

echo "----------en3----------"
cd en3/cv

for i in `seq 1 5`
do
    latexmk -pdflatex=lualatex -pdf cv${i}.tex
done

cd ..

latexmk -pdflatex=lualatex -pdf info.tex
latexmk -pdflatex=lualatex -pdf teorie.tex

echo ""----------en3 - done"----------"

cd ../../scripts

echo "------------------------------"
echo "tex - done"
echo "------------------------------"

echo "------------------------------"
echo "copy_to_subjects"
echo "------------------------------"

python copy_to_subjects.py

echo "------------------------------"
echo "copy_to_subjects - done"
echo "------------------------------"

echo "------------------------------"
echo "create_merges.py"
echo "------------------------------"

python create_merges.py

echo "------------------------------"
echo "create_merges.py - done"
echo "------------------------------"
