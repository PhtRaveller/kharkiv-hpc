#!/usr/bin/python

'''This module demonstrates usage of ``multiprocessing`` Python module, in particular its
``Queue`` and ``Process`` classes.'''

from Queue import Empty, Full
from multiprocessing import Process, Queue, JoinableQueue

class Worker(Process):
    def __init__(self, tasks, results, operation):
        Process.__init__(self)
        self.queue = tasks
        self.results = results
        self.operation = operation
    def run(self):
        '''``run`` method will be called '''
        while True:
            try:
                value = self.queue.get(True, 1)
                print 'PID {0} got {1} from task queue'.format(self.pid, value)
                if value is None:
                    print 'PID {0} Got stop signal.'.format(self.pid)
                    self.queue.task_done()
                    break
                self.queue.task_done()
                self.results.put((self.pid, value, self.operation(value)), True, 1)
            except Empty as e:
                print 'Tasks queue is empty. I\'m leaving.'
                break
            except Full as e:
                print 'Results queue is full. I\'ll try next time.'
                break
            except TypeError as e:
                print 'Operation is not callable: {0}'.format(e)
                break
        return

if __name__ == '__main__':
    import sys
    # Get params
    # Number of worker processes
    if '-n' in sys.argv:
        num_workers = int(sys.argv[sys.argv.index('-n')+1])
    else:
        num_workers = 2
    # Number of tasks
    if '-k' in sys.argv:
        num_tasks = int(sys.argv[sys.argv.index('-k')+1])
    else:
        num_tasks = 100
    # Create JoinableQueue for tasks
    tasks = JoinableQueue()
    # Create Queue for results
    results = Queue()
    operation = lambda x: x**2
    # Create and start worker processes
    workers = [Worker(tasks, results, operation) for i in range(num_workers)]
    for worker in workers:
        worker.start()
    # Put tasks in task queue
    for i in range(num_tasks):
        tasks.put(i)
    # for i in range(num_workers):
    #     tasks.put(None)
    # Wait for tasks
    tasks.join()
    # Get the results
    for i in range(num_tasks):
        result = results.get()
        print 'Process: {0} Task: {1} Result: {2}'.format(*result)
