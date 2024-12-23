import itertools

def load_english_words(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().lower() for line in file.readlines()]

def generate_combinations(rule, categories):
    return [''.join(combination) for combination in itertools.product(*[categories[cat] for cat in rule])]

def calculate_difficulty(combination, difficulty_scores):
    return sum(difficulty_scores.get(symbol, 0) for symbol in combination)

def create_sorted_combinations(rules, categories, difficulty_scores):
    combinations = set()
    for rule in rules:
        combinations.update(generate_combinations(rule, categories))

    sorted_combinations = sorted(combinations, key=lambda comb: calculate_difficulty(comb, difficulty_scores))
    return sorted_combinations

def create_conlang_dictionary(english_words, sorted_combinations):
    conlang_dictionary = {}
    for eng_word, conlang_word in zip(english_words, sorted_combinations):
        conlang_dictionary[eng_word] = conlang_word
    return conlang_dictionary

def translate_to_conlang(english_string, conlang_dictionary):
    # Split the string into words
    english_words = english_string.lower().split()

    # Translate each word
    conlang_words = []
    for word in english_words:
        # Use the conlang word if it exists, otherwise keep the English word
        conlang_word = conlang_dictionary.get(word, word)
        conlang_words.append(conlang_word)

    # Reassemble into a string
    conlang_string = ' '.join(conlang_words)
    return conlang_string

