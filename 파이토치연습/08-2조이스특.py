def solution(name):
    name = list(name)
    base_l = list('A'*len(name))
    base_r = list('A'*len(name))
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    left = 0
    right = 0
    answer_l = 0
    answer_r = 0
    while True:
        # 좌로 만 움직이는 경우
        answer_l += min(alphabet.index(name[left]), (len(alphabet) - alphabet.index(name[left])))
        base_l[left] = name[left]
        if base_l == name:
            break
        left -= 1
        answer_l += 1
    while True:
        # 우로만 움직이는 경우
        answer_r += min(alphabet.index(name[right]), (len(alphabet) - alphabet.index(name[right])))
        base_r[right] = name[right]
        if base_r == name:
            break
        right += 1
        answer_r += 1
    return min(answer_l, answer_r)


