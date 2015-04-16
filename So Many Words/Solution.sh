cat dictionary.txt | grep "and" > and.txt

sum=0
while read line
do
    word=$line
    sum=$(($sum+$(expr length $line)))
done < and.txt
echo $sum
