import random

a_gramm = { 'S' : ['a', 'b', 'c'] }
t_gramm = [ ('S', 'A', 'B'), ('S', 'A', 'R'), ('R', 'S', 'B'), ('S', 'B', 'R') ]
p_gramm = [ ('A', 0), ('B', 1) ]

# Converts grammars from the form
# [(L1, R1), (L1, R2)] to the form
# { L1 : [R1, R2] }
def convertGrammar(gramm1, gramm2):
        newGram = {}
        for g in gramm1:
                if g[0] in newGram:
                        newGram[g[0]].append(list(g[1:]))
                else:
                        newGram[g[0]] = [list(g[1:])]
        for g in gramm2:
                if g[0] in newGram:
                        newGram[g[0]].append(list(g[1:]))
                else:
                        newGram[g[0]] = [list(g[1:])]
        return newGram

# returns a list of terminals given a list of nonterminals to terminals
def getTerminals(gramm):
        tGram = []
        for g in gramm:
                tGram.extend(g[1:])
        return tGram

# returns true if the symbol is in the symbollist
def inList(sym, termlist):
        if sym in termlist:
                return True
        else:
                return None

# returns a random right hand side of the grammar
def getRandomRHS(gramm, sym):
        rhs = gramm[sym]
        count = len(rhs)
        return rhs[random.randint(0, count - 1)]

# PL is Lexical Phrases, P are non-lexical phrases
# sym should be a start symbol
def genRandSentence(PL, P, sym):
        gramm = convertGrammar(PL, P)
        terms = getTerminals(PL)

        lastTerminal = 0
        sentence = []

        sentence.extend(getRandomRHS(gramm, sym))
    
        while lastTerminal < len(sentence):
                if inList(sentence[lastTerminal], terms):
                        lastTerminal = lastTerminal + 1
                else:
                        rhs = getRandomRHS(gramm, sentence[lastTerminal])
                        del sentence[lastTerminal]
                        for x in range(0, len(rhs)):
                                sentence.insert(lastTerminal + x, rhs[x])
        return sentence



