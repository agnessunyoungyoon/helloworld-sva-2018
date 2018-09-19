# let the user know what's going on
print ("Welcome to Agnes's MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
aaa = raw_input("What's the main character's name: ")
bbb = raw_input("What's the secondary character's name: ")
ccc = raw_input("What does the the second character want from the protagonist?: ")
ddd = raw_input("how does the second character feel about the protagonist?: ")
eee = raw_input("Something the protagonist would like to say to the second character: ")
fff = raw_input("The name of the place where it all happens: ")
ggg = raw_input("A feature of the place: ")
hhh = raw_input("A abjective that could be used to describe that place: ")
iii = raw_input("An abjective that could describe an object: ")
jjj = raw_input("An occation: ") #e.g. party, holiday, funeral
kkk = raw_input("Something/sombebody vulnerable, singular: ")
lll = raw_input("A noun you might compare the main character to: ")
mmm = raw_input("A noun you might compare the other character : ")


# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = aaa + " was thinking about " + bbb + " again " + "." + bbb + " was an intuitive " + mmm + " dolphin with short toenails and brunette moles" + "." + \
aaa + "walked over to the window and reflected on" + aaa + hhh + "surroundings" + "." + aaa + "had always loved" + hhh +  fff + "with it's" + iii + ggg + "." + \
"It was a place that encouraged" + aaa + "'s" + "tendency to feel happy" + "." + \
"Then" + aaa + "saw somehting in the distnace, or rather someone" + "." + "It was the an intuitive figure of" + bbb + "." + \
aaa + "gulped" + "." + aaa + "glanced at her own reflection" + "." + aaa + "was a" + mmm + "," + "squash drinker with" + "pretty toenails and spiky moles" + "." + \
"As" + aaa + "stepped outside and" + bbb + "came closer" + "," + aaa + "could see the moarning glint in" + bbb + "'s" + "eye" + "." + aaa + "looked back, even more and still fingering the giant blade" + "." + bbb + "," + "I love you," + aaa + "replied" + "."

# finally we print the story
print (story)

