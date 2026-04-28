def solution(word):
    all_words = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def generate(current_word):
        if len(current_word) > 5:
            return
        
        if current_word:
            all_words.append(current_word)
        
        for v in vowels:
            generate(current_word + v)
            
    generate("")
    
    return all_words.index(word) + 1