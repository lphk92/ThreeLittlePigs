from characters import Pig, Wolf, Man
from house import Material, House
# Once upon a time, when pigs still could rhyme
# There was a pig
print Pig()

# Oh crap wait, there were 3 pigs
print Pig() * 3

# Yea, so these three pigs decided that they wanted to do something with their lives!
# Naturally, the first thing to do for a pig in Ye-Old-America was to become a land owner
pigs = [Pig(), Pig(), Pig()]

piggy1 = pigs[0]
man = Man()

print man.say("What can I do ye fer?").concat(piggy1.say("Hello, my name is Benjamin. I shall become the  overlord of everything  you possess. I demand   all of your straw       ...please"), padding=15)

print man.say("Well ain't that just      dandier than a pickle in afish barrel! Here ya go").concat(piggy1.say("Thanks! I mean...yea youbetter obey!"), padding=15)

# And the first pig took that straw and build himself a house
piggy1.build_house(Material.STRAW)
print piggy1.say("Yoshi! It is the perfectbase for my plans!").concat(piggy1.house.art, padding=5)

# However, there was a wolf in the forest that noticed the piggy's lovely new home
wolf = Wolf()

# Not just ANY wolf, a BIG BAD WOLF!
wolf.description = "Big Bad"
print wolf

# And he came up tot he piggy's house
print wolf.say("Little pig, Little pig, let me    come in").concat(piggy1.house.art, padding=15).concat(piggy1.say("Not by the hair on my   chinny chin chin!"))

print wolf.say("Then I'll huff and puff and blow  your house in!").concat(piggy1.house.art, padding=15).concat(piggy1.say("I'd like to see you try fool!"))

# So he huffed, and he puffed and he blew his house in...
print wolf.huff_and_puff(piggy1.house).concat(piggy1.say("NOOOOooooo..."))

# And ate that little piggy for breakfast.
print wolf.say("Deliiicioussss...").concat(piggy1.house.art, padding=15)

# The second pig got news of his brother's untimely demise, and decided he needed to be build an even stronger house.
piggy2 = pigs[1]
print man.say("Another Pig? This is the  busiest I been all week!").concat(piggy2.say("Hi, my name is Claude.  My brother got eaten,   and I here wolves are   allergic to sticks. You got any sticks?"), padding=15)

# The man had sympathy for his story, and lent his aid!
print man.say("I had a brother once...   Anywho, here's the sticks!").concat(piggy2.say("Thanks! Wish me luck!"), padding=15)

# And the first pig took that straw and build himself a house
piggy2.build_house(Material.STICK)
print piggy1.say("This will keep me safe!").concat(piggy2.house.art, padding=5)

# The Big Bad Wolf saw this house, and came over to pay a house-warming visit...
print wolf.say("Little pig, Little pig, let me    come in").concat(piggy2.house.art, padding=15).concat(piggy2.say("Not by the hair on my   chinny chin chin!"))

print wolf.say("Then I'll huff and puff and blow  your house in!").concat(piggy2.house.art, padding=15).concat(piggy2.say("Not this time!"))

# So he huffed, and he puffed and he blew his house in...
print wolf.huff_and_puff(piggy2.house).concat(piggy2.say("WWWWHHHhhhhyyyyy..."))

# And ate that little piggy for lunch.
print wolf.say("Just what I was craving!").concat(piggy2.house.art, padding=15)
