class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    previous = None
    current = head
    while current:
        next_node = current.next  # Зберігаємо наступний вузол
        current.next = previous   # Реверсуємо посилання
        previous = current        # Переміщаємо previous на один вузол вперед
        current = next_node       # Переміщаємо current на один вузол вперед
    return previous

def insertion_sort_list(head):
    sorted_head = None
    current = head
    while current:
        next_node = current.next
        sorted_head = insert_into_sorted_list(sorted_head, current)
        current = next_node
    return sorted_head

def insert_into_sorted_list(sorted_head, node_to_insert):
    if not sorted_head or node_to_insert.value < sorted_head.value:
        node_to_insert.next = sorted_head
        return node_to_insert
    current = sorted_head
    while current.next and current.next.value < node_to_insert.value:
        current = current.next
    node_to_insert.next = current.next
    current.next = node_to_insert
    return sorted_head


def merge_two_sorted_lists(l1, l2):
    dummy_head = ListNode()
    tail = dummy_head
    while l1 and l2:
        if l1.value < l2.value:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy_head.next


def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Створення списків для тестування
node1 = ListNode(4)
node2 = ListNode(1)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node4 = ListNode(5)
node5 = ListNode(2)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

# Вивід оригінальних списків
print("Original List 1:")
print_list(node1)
print("Original List 2:")
print_list(node4)

# Тестування реверсування списку
reversed_list = reverse_linked_list(node1)
print("Reversed List 1:")
print_list(reversed_list)

# Тестування сортування вставками (сортуємо реверсований список знову)
sorted_list = insertion_sort_list(reversed_list)
print("Sorted List 1 after insertion sort:")
print_list(sorted_list)

# Тестування сортування вставками для другого списку
sorted_list2 = insertion_sort_list(node4)
print("Sorted List 2 after insertion sort:")
print_list(sorted_list2)

# Тестування об'єднання двох відсортованих списків
merged_list = merge_two_sorted_lists(sorted_list, sorted_list2)
print("Merged Sorted List:")
print_list(merged_list)
