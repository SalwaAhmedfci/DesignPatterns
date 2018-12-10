from observer import subscriber,Publisher


pub = Publisher()

bob = subscriber("Bob")
alice = subscriber('Alice')
john = subscriber('John')

pub. register(bob) #invoke the registeration
pub.register(alice)
pub.register(john)

pub.dispatch("It's lunch time")
pub.unregister(john)
pub.dispatch("Time for dinner")