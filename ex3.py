# Without floating point #'s, all decimals are omitted

print "This example is without floating point #'s:"

print "I will now count my chickens:"

# 25 plus (30 divided by 6)
print "Hens", 25 + 30 / 6
# 100 minus the remainder of (75 divided by 4), which is 3 (4 into 75 18 times, 18 * 4 is 72, 75-72 is 3
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"
# % and * take precedence over - and +, with equal weight. So, * and % always operate left to right first, and then - and + follow left to right after
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5-7?", 5 - 7

print "Oh, that's why it's false."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= - 2
print "Is it less or equal?", 5 <= -2

print "This example is WITH floating point #'s:"

print "I will now count my chickens:"

print "Hens", 25.0 + 30.0 / 6.0
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0

print "Now I will count the eggs:"
# Answer changes to 6.75, because (1/4 = 0) changes to (1.0/4.0 = .25)
print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

print "Is it true that 3 + 2 < 5 - 7?"

print 3.0 + 2.0 < 5.0 - 7.0

print "What is 3 + 2?", 3.0 + 2.0
print "What is 5-7?", 5.0 - 7.0

print "Oh, that's why it's false."

print "How about some more."

print "Is it greater?", 5.0 > -2.0
print "Is it greater or equal?", 5.0 >= - 2.0
print "Is it less or equal?", 5.0 <= -2.0