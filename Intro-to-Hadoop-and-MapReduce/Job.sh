#create a test file
head -50 ../data/purchases.txt > testfile.txt

#test mappy.py
cat testfile.txt | ./mappy.py


#simulate entire process for the first 50 lines
cat testfile.txt | ./mapper.py | sort | ./reducer.py
