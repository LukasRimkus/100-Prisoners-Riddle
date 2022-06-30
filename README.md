# 100-Prisoners-Riddle

The solution is to pick firstly a number of pa prisoner, then follow where the found number says, etc. It is 
calculated that a probability to finally for all prisoners to escape is about 30%. 

This probability is quite high, because now the probabilities of escaping for each prisoner are not independent (compared
to the random case), as those numbers are going to construct the loops. So if there are no loops bigger than 50 in the original
case or just more than a half of all numbers, then the prisoners are going to escape. 
