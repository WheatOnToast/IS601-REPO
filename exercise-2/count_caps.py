def count_caps(sentence):
    if type(sentence) != str:
        return False
    
    split_sentence = sentence.split()
    capital_word_count = 0
    
    for word in split_sentence:
        if word[0].isupper() == True:
            capital_word_count += 1
    
    return capital_word_count