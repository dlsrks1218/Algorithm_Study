def blog_printer(name, *blogs, **blog_benefits):
    '''
    name: 블로그 주인 이름
    *blogs: 블로그를 만들 때 설명
    **blog_benefits: 해당 블로그의 수익
    '''

    print(name)
    for post in blogs:
        print(post)
    for blog, benefits in blog_benefits.items():
        print('{0} 수익은 >> {1}'.format(blog, benefits))
    
주인장이름 = '블로그 주인'
블로그1 = '첫번째 블로그지롱'
블로그2 = '성공해서 두번째 블로그도 만들었지롱'
블로그3 = '세번째도 만들었지롱'

# help(func) : func에 대한 정보를 보여줌
help(blog_printer)
blog_printer(주인장이름, 블로그1, 블로그2, 블로그3, 블로그수익1=30, 블로그수익2=40, 블로그수익3=100)