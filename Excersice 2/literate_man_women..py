# 10. In a town, men = 52% total literacy - 48% literate Men = 35% of total population. Population = 80000. Write a program to find the total number of illieterate men and women.

total_population = int(input("Population of a town is = "))

total_men = total_population * 52/100
print("Total men of this town is = ", total_men)
total_literacy = total_population * 48/100
print("Total literacy of this town is = ", total_literacy)
literate_men = total_population * 35/100
literate_women = total_population *13/100
print("Total literate men of this town is = ", literate_men)
print("Total literate women of this town is ", literate_women)
