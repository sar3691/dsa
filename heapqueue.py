import heapq

pq = []

while True:
    print("\n1. Add Task")
    print("2. Remove Highest Priority Task")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        priority = int(input("Enter priority: "))
        heapq.heappush(pq, (-priority, task))
        print("Task added")

    elif choice == '2':
        if pq:
            priority, task = heapq.heappop(pq)
            print("Removed task:", task)
        else:
            print("Priority Queue is empty")

    elif choice == '3':
        break

    else:
        print("Invalid choice")
