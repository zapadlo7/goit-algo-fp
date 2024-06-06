class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        self.head = reverse_list(self.head)

    def sort(self):
        self.head = merge_sort(self.head)

    @staticmethod
    def merge_sorted_lists(l1, l2):
        merged_head = merge_two_sorted_lists(l1.head, l2.head)
        merged_list = LinkedList()
        merged_list.head = merged_head
        return merged_list

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_sort(head):
    if not head or not head.next:
        return head

    def split(head):
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return head, slow

    def merge(l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    left, right = split(head)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

# Використання:
# Створення і заповнення першого списку
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

# Створення і заповнення другого списку
ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

# Виведення початкових списків
print("Перший список:")
ll1.print_list()

print("Другий список:")
ll2.print_list()

# Реверсування першого списку
ll1.reverse()
print("Реверсований перший список:")
ll1.print_list()

# Сортування другого списку
ll2.sort()
print("Відсортований другий список:")
ll2.print_list()

# Об'єднання двох відсортованих списків
merged_list = LinkedList.merge_sorted_lists(ll1, ll2)
print("Об'єднаний відсортований список:")
merged_list.print_list()
