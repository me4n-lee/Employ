#프로그래머스
#영어 끝말잇기

def solution(n, words):

    num = 0
    word = []

    a = len(words)

    for i in range(a):

        if i == 0:
            word.append(words[i])

        else:

            #만약 끝말잇기가 안됐다면
            if words[i-1][-1] != words[i][0]:
                num = i+1
                break

            #만약 단어가 이미 써져있다면
            if words[i] in word:
                num = i+1
                break

            word.append(words[i])


    print(num)

    ans1 = 0
    ans2 = 0

    if num != 0:
        if num%n == 0:
            ans1 = n
            ans2 = num//n
        else:
            ans1 = num%n
            ans2 = num//n + 1

    answer = [ans1, ans2]

    return answer