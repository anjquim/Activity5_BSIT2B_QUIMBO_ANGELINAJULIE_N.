from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

def stack_menu(stack):
    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("0. Back")

        choice = input("Choice: ")

        try:
            if choice == "1":
                item = input("Enter item: ")
                stack.push(item)

            elif choice == "2":
                print("Removed:", stack.pop())

            elif choice == "3":
                print("Top:", stack.peek())

            elif choice == "4":
                print(stack)

            elif choice == "0":
                break

            print("Current State:", stack)

        except Exception as e:
            print("Error:", e)


def queue_menu(queue):
    while True:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. Peek Front")
        print("4. Display")
        print("0. Back")

        choice = input("Choice: ")

        try:
            if choice == "1":
                item = input("Enter item: ")
                queue.enqueue(item)

            elif choice == "2":
                print("Removed:", queue.dequeue())

            elif choice == "3":
                print("Front:", queue.peek_front())

            elif choice == "4":
                print(queue)

            elif choice == "0":
                break

            print("Current State:", queue)

        except Exception as e:
            print("Error:", e)


def main():
    while True:
        print("\n=== DATA STRUCTURES MENU ===")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Array Queue")
        print("4. Linked Queue")
        print("0. Exit")

        choice = input("Select: ")

        if choice == "1":
            cap = int(input("Capacity: "))
            stack_menu(ArrayStack(cap))

        elif choice == "2":
            stack_menu(LinkedStack())

        elif choice == "3":
            cap = int(input("Capacity: "))
            queue_menu(ArrayQueue(cap))

        elif choice == "4":
            queue_menu(LinkedQueue())

        elif choice == "0":
            break


if __name__ == "__main__":
    main()