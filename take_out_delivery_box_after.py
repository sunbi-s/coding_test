def solution(n, w, num):
    '''
    n = 총 택배 상자수
    w = 가로 길이
    num = 찾아야 되는 상자
    
    '''
    
    m1  = num % (2*w)
    m2  = ((2*w) + 1- m1) % (2*w)
    

    answer = 0
    for i in range(num, n + 1):
        r = i % (2 * w)
        if r == m1 or r == m2:
            answer += 1
    
    return answer