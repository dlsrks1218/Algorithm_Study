import collections

Teacher = collections.namedtuple('Teacher', 'name age gender')
Student = collections.namedtuple('Student', 'name age gender')
t = Teacher('아스틴', 30, '남자')
s = Student('저스틴', 19, '남자')

print(t)
print(s)
