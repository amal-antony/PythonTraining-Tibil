
class Bird:
   def __init__(self):
      self.hungry = 1

   def eat(self):
     if self.hungry:
        print('Aaaah...')
        self.hungry = 0
     else:
        print('No, thanks!')
print("\nParent class\n")
b = Bird()

b.eat()
b.eat()


class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)

print("\nchild class\n")
sb = SongBird()
sb.sing()
sb.eat()
