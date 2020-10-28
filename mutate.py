

def soft_mutate(word):
    mutable_letters = set(("b", "c", "d", "g", "ll", "p", "m", "rh", "t"))
    soft_map = {"b":"f", "ch":"ch", "c":"g", "dd":"dd", "d":"dd", "g":"",
                "ll":"l", "ph":"ph", "p":"b", "m":"f", "rh":"r", "th":"th",
                "t":"d"}
    do_not_mutate_list = ["golff", "gêm"]
    for mutable_letter in mutable_letters:
        if word.startswith(mutable_letter):
            for mutation in soft_map:
                if word.startswith(mutation):
                    if mutation not in ["g"]:
                        mutated_word = soft_map[mutation] + word[(len(mutation)):]
                    elif mutation is "g":
                        if word not in do_not_mutate_list:
                            mutated_word = word[1:]
                        else:
                            return word
                    return mutated_word
    return word

def nasal_mutate(word):
    mutable_letters = set(("b", "c", "d", "g", "p", "t"))
    nasal_map = {"b":"m", "ch":"ch", "c":"ngh", "dd":"dd", "d":"n", "g":"ng",
                 "p":"mh", "g":"ng", "th":"th", "t":"nh"}
    for mutable_letter in mutable_letters:
        if word.startswith(mutable_letter):
            for mutation in nasal_map:
                if word.startswith(mutation):
                    mutated_word = nasal_map[mutation] + word[(len(mutation)):]
                    return mutated_word
    return word

def aspirate_mutate(word):
    mutable_letters = set(("c", "p", "t"))
    nasal_map = {"ch":"ch", "c":"ch", "ph":"ph", "p":"ph", "th":"th", "t":"th"}
    for mutable_letter in mutable_letters:
        if word.startswith(mutable_letter):
            for mutation in nasal_map:
                if word.startswith(mutation):
                    mutated_word = nasal_map[mutation] + word[(len(mutation)):]
                    return mutated_word
    return word

def h_prothesise(word):
    mutable_letters = set(("a", "e", "i", "o", "w", "y"))
    do_not_mutate_list = set(["a", "ar", "i", "o", "w", "y", "yn"])
    if word not in do_not_mutate_list:
        for mutable_letter in mutable_letters:
            if word.startswith(mutable_letter):
                mutated_word = "h" + word
                return mutated_word
    return word


words = ["afal",
        "bara",
        "cath",
        "chwiban",
        "draig",
        "dderwen",
        "efail",
        "feiolin",
        "ffedog",
        "golau",
        "ngalaeth",
        "haul",
        "ieuenctid",
        "kilo",
        "jeli",
        "lori",
        "llwynog",
        "map",
        "nos",
        "priodas",
        "riwbob",
        "rhuban",
        "sidan",
        "shifft",
        "tebot",
        "theori",
        "uwd",
        "volt",
        "wybren",
        "x-ray",
        "ysgol",
        "zebra"]

for word in words:
   print (word, ": fy " + nasal_mutate(word), ", gyda", aspirate_mutate(word), ", dy", soft_mutate(word), ", ei", aspirate_mutate(h_prothesise(word)))
