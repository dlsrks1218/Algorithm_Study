class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'


def build_menu(names, values, calories):
    '''names, values, calories는 같은 길이를 가지며 
        names는 문자열로 된 이름들의 리스트이며
        values, calories는 숫자들의 리스트이고
        Food들의 리스트를 반환함'''
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    
    return menu


def greedy(items, max_cost, key_function):
    '''items를 리스트로, max_cost는 0이상이며
        key_function은 items의 요소들을 숫자들과 매핑시킨다'''
    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_cost = 0.0, 0.0
    for i in range(len(items_copy)):
        if (total_cost + items_copy[i].getCost()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].getCost()
            total_value += items_copy[i].getValue()

    return (result, total_value)


def test_greedy(items, constraint, key_function):
    taken, val = greedy(items, constraint, key_function)
    print('Total value of items take =', val)
    for item in taken:
        print('    ', item)


def test_greedys(foods, max_units):
    print('User greedy by value to allocate', max_units, 'calories')
    test_greedy(foods, max_units, Food.getValue)

    print('\nUser greedy by cost to allocate', max_units, 'calories')
    test_greedy(foods, max_units, lambda x: 1/Food.getCost(x))

    print('\nUse greedy by density to allocate', max_units, 'calories')
    test_greedy(foods, max_units, Food.density)


if __name__ == '__main__':
    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'coke', 'apple', 'donut', 'cake']
    values = [89,90,95,100,90,79,50,10]
    calories = [123,154,258,354,365,150,95,195]
    foods = build_menu(names, values, calories)

    test_greedys(foods, 800)