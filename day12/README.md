## Namespaces: Local Vs Global Scope

## Local and Global variables
### 1. Local Scope
Local variables are variables defined inside a function. This means that they are only accessible within the function. These variables have `local scope`.

Local scope variables are only valid within the function structure that they are defined in. Trying to access them outside of their function raises a `NameError`

### 2. Global Scope
Global variables are variables defined at the outer leve(outside functins). These can be accessed within functions, and anywhere in the source file. These variables have `global scope`