# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation helps us group variables and methods together, forming one object. When applying this to the sari-sari store inventory system, a "Product" object can be used to store variables such as: "name", "price", and "supply." The stock or supply can be updated using methods like sell() or add_supply() instead of letting any part of the program directly change it. This allows for lesser errors like the "supply" becoming negative. Basically for me, almost everything is encapsulated; even us humans. We have data such as heart rate, blood pressure, and hormone levels that combine with methods like breathing, moving, speaking and digesting food, to create a fully working human body.

### 2. Abstraction
Abstraction is when you hide unnecessary internal details that the user doesn't need to know and showing only the features that users need to use. The user interacts with simple methods without knowing how they work inside. In a sari-sari store, a cashier can simply call sell() to sell an item. The method handles checking the stock and updating it internally. The cashier doesn't need to know the calculations happening behind the scenes. The user need not to see the store's daily or monthly profit, profit margins, and buying prices. What the user needs to see is only the name of the item, the price of the item, and if the item is still available or not.

### 3. Inheritance
Inheritance is basically when one type of object can get the properties and methods of another type. When this is applied to the sari-sari store, a general Product can have information such as its name, price, and number of stock. And, FoodProduct and DrinkProduct can use those same features. This is important to avoid repeating the same information and makes the inventory easier to organize.

### 4. Polymorphism
Polymorphism is when different types of objects can use the same method but perform it differently. For example, different products can use display_info(), but a food product could display its expiration date while a drink could display its size. This makes the program more flexible because the same action can work differently depending on the product.

## Reflection
Among the four pillars of Object-Oriented Programming, I think encapsulation is the most useful for improving a sari-sari store inventory system. It keeps each product's information and related actions together, making the program easier to organize. It also helps protect the inventory data by ensuring that stock changes happen only through the proper methods. As the store adds more products, this structure makes the system easier to maintain and update.
