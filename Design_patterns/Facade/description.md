> description by `@iwonieevo`
> implementation by `@flis0`

# Fasada

## Przegląd

Wzorzec Fasady (Facade Pattern) to strukturalny wzorzec projektowy, który zapewnia uproszczony interfejs do złożonego podsystemu. Oddziela klientów od wewnętrznych szczegółów implementacji podsystemu, dzięki czemu system jest łatwiejszy w użyciu i zrozumieniu.

## Rozwiązanie

-   Stosuj wzorzec Fasady podczas pracy ze złożonymi podsystemami, aby zapewnić prosty, ujednolicony interfejs dla klientów.
-   Używaj go, aby zmniejszyć liczbę interakcji między kodem klienta a komponentami podsystemu.
-   Zastosuj ten wzorzec, aby ograniczyć bezpośrednie zależności między klientami a wieloma klasami podsystemu.

## Przyczyny

(+) Redukuje złożoność poprzez dostarczenie prostszego interfejsu do skomplikowanych systemów.  
(+) Zwiększa czytelność i użyteczność kodu poprzez ukrycie złożonej logiki podsystemu.  
(+) Wspiera separację odpowiedzialności, co poprawia utrzymanie kodu.  
(+) Ogranicza bezpośrednie powiązania między klientami a komponentami podsystemu.

(-) Może stać się zbyt rozbudowany lub złożony, jeśli przejmie zbyt wiele odpowiedzialności (ryzyko „god object”).  
(-) Zmiany w podsystemie mogą wymagać aktualizacji fasady, jeśli wpływają na jej interfejs.  
(-) Może ukrywać zaawansowaną funkcjonalność podsystemu, co wymaga bezpośredniego dostępu w celu uzyskania pełnej kontroli.  
(-) Wprowadza dodatkową warstwę abstrakcji, co może powodować niewielki narzut.  


# Facade

## Overview

The Facade Pattern is a structural design pattern that provides a simplified interface to a complex subsystem. It decouples clients from the subsystem’s internal implementation details, making the system easier to use and understand.

## Solution

-   Implement the Facade Pattern when working with complex subsystems to provide a simple, unified interface for clients.
-   Use it to reduce the number of interactions required between client code and subsystem components.
-   Apply the pattern to minimize direct dependencies between clients and multiple subsystem classes.

## Causes

(+) Reduces complexity by providing a simpler interface to complex systems.  
(+) Increases code readability and usability by abstracting intricate subsystem logic.  
(+) Promotes separation of concerns, improving maintainability.  
(+) Reduces direct coupling between clients and subsystem components.

(-) Can become overly large or complex if it tries to handle too many responsibilities (god object risk).  
(-) Changes to the subsystem may require updates to the facade if they affect its exposed interface.  
(-) May obscure advanced subsystem functionality, requiring direct access when more control is needed.  
(-) Introduces an additional abstraction layer, which can add slight overhead.

# Przykład kodu/Code example
*Źródło/Source: https://www.geeksforgeeks.org/system-design/facade-design-pattern-introduction/*
```py
from abc import ABC, abstractmethod

class Hotel(ABC):
    @abstractmethod
    def get_menus(self):
        pass
```

```py
from structural.facade import Hotel, Menus, NonVegMenu

class NonVegRestaurant(Hotel):

    def get_menus(self):
        nv = NonVegMenu()
        return nv
```

```py
class VegRestaurant:
    def getMenus(self):
        v = VegMenu()
        return v
```

```py
class VegNonBothRestaurant:
    def getMenus(self):
        b = Both()
        return b
```

```py
"""package whatever //do not write package name here """ 

from abc import ABC, abstractmethod

class HotelKeeper(ABC):

    @abstractmethod
    def getVegMenu(self):
        pass

    @abstractmethod
    def getNonVegMenu(self):
        pass

    @abstractmethod
    def getVegNonMenu(self):
        pass
```

```py
from abc import ABC, abstractmethod

class HotelKeeper(ABC):
    @abstractmethod
    def getVegMenu(self):
        pass

    @abstractmethod
    def getNonVegMenu(self):
        pass

    @abstractmethod
    def getVegNonMenu(self):
        pass

class VegRestaurant:
    def getMenus(self):
        return VegMenu()

class NonVegRestaurant:
    def getMenus(self):
        return NonVegMenu()

class VegNonBothRestaurant:
    def getMenus(self):
        return Both()

class HotelKeeperImplementation(HotelKeeper):

    def getVegMenu(self):
        v = VegRestaurant()
        vegMenu = v.getMenus()
        return vegMenu

    def getNonVegMenu(self):
        v = NonVegRestaurant()
        nonVegMenu = v.getMenus()
        return nonVegMenu

    def getVegNonMenu(self):
        v = VegNonBothRestaurant()
        bothMenu = v.getMenus()
        return bothMenu

class VegMenu:
    pass

class NonVegMenu:
    pass

class Both:
    pass
```

```py
from structural.facade import HotelKeeperImplementation, VegMenu, NonVegMenu, BothMenu

def main():
    keeper = HotelKeeperImplementation()
    v = keeper.get_veg_menu()
    nv = keeper.get_non_veg_menu()
    both = keeper.get_veg_non_menu()

if __name__ == "__main__":
    main()
```
