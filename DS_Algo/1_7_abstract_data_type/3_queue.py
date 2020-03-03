'''
insert() 메서드가 사용되어 모든 요소가 메모리에서 이동될 수 있으므로 비효율적, O(n)
'''
class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print('Queue is empty')

    def size(self):
        return len(self.items)

    def front(self):
        if self.items:
            return self.items[-1]

    def __repr__(self):
        return repr(self.items)


if __name__ == '__main__':
    queue = Queue()

    print('큐가 비었나요? {0}'.format(queue.isEmpty()))
    print('큐에 숫자 0~9를 추가합니다')
    for i in range(10):
        queue.enqueue(i)
    print('큐 크기 : {0}'.format(queue.size()))
    print('front : {0}'.format(queue.front()))
    print('dequeue : {0}'.format(queue.dequeue()))
    print('front : {0}'.format(queue.front()))
    print('큐가 비었나요? {0}'.format(queue.isEmpty()))
    print(queue.__repr__())