# 구독자
class Subscriber(object):
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print('{0}, {1}'.format(self.name, message))

# 발행자
class Publisher(object):
    def __init__(self):
        self.subscibers = set()

    def register(self, who):
        self.subscibers.add(who)

    # discard() > set의 메서드로, 차집합의 기능을 수행
    def unregister(self, who):
        self.subscibers.discard(who)
    
    # disparch > 전파하다, 보내다
    def dispatch(self, message):
        for subsciber in self.subscibers:
            subsciber.update(message)


if __name__ == '__main__':
    pub = Publisher()

    astin = Subscriber('아스틴')
    james = Subscriber('제임스')
    jeff = Subscriber('제프')

    astin.update('나는 배고파')
    james.update('나는 배불러')
    jeff.update('나는 모르겠어')
    print()
    
    pub.register(astin)
    pub.register(james)
    pub.register(jeff)

    pub.dispatch('점심시간입니다')
    pub.unregister(jeff)
    pub.dispatch('퇴근시간입니다')