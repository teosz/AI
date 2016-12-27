
# coding: utf-8

# In[1]:

# globals
Alphabet = {}
Tests = []

def init():
    with open("alphabet.txt") as f:
        AlphabetRaw = " ".join(f.readlines())

    alphalist = AlphabetRaw.split()
    i = 0
    while i < len(alphalist):
        Alphabet[alphalist[i]] = alphalist[i+1]
        i += 2

    for i in range(4):
        with open("tests/test" + str(i + 1) + ".txt") as ftest:
            lines = ftest.readlines()
            code = lines[0].strip()
            dictionary = [line.strip() for line in lines[1:]]
            Tests.append((code, dictionary))
init()

# print(Alphabet)
# print(Tests[0:3])


# In[1]:

def tt_translate(words):
    return "".join(["".join([Alphabet[char] for char in word]) for word in words])


def tt_check(code, dic, sols, a):
    error = False
    if a != len(sols):
        print("number of solutions is incorrect. Should be", a)
        error = True
    i = 0
    for s in sols:
        so = tt_translate(s)
        if so != code:
            print("solution #" + i, "translates to code different from input: [", so, "]")
            error = True
        i += 1
    return not error
            

def tt_test(solver, code, dic, a):
    if len(code) > 100:
        debug = False
    print("======================================= input ( length =", len(code), "):")
    print(code[:100] + (" (...)" if len(code) > 100 else ""))
    solutions = solver(Alphabet, code, dic)
    print("======================================= solution:")
    sep = " " if len(solutions) < 5 else "\n"
    solutions.sort()
    print(len(solutions), "solution(s):" + sep, ("," + sep).join([" ".join(sol) for sol in solutions]))
    print("=======================================")
    res = tt_check(code, dic, solutions, a)
    print("OK" if res else "FAILED")
    return res
    
def tt_TA(solver, ACTIVATEBONUS = False):
    i = 0
    for t in (Tests[:-1] if not ACTIVATEBONUS else Tests):
        tt_test(*([solver]+list(t)+[[1, 1, 2, 72, 5][i]]))
        i += 1

