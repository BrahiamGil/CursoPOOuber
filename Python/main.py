from car import Car
from account import Account
from uberX import UberX
from user import User

if __name__ == "__main__":
    print('Inicializado las info de los carros')
    print('Car')
    print('Uberx')
    uberX = UberX('Klo365', Account('Marco Sanchez', 'SGHJ1236',
    "marco@platzi.com", "7856"), "Toyota", "Corolla")

    print(vars(uberX))
    print(vars(uberX.driver))

    print('User')
    user = User('mariana valle', 'SDFG12F', 'mariana@platzi.com',"7856")
    print(vars(user))