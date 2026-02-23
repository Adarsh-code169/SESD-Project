# Use Case Diagram

```mermaid
useCaseDiagram
    actor Customer
    actor Seller
    actor System

    package "GreenCart System" {
        usecase "Browse Products" as UC1
        usecase "Add to Cart" as UC2
        usecase "Place Order" as UC3
        usecase "Track Order" as UC4
        usecase "Manage Address" as UC5
        usecase "Add Product" as UC6
        usecase "Manage Inventory" as UC7
        usecase "Process Orders" as UC8
        usecase "User Authentication" as UC9
    }

    Customer --> UC1
    Customer --> UC2
    Customer --> UC3
    Customer --> UC4
    Customer --> UC5
    Customer --> UC9

    Seller --> UC6
    Seller --> UC7
    Seller --> UC8
    Seller --> UC9

    UC3 ..> System : triggers
    UC8 ..> System : updates status
```
