
def is_subsequence(subseq, seq):
    subseq.reverse()
    for elem in seq:
        if not subseq:
            return True
        if elem == subseq[-1]:
            subseq.pop()
    if subseq:
        return False
    return True


if __name__ == '__main__':
    subseq = list(input())
    seq = list(input())
    print(is_subsequence(subseq, seq))


# def is_subsequence(subseq, seq):
#     current_pos = 0
#     for elem in subseq:
#         current_pos = seq.find(elem, current_pos) + 1
#         if current_pos == 0:
#             return False
#     return True
# 
# 
# if __name__ == '__main__':
#     subseq = input()
#     seq = input()
#     print(is_subsequence(subseq, seq))
# 