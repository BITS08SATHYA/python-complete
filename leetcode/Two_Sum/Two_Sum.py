def two_sum(l1, l2):
    result = []

    if len(l1) == 0 or len(l2) == 0 or len(l1) != len(l2):
        return

    carryOn = 0
    for x,y in zip(l1, l2):
        sum = x + y + carryOn
        if sum > 9:
            first, second = map(int, str(sum))
            result.append(int(second))
            carryOn += int(first)
        else:
            result.append(sum)
            carryOn = 0


    return result

# def twosum(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     dummy = ListNode(0) # start with a dummy node
#     curr = dummy   # pointer to build result list
#     carry = 0  # carry from addition
#     p,q = l1,l2  # pointers for traversing l1, l2
#
#     while p or q or carry:
#         x = p.val if p else 0
#         y = q.val if q else 0
#         carry, digit = divmod(x + y + carry, 10)
#
#         curr.next = ListNode(digit)
#         curr = curr.next
#
#         p = p.next if p else None
#         q = q.next if q else None
#
#     return dummy.next



l1 = [2, 4, 3]
l2 = [5, 6, 4]
print(two_sum(l1, l2))