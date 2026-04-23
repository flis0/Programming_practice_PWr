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