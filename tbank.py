# def solve():
#     L, W = map(int, input().split())
#     A, B = map(int, input().split())
    
#     horiz = (L - A + 1 + A - 1) // A 
#     vert = (W - B + 1 + B - 1) // B
    
#     print(horiz * vert)

# if __name__ == "__main__":
#     solve()

# def solve():
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))

#     reachable = set([a[0]])
#     res = [0] * n
#     res[0] = 1

#     for i in range(1, n):
#         temp_h = a[i]
#         ok = False

#         for rh in reachable:
#             if abs(rh - temp_h) <= k:
#                 ok = True
#                 break
#         if ok:
#             res[i] = 1
#             reachable.add(temp_h)
#         else:
#             res[i] = 0

#     print(' '.join(map(str, res)))
# if __name__ == "__main__":
#     solve()


# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# answer = 0
# l = 0

# for r in range(n):
#     current_min = min(a[l:r+1])
#     current_max = max(a[l:r+1])

#     while current_max - current_min > k:
#         l += 1
#         current_max = max(a[l:r+1])
#         current_min = min(a[l:r+1])
        
#     answer += (r - l + 1)

# print(answer)

# def main():
#     n = int(input().strip())
#     radius = list(map(int, input().split()))
#     if len(radius) != n:
#         return None
    
#     cnt1 = 0  
#     cnt5 = 0  
    
#     for r in radius:
#         if r == 0:
#             cnt1 += 1
#         else:
#             if (r - 1) % 6 < 3:
#                 cnt5 += 1
#             else:
#                 cnt1 += 1
    
#     total_mod = (cnt1 * 1 + cnt5 * 5) % 8
    
#     if total_mod == 0:
#         print(0)
#         return
    
#     answer = float('inf')
    
#     for b in range(0, min(cnt5, 7) + 1):
#         a_needed = (total_mod - 5 * b) % 8
        
#         if a_needed <= cnt1:
#             answer = min(answer, a_needed + b)
    
#     if total_mod <= cnt1:
#         answer = min(answer, total_mod)
    
#     print(answer if answer != float('inf') else -1)

# if __name__ == "__main__":
#     main()

# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# max_score = 0
# for i in range(1, n):
#     max_score = max(max_score, sum(a[:i + 1]))
    
# print(max(0, max_score))