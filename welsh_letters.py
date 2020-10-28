welsh_singletons = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m",
                    "n", "o", "p", "r", "s", "t", "u", "w", "y"]

welsh_digraphs = ["ch", "dd", "ff", "ng", "ll", "ph", "rh", "th"]

welsh_alphabet = ["a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng",
                  "h", "i", "j", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh",
                  "s", "t", "th", "u", "w", "y"]

supplemental_letters = ["k", "q", "v", "x", "z"]

letters_in_welsh = welsh_alphabet + supplemental_letters

exceptions = {"arholiad":"rh", "arholi":"rh","bangor":"ng", "llongyfarch":"ng"}

test_words = ["llaeth", "achwyn", "deddf", "chynghorwyr", "llyncom", "llumanu",
         "iâr", "ci", "gafr", "cath", "mwnci", "ceffylau", "hwyaid", "ceiliog",
         "angor", "bangor", "arholi", "rhwyfo", "llechoch", "llongyfarch"]

def get_welsh_letter_count(word):
    word = word.lower()
    for welsh_digraph in welsh_digraphs:
        if welsh_digraph is not exceptions.get(word):
            word = word.replace(welsh_digraph, "@")
    return len(word)
