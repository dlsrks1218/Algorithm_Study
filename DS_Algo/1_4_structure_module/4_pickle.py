# pickle 모듈을 이용해 파이썬 객체를 문자열 표현으로 서로 변환 가능
import pickle

x = {}
x['name'] = '아스틴'
x['age'] = '23'
# 피클링 : 파이썬 객체 > 문자열 표현으로 변환
with open('name.pkl', 'wb') as f:
    pickle.dump(x, f)
# 언피클링 : 문자열 표현을 파이썬 객체로 변환
with open('name.pkl', 'rb') as f:
    name = pickle.load(f)

print(name)