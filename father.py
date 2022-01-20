local_val = "unicornios mágicos"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        return "hola"
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hi())
print(locals())
print(__name__)
if __name__ == "__main__":
    print("el archivo se está ejecutando directamente")
else:
    print("El archivo se está ejecutando porque es importado por otro archivo. El archivo se llama:", __name__)