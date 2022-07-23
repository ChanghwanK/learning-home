def solution(s):
    answer = ""
    word_list = s.split(" ")
    changed_words = list()   
    
    for word in word_list:
        changed_words.append(change_word(word))
    
    for i in range(0, len(changed_words)):
        if i == len(changed_words)-1:
            answer += changed_words[i]
        else:
            answer += changed_words[i] + " "

    return answer
      

def change_word(word):
    changed_word = list()
    for i in range(0, len(word)):
        if i == 0 or (i % 2 == 0):
            changed_word.append(word[i].upper())
        else:
            changed_word.append(word[i].lower())
    return "".join(changed_word)