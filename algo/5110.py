import sys
sys.stdin = open("5110.txt")

# for tc in range(1, int(input())+1):
#     N, M = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(M)]
#     print(arr)
#     test = []
#     for i in range(M):
#         print(arr[i])
#         count = 0
#         if len(test) == 0:
#             test += arr[i]
#         else:
#             for a in range(len(test)):
#                 if test[a] > arr[i][0]:
#                     for b in range(len(arr[i])):
#                         test.insert(test[a], arr[i][len(arr[i])-b])
#                     count += 1
#                     break
#
#                 #     break
#                 # if count >= 1:
#                 #     break
#                 # print(test)
#         print(test)