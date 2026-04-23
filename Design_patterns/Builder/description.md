> description by `@flis0`\
> implementation by `@iwonieevo`

### Design pattern: Builder

**Builder** replaces complex constructor arguments or a need for multiple subclasses to achieve a configurable object with optional, multi-choice parameters

Example of multiple sublasses:
```python3
class House:
    def __init__(self):
        print('Build house')

class HouseWithPool(House):
    def __init__(self):
        super().__init__()
        print('Build pool')

class HouseWithGarage(House):
    def __init__(self):
        super().__init__()
        print('Build garage')

class HouseWithPoolAndGarage(HouseWithPool):
    def __init__(self):
        super().__init__()
        print('Build garage')
```


Example of complex constructor arguments:
```python3
class House:
    def __init__(self, hasPool, hasGarage, isGarageBig, hasGarden, [...]):
        print('Build house')
        if hasPool:
            print('Build pool')
        if hasGarage:
            if isGarageBig:
                print('Build big garage')
            else: 
                print('Build small garage')
        if hasGarden:
            print('Build garden')
```

Thats where builder comes in. It's a class like `HouseBuilder` that has separate methods for each option, with it's corresponding options.
Usage example:

```python3
hb = HouseBuilder()
hb.addPool(big=true)
hb.addGarden()
hb.addGarage(spots=2)
```

### Task

Create a builder class for building SQL queries and prompt user for each input. Pass the inputs to the builder class and use it to generate the full SQL query.


*AI translation*

### Wzorzec projektowy: Builder

**Builder** zastępuje złożone argumenty konstruktora lub konieczność tworzenia wielu podklas w celu uzyskania konfigurowalnego obiektu z opcjonalnymi, wielowariantowymi parametrami.

Przykład wielu podklas:

```python3
class House:
    def __init__(self):
        print('Budowanie domu')

class HouseWithPool(House):
    def __init__(self):
        super().__init__()
        print('Budowanie basenu')

class HouseWithGarage(House):
    def __init__(self):
        super().__init__()
        print('Budowanie garażu')

class HouseWithPoolAndGarage(HouseWithPool):
    def __init__(self):
        super().__init__()
        print('Budowanie garażu')
```

Przykład złożonych argumentów konstruktora:

```python3
class House:
    def __init__(self, hasPool, hasGarage, isGarageBig, hasGarden, [...]):
        print('Budowanie domu')
        if hasPool:
            print('Budowanie basenu')
        if hasGarage:
            if isGarageBig:
                print('Budowanie dużego garażu')
            else: 
                print('Budowanie małego garażu')
        if hasGarden:
            print('Budowanie ogrodu')
```

W tym miejscu pojawia się builder. Jest to klasa taka jak `HouseBuilder`, która posiada oddzielne metody dla każdej opcji wraz z odpowiadającymi im parametrami.

Przykład użycia:

```python3
hb = HouseBuilder()
hb.addPool(big=true)
hb.addGarden()
hb.addGarage(spots=2)
```

### Zadanie

Utwórz klasę buildera do budowania zapytań SQL i pobieraj dane wejściowe od użytkownika dla każdego elementu. Przekaż te dane do klasy buildera i użyj jej do wygenerowania pełnego zapytania SQL.
