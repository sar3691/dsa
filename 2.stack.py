class Stack:
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1

    def push(self, x):
        if self.isFull():
            print("Stack Overflow!! Calling exit()…")
            exit(1)

        print(f"Inserting {x} into the stack…")
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow!! Calling exit()…")
            exit(1)

        print(f"Removing {self.peek()} from the stack")
        top = self.arr[self.top]
        self.top -= 1
        return top

    def peek(self):
        if self.isEmpty():
            exit(1)
        return self.arr[self.top]

    def size(self):
        return self.top + 1

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity


def main_stack():
    stack_size = int(input("Enter the size of the stack: "))
    stack = Stack(stack_size)

    while True:
        print("\nMenu:")
        print("1. Push element to the stack")
        print("2. Pop element from the stack")
        print("3. Peek at the top element")
        print("4. Check if the stack is empty")
        print("5. Check if the stack is full")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = int(input("Enter the element to push: "))
            stack.push(element)
        elif choice == 2:
            popped_element = stack.pop()
            print(f"Popped element: {popped_element}")
        elif choice == 3:
            print("Top element:", stack.peek())
        elif choice == 4:
            print("Is the stack empty?", stack.isEmpty())
        elif choice == 5:
            print("Is the stack full?", stack.isFull())
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == '__main__':
    main_stack()
