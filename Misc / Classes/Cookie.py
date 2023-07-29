class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

cookie_one = Cookie('Green')
cookie_two = Cookie('Blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_two.set_color('Yellow')

print('\nCookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())