def smile_2(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True
    elif a_smile == False and b_smile == False:
        return True
    else:
        return False

def int_sum(s,t):
    if s==t:
        return 2*(s+t)
    else:
        return (s+t)



def problem4(t):
    hours = []
    for i in range(t+1,24,1):
        hours.append(i)
    return hours

def problem4_1(t):
    return list (range(h+1,24))

def prob_5(a,b,negative):
    if a<0 and b>0:
        return True
    elif a>0 and b<0:
        return True
    elif a<0 and b<0:
        if  negative ==True:
            return True
        else:
            return False
    else:
        return False

def prob_6(wordd) :
    s = wordd
    mid = s[1:-1]
    first_ltr = s[0]
    last_ltr = s[-1]
    word_final = last_ltr+mid+first_ltr
    return word_final

def prob_7(worddd,num):

    s = worddd
    if len(s)>2:
        front = s[:3]
        return num*front
def prob_8(s,num):
    if len(s)>1:
        back = s[-2:]
        return num*back

def prob_9(s):
    length1 = len(s)
    length2 = length1*2
    last_el = s[-1]
    new_list = []
    for i in range(length2):
        new_list.append(0)
    new_list[-1] = last_el

    return new_list

def prob_9_2(g_l):
    new_list = [0] * len(g_l) *2
    new_list[-1] = g_l[-1]
    return new_list

def porb_10(num):
    total = 0
    for i in num:
        if i == 9:
            total +=1
    return total

def prob_10_2(num):
    return num.count(9)


if __name__ == '__main__':
    val3 = prob_10_2([1,9,6,9])
    print(val3)

    f=lambda x : x*x
    print(f(12))

    h=lambda a,b: a*a + b
    print(h(3,1))