# Define IPA symbols for each category
ipa_categories = {
    'vowel': ['i', 'ɪ', 'e', 'æ', 'ɑ', 'ɒ', 'ɔ', 'ʌ', 'ʊ', 'u', 'ə', 'aɪ', 'aʊ', 'oʊ', 'eɪ', 'ɔɪ'],
    'stop': ['p', 'b', 't', 'd', 'k', 'g'],
    'fricative': ['f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'h'],
    'affricate': ['tʃ', 'dʒ'],
    'nasal': ['m', 'n', 'ŋ'],
    'liquid': ['r', 'l'],
    'glide': ['j', 'w'],
    'syllabic_consonant': ['l̩', 'n̩']
}

# Assign difficulty values to each IPA symbol
difficulty_scores = {}

# Monophthong vowels
difficulty_scores['i'] = 4
difficulty_scores['ɪ'] = 3
difficulty_scores['e'] = 3
difficulty_scores['æ'] = 4
difficulty_scores['ɑ'] = 1
difficulty_scores['ɒ'] = 1
difficulty_scores['ɔ'] = 1
difficulty_scores['ʌ'] = 0
difficulty_scores['ʊ'] = 1
difficulty_scores['u'] = 1
difficulty_scores['ə'] = 0

# Diphthong vowels
difficulty_scores['aɪ'] = 4
difficulty_scores['aʊ'] = 4
difficulty_scores['oʊ'] = 5
difficulty_scores['eɪ'] = 6
difficulty_scores['ɔɪ'] = 6

# Stops
difficulty_scores['p'] = 2
difficulty_scores['b'] = 3
difficulty_scores['t'] = 3
difficulty_scores['d'] = 4
difficulty_scores['k'] = 4
difficulty_scores['g'] = 5

# Fricatives
difficulty_scores['f'] = 3
difficulty_scores['v'] = 4
difficulty_scores['θ'] = 6
difficulty_scores['ð'] = 6
difficulty_scores['s'] = 4
difficulty_scores['z'] = 5
difficulty_scores['ʃ'] = 3
difficulty_scores['ʒ'] = 4
difficulty_scores['h'] = 1

# Affricates
difficulty_scores['tʃ'] = 5
difficulty_scores['dʒ'] = 5

# Nasals
difficulty_scores['m'] = 1
difficulty_scores['n'] = 1
difficulty_scores['ŋ'] = 2

# Liquids
difficulty_scores['r'] = 2
difficulty_scores['l'] = 1

# Glides
difficulty_scores['j'] = 1
difficulty_scores['w'] = 1

# Syllabic consonants
difficulty_scores['l̩'] = 2
difficulty_scores['n̩'] = 2

# Define rules
rules = [
    ['vowel'],
    ['vowel', 'glide'],
    ['glide', 'vowel'],
    ['vowel', 'stop'],
    ['stop', 'vowel'],
    ['stop', 'fricative'],
    ['fricative', 'stop'],
    ['nasal', 'vowel'],
    ['vowel', 'nasal'],
    ['liquid', 'vowel'],
    ['vowel', 'liquid'],
    ['affricate', 'vowel'],
    ['vowel', 'affricate'],
    ['glide', 'vowel', 'stop'],
    ['stop', 'vowel', 'glide'],
    ['fricative', 'vowel'],
    ['vowel', 'fricative'],
    ['nasal', 'vowel', 'stop'],
    ['stop', 'vowel', 'nasal'],
    ['liquid', 'vowel', 'stop'],
    ['stop', 'vowel', 'liquid'],
    ['affricate', 'vowel', 'stop'],
    ['stop', 'vowel', 'affricate'],
    ['glide', 'vowel', 'fricative'],
    ['fricative', 'vowel', 'glide'],
    ['nasal', 'vowel', 'fricative'],
    ['fricative', 'vowel', 'nasal'],
    ['liquid', 'vowel', 'fricative'],
    ['fricative', 'vowel', 'liquid'],
    ['affricate', 'vowel', 'fricative'],
    ['fricative', 'vowel', 'affricate'],
    ['glide', 'vowel', 'nasal'],
    ['nasal', 'vowel', 'glide'],
    ['liquid', 'vowel', 'nasal'],
    ['nasal', 'vowel', 'liquid'],
    ['affricate', 'vowel', 'nasal'],
    ['nasal', 'vowel', 'affricate'],
    ['glide', 'vowel', 'liquid'],
    ['liquid', 'vowel', 'glide'],
    ['affricate', 'vowel', 'liquid'],
    ['liquid', 'vowel', 'affricate'],
    ['glide', 'vowel', 'affricate'],
    ['affricate', 'vowel', 'glide'],
    ['syllabic_consonant', 'vowel'],
    ['vowel', 'syllabic_consonant'],
    ['syllabic_consonant', 'vowel', 'stop'],
    ['stop', 'vowel', 'syllabic_consonant'],
    ['syllabic_consonant', 'vowel', 'fricative'],
    ['fricative', 'vowel', 'syllabic_consonant'],
    ['syllabic_consonant', 'vowel', 'nasal'],
    ['nasal', 'vowel', 'syllabic_consonant'],
    ['syllabic_consonant', 'vowel', 'liquid'],
    ['liquid', 'vowel', 'syllabic_consonant'],
    ['syllabic_consonant', 'vowel', 'glide'],
    ['glide', 'vowel', 'syllabic_consonant'],
    ['syllabic_consonant', 'vowel', 'affricate'],
    ['affricate', 'vowel', 'syllabic_consonant'],
    ['vowel', 'glide', 'vowel'],
    ['vowel', 'stop', 'vowel'],
    ['stop', 'fricative', 'vowel'],
    ['fricative', 'stop', 'vowel'],
    ['vowel', 'liquid', 'vowel'],
    ['vowel', 'affricate', 'vowel'],
    ['glide', 'vowel', 'stop', 'vowel'],
    ['stop', 'vowel', 'glide', 'vowel'],
    ['vowel', 'fricative', 'vowel'],
    ['nasal', 'vowel', 'stop', 'vowel'],
    ['liquid', 'vowel', 'stop', 'vowel'],
    ['stop', 'vowel', 'liquid', 'vowel'],
    ['affricate', 'vowel', 'stop', 'vowel'],
    ['stop', 'vowel', 'affricate', 'vowel'],
    ['glide', 'vowel', 'fricative', 'vowel'],
    ['fricative', 'vowel', 'glide', 'vowel'],
    ['nasal', 'vowel', 'fricative', 'vowel'],
    ['liquid', 'vowel', 'fricative', 'vowel'],
    ['fricative', 'vowel', 'liquid', 'vowel'],
    ['affricate', 'vowel', 'fricative', 'vowel'],
    ['fricative', 'vowel', 'affricate', 'vowel'],
    ['nasal', 'vowel', 'glide', 'vowel'],
    ['liquid', 'vowel', 'nasal', 'vowel'],
    ['nasal', 'vowel', 'liquid', 'vowel'],
    ['affricate', 'vowel', 'nasal', 'vowel'],
    ['nasal', 'vowel', 'affricate', 'vowel'],
    ['glide', 'vowel', 'liquid', 'vowel'],
    ['liquid', 'vowel', 'glide', 'vowel'],
    ['affricate', 'vowel', 'liquid', 'vowel'],
    ['liquid', 'vowel', 'affricate', 'vowel'],
    ['glide', 'vowel', 'affricate', 'vowel'],
    ['affricate', 'vowel', 'glide', 'vowel'],
    ['vowel', 'syllabic_consonant', 'vowel'],
    ['syllabic_consonant', 'vowel', 'stop', 'vowel'],
    ['stop', 'vowel', 'syllabic_consonant', 'vowel'],
    ['syllabic_consonant', 'vowel', 'fricative', 'vowel'],
    ['fricative', 'vowel', 'syllabic_consonant', 'vowel'],
    ['syllabic_consonant', 'vowel', 'nasal', 'vowel'],
    ['nasal', 'vowel', 'syllabic_consonant', 'vowel'],
    ['syllabic_consonant', 'vowel', 'liquid', 'vowel'],
    ['liquid', 'vowel', 'syllabic_consonant', 'vowel'],
    ['syllabic_consonant', 'vowel', 'glide', 'vowel'],
    ['glide', 'vowel', 'syllabic_consonant', 'vowel'],
    ['syllabic_consonant', 'vowel', 'affricate', 'vowel'],
    ['affricate', 'vowel', 'syllabic_consonant', 'vowel'],
    ['vowel', 'glide', 'vowel'],
    ['vowel', 'stop', 'vowel'],
    ['vowel', 'stop', 'fricative'],
    ['vowel', 'fricative', 'stop'],
    ['vowel', 'nasal', 'vowel'],
    ['vowel', 'liquid', 'vowel'],
    ['vowel', 'affricate', 'vowel'],
    ['vowel', 'glide', 'vowel', 'stop'],
    ['vowel', 'stop', 'vowel', 'glide'],
    ['vowel', 'fricative', 'vowel'],
    ['vowel', 'nasal', 'vowel', 'stop'],
    ['vowel', 'stop', 'vowel', 'nasal'],
    ['vowel', 'liquid', 'vowel', 'stop'],
    ['vowel', 'stop', 'vowel', 'liquid'],
    ['vowel', 'affricate', 'vowel', 'stop'],
    ['vowel', 'stop', 'vowel', 'affricate'],
    ['vowel', 'glide', 'vowel', 'fricative'],
    ['vowel', 'fricative', 'vowel', 'glide'],
    ['vowel', 'nasal', 'vowel', 'fricative'],
    ['vowel', 'fricative', 'vowel', 'nasal'],
    ['vowel', 'liquid', 'vowel', 'fricative'],
    ['vowel', 'fricative', 'vowel', 'liquid'],
    ['vowel', 'affricate', 'vowel', 'fricative'],
    ['vowel', 'fricative', 'vowel', 'affricate'],
    ['vowel', 'glide', 'vowel', 'nasal'],
    ['vowel', 'nasal', 'vowel', 'glide'],
    ['vowel', 'liquid', 'vowel', 'nasal'],
    ['vowel', 'nasal', 'vowel', 'liquid'],
    ['vowel', 'affricate', 'vowel', 'nasal'],
    ['vowel', 'nasal', 'vowel', 'affricate'],
    ['vowel', 'glide', 'vowel', 'liquid'],
    ['vowel', 'liquid', 'vowel', 'glide'],
    ['vowel', 'affricate', 'vowel', 'liquid'],
    ['vowel', 'liquid', 'vowel', 'affricate'],
    ['vowel', 'glide', 'vowel', 'affricate'],
    ['vowel', 'affricate', 'vowel', 'glide'],
    ['vowel', 'syllabic_consonant', 'vowel'],
    ['vowel', 'syllabic_consonant', 'vowel', 'stop'],
    ['vowel', 'stop', 'vowel', 'syllabic_consonant'],
    ['vowel', 'syllabic_consonant', 'vowel', 'fricative'],
    ['vowel', 'fricative', 'vowel', 'syllabic_consonant'],
    ['vowel', 'syllabic_consonant', 'vowel', 'nasal'],
    ['vowel', 'nasal', 'vowel', 'syllabic_consonant'],
    ['vowel', 'syllabic_consonant', 'vowel', 'liquid'],
    ['vowel', 'liquid', 'vowel', 'syllabic_consonant'],
    ['vowel', 'syllabic_consonant', 'vowel', 'glide'],
    ['vowel', 'glide', 'vowel', 'syllabic_consonant'],
    ['vowel', 'syllabic_consonant', 'vowel', 'affricate'],
    ['vowel', 'affricate', 'vowel', 'syllabic_consonant']
]

# Generate and sort combinations
sorted_combinations = create_sorted_combinations(rules, ipa_categories, difficulty_scores)
print(sorted_combinations)
print(len(sorted_combinations))

# Load English words
english_words = load_english_words('freq_list.txt')

# Create the conlang dictionary
conlang_dictionary = create_conlang_dictionary(english_words, sorted_combinations)

# Print the first 20 entries
for eng_word, conlang_word in list(conlang_dictionary.items())[:20]:
    print(f"{eng_word}: {conlang_word}")

english_string = "hello how are you my hovercraft is full of eels"
conlang_string = translate_to_conlang(english_string, conlang_dictionary)
print(conlang_string)
