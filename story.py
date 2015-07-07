from characters import Pig, Wolf, Man
# Once upon a time, when pigs still could rhyme
# There was a pig
print Pig()

# Oh crap wait, there were 3 pigs
print Pig() * 3

# Yea, so these three pigs decided that they wanted to do something with their lives!
# Naturally, the first thing to do for a pig in Ye-Old-America was to become a land owner
pigs = [Pig(), Pig(), Pig()]

man = Man()
print man.say("What can I do ye fer?").concat(pigs[0].say("Hello, my name is Benjamin. I shall become the  overlord of everything  you possess. I demand   all of your straw       ...please"), padding=15)

print man.say("Well ain't that just      dandier than a pickle in afish barrel! Here ya go").concat(pigs[0].say("Thanks! I mean...yea youbetter obey!"), padding=15)
