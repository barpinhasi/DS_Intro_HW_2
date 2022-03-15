###~~~~~~~~~~~ A ~~~~~~~~~~~###
def reverse(sentence, reverse_word):
    res = sentence.split()
    if type(reverse_word) != str:
        return "invalid input" 
    elif reverse_word not in res:
        return "no match word found"
    for j,i in enumerate(res):
        if i == reverse_word:
            res[j] = i[::-1]
            break;
    return (' '.join(res))

###~~~~~~~~~~~ b ~~~~~~~~~~~###
def compute_equation(equation):
    return eval(equation), type(eval(equation))

