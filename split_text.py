def split_foods(text):
    words = text.split(':',1)[1]
    return split_text(words)

def split_text(text):
    words = text.split(',',1)
    return words

print(split_foods('Hey Nutribot. Today I had: Mcdonald\'s Cheeseburger, 16 oz. Dr. Pepper'))
