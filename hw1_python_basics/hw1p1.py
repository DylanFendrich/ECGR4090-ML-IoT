#!/usr/bin/env python

import person
import numpy
import matplotlib.pyplot as plt

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

#part A
print("\npart A")
for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))
  
#part B
print("\npart B")
new_list = [len(name) for name in list_of_names]
print(new_list)

#part E
print("\npart E")
for count in range(0,4):
    people = {list_of_names[count]:person.person(list_of_names[count], list_of_ages[count], list_of_heights_cm[count])}
    print(people[list_of_names[count]])
    
#part F
array_ages = numpy.array(list_of_ages)
array_heights = numpy.array(list_of_heights_cm)

#part G
print("\npart G")
average_age = numpy.mean(array_ages)
print("The average age is {:}".format(average_age))

#part H
print("\npart H")
figure, scatter_plot = plt.subplots()

scatter_plot.scatter(array_ages, array_heights)
scatter_plot.set(xlabel='Age (years)', ylabel='Height (cm)', title='Age vs Height')
scatter_plot.grid()

figure.savefig("age_vs_height.png")
plt.show()