# random expression generator

from random import randint as rint, random as rnd


def make_expr(difficulty=5):

    wrappers = [
            lambda a,b : '%s + %s'%(a,b),
            lambda a,b : '%s * %s'%(a,b),
            lambda a,b : '%s / %s'%(a,b),
            lambda a,b : '%s // %s'%(a,b),
            lambda a,b : '%s - %s'%(a,b),
            lambda a,b : '%s ** %s'%(a,b),
            lambda a,b : '%s %s %s'%(a,'%',b),
            lambda a,b : '%s and %s'%(a,b),
            lambda a,b : '%s or %s'%(a,b),
            lambda a : '-%s'%a,
            lambda a : '(not %s)'%a,
            lambda a : 'bool(%s)'%a,
            lambda a : 'int(%s)'%a,
            lambda a : 'float(%s)'%a,
            lambda a : 'abs(%s)'%a
        ]

    wrap = lambda : wrappers[rint(0,len(wrappers)-1)]

    x = 1
    expr = []

    while x>0:
        x -= rnd()**difficulty
        expr.append(rint(0,len(wrappers)-1))

    while len(expr)>1:
        i = rint(0,len(expr)-1)
        a,b = None,None
        f = wrap()
        args = f.__code__.co_argcount
        delete = []
        if i>0 and isinstance(expr[i-1],str):
            a = expr[i-1]
            delete.append(i-1)
        else:
            a = rint(0,10)
            if rnd()>0.8: a += round(rnd(),1)
        if args>1 and i<len(expr)-1 and isinstance(expr[i+1],str):
            b = expr[i+1]
            delete.append(i+1)
        else:
            b = rint(0,10)
            if rnd()>0.8: b += round(rnd(),1)

        expr[i] = f(*(a,b)[:f.__code__.co_argcount])
        for k in delete[::-1]:
            del expr[k]

    return expr[0]


def testme(questions=10,incr=1):
    questions_ = [make_expr(i) for i in range(incr,questions*incr+1,incr)]
    correct = 0
    for q in range(len(questions_)):
        print()
        print('%s. Frage:'%(q+1))
        print(questions_[q])
        answer = input('What does it evaluate to?\n').replace(' ','').replace('\t','')
        try: correct_answer = str(eval(questions_[q]))
        except Exception as e:
            correct_answer = str(e)
        if correct_answer == answer:
            print('RICHTIG')
            correct += 1
        else:
            print('LEIDER FALSCH')
            print('RICHTIG GEWESEN WÄRE : %s'%correct_answer)

    print()
    print('%s / %s Punkte'%(correct,questions))
