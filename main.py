noun = input("Type a noun: ")
verb = input("Type a verb: ")
adj = input("Type an adjective: ")
s_pronoun = input("Type a singular pronoun: ")
ing_verb = input("Type a verb ending in -ing: ")


def mad_lib_gen():
    print("")
    print("Hello class my name is " + noun + "!")
    print("Today we will be learning how to " + verb + " a cow.")
    print("The art of " + verb + "ing a cow is to perfect it like a " + adj + " airplane!")
    print("The cow for one, would like to be called a " + s_pronoun + ".")
    print("This is because the cow developed a new way to pretend to be " + ing_verb + "!")


mad_lib_gen()
