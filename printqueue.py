from linked_queue import LinkedQueue

class PrintJob:
    def __init__(self, job_id, pages):
        self.job_id = job_id
        self.pages = pages

    def __str__(self):
        return f"Job {self.job_id} ({self.pages} pages)"


queue = LinkedQueue()

queue.enqueue(PrintJob("A101", 10))
queue.enqueue(PrintJob("A102", 5))
queue.enqueue(PrintJob("A103", 20))

order = 1

while not queue.is_empty():
    job = queue.dequeue()
    print(f"#{order}: Printing {job}")
    order += 1
