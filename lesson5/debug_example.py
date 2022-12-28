goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

longest_word = goods[0][0]
longst_words = []
for fruits_list in goods:
    for fruit in fruits_list:
        if len(fruit) > len(longest_word):
            longest_word = fruit
            longst_words = [fruit]
        elif len(fruit) == len(longest_word):
            longst_words.append(fruit)

# ['breadfruit', 'cloudberry', 'blackberry']
print(f"the longest word is {longst_words} ")