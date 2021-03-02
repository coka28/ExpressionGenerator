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
    global x,y
    x = difficulty
    y = 0

    def add():
        global x,y
        x -= rnd()
        if rnd()<1/difficulty or x<0:
            if y>0: return rint(0,9) + (round(rnd(),1) if rnd()<0.1 else 0)
            else: pass
        y += 1

        f = wrap()
        args = f.__code__.co_argcount
        return f(*(add(),add())[:args])

    return str(add())
        


def testme(questions=10,incr=1):
    questions_ = [make_expr(incr*i) for i in range(1,questions+1)]
    correct = 0
    for q in range(len(questions_)):
        print()
        print('%s. Frage:'%(q+1))
        print(questions_[q])
        answer = input('What does it evaluate to?\n')
        try:
            correct_answer = str(eval(questions_[q]))
            answer = answer.replace(' ','').replace('\t','')
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
