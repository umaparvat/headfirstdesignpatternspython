## Flyweight Pattern

What is Flyweight Pattern?
- it's a design pattern techinque used to minimize the memory usage and improve performance by introducing data sharing b/w similar objects.
- it's a shared object which contains state independent and immutable data.
- state independent and mutable object should not be part of Flyweight because data varies b/w objects.

###GOF Terminology

1. The application needs to use large number of objects
2. There are so many objects , it's not possible to store and render them.
3. if the mutable state data is removed ( if required, need to be passed explictly to Flyweight by client code), many group of distinct objects can be replaced by relatively few shared objects.
4. object identity is not important for the application. we cannot rely on object identity because object sharing causes identity comparisions will fail(objects may appear different to the client code, end up having same identity)

  
