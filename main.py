import itertools

with open('words_alpha.txt','r') as f:
    all_words = [line.rstrip() for line in f]


my_words = [
    'Cocreative',
    'Design',
    'Interface',
]

good_words = []

for num_twos in range(len(my_words)+1):
    ind_list = [1 for x in range(len(my_words))]
    for i in range(num_twos):
        ind_list[i] += 1

    many_inds = list(set(itertools.permutations(ind_list)))
    
    for inds in many_inds:
        strings = []
        for k, word in enumerate(my_words):
            strings.append(word[:inds[k]])
        permutations = list(set(itertools.permutations(strings)))
        
        for perm in permutations:
            madeup_word = ''.join(perm)
            if madeup_word.lower() in all_words:
                good_words.append(madeup_word)

if not good_words:
    print('no words found')
else:
    for word in good_words:
        print(word)
