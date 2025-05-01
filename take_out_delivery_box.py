import math 
def solution(n, w, num):
    '''
    n = 총 택배 상자수
    w = 가로 길이
    num = 찾아야 되는 상자
    
    '''
    
    
    h = math.ceil(n / w)  
    
    # 세로, 가로 순
    store = [[0 for _ in range(w)] for _ in range(h)] 
    
    # box 쌓기
    box_num = 1
    for i in range(h):
        for j in range(w):
             # 종료 조건
             if box_num > n:
                break
             else:
                # 짝수
                if i % 2 == 0:
                    store[i][j] = box_num
                # 홀수
                else:
                    store[i][w-1-j] = box_num
                box_num += 1
    
    # 지정한 box 위치 찾기
    def find_box(store, num):
        for i in range(h):
            for j in range(w):
                if num == store[i][j]:
                    return i , j
    
    col, row = find_box(store, num)
    
    # box 위로 몇개나 있는지 체크 (자기 포함)
    total_box = 0
    for i in range(col,h):
        box_num = store[i][row]
        if box_num != 0:
            total_box += 1  
    
    answer = total_box
    return answer