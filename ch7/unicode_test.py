def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value) # name() 인자로 유니코드 문자를 취하고, 대문자 이름을 반환
    value2 = unicodedata.lookup(name) # lookup() 대소문자를 구분하지 않는 인자를 취하고, 유니코드 문자를 반환
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

if __name__ == "__main__":
    unicode_test('A')
    unicode_test('$')
    unicode_test('\u00a2')
    unicode_test('\u20ac')
    unicode_test('\u20ac')