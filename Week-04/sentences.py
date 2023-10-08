import random

#Week 04
#Write the second half of a Python program that generates simple English sentences that you began in the previous lesson’s prove milestone. As part of the previous lesson’s prove milestone, you wrote a program that generates English sentences with three parts: a determiner, a noun, and a verb. During this prove assignment, you will add functions so that your program generates sentences with four parts:

#a determiner
#a noun
#a verb
#a prepositional phrase

def get_determiner(quantity):
    if quantity == 1:
        words = ["The", "A", "One"]
    else:
        words = ["Some", "Many", "The"]

    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "child", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        if quantity == 1:
            verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "spoke", "walked", "wrote"]
        else:
            verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "spoke", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "speaks", "walks", "writes"]
        else:
            verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "speak", "walk", "write"]
    elif tense == "future":
        if quantity == 1:
            verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will speak", "will walk", "will write"]
        else:
            verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will speak", "willwalk", "will write"]

    verb = random.choice(verbs)
    return verb

def get_preposition():
    prepositions = ["over", "above", "through", "after", "along", "around", "in", "before", "behind", "down", "beyond", "by", "despite", "except", "for", "of", "on", "onto", "near", "off", "on", "out", "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    preposition = get_preposition()
    prepositional_phrase = f"{preposition} {determiner} {noun}"

    return prepositional_phrase

def make_sentence():
    quantity = random.choice([1, 2])
    tense = random.choice(["past", "present", "future"])

    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    
    sentence = f"{determiner} {noun} {verb} {prepositional_phrase}."
    return sentence

def main():
    sentences = [
        (1, "past"),
        (1, "present"),
        (1, "future"),
        (2, "past"),
        (2, "present"),
        (2, "future")
    ]

    for quantity, tense in sentences:
        sentence = make_sentence()
        print(sentence)

if __name__ == "__main__":
    main()