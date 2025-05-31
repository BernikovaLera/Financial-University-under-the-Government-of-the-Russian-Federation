import nltk


print(nltk.edit_distance('Левенштейн', 'Левинтшейна', transpositions=True, substitution_cost=3))


print(nltk.edit_distance('Левенштейн', 'Левинтшейна', transpositions=True))


print(nltk.edit_distance('Левенштейн', 'Левинтшейна'))


print(nltk.edit_distance('Левенштейн', 'Левинтшейна', substitution_cost=3))