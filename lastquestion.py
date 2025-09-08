def question_8()->int:
    sentence = "Question 1 contained 2 sections and was worth 4 out of a total of 8 marks"
    text_nums = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    new_sentence = ""
    
    for i in range(len(sentence)):
        if sentence[i] in digits:
            pos = int(sentence[i])
            new_sentence = new_sentence + text_nums[pos]
        else:
            new_sentence = new_sentence + sentence[i]
    # endif
                
    print(new_sentence)
# end of procedure

question_8()