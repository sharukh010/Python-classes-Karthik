Product inventory management system (PIMS): 
1. add products
2. check product stock 
3. refill product stock 
4. report 
5. display single product 
6. display all the available products 

1. Add product : 
- maintain a global list called "products" which holds multiple product dictionaries 
- product schema:
id : int (automatically generated)
name: str 
supplier: str 
quantity: int 
price_per_unit: float 
stock_capacity: int 
total_price: float (automatically calculated )
is_available: bool ( automatically generated based on quantity ) -> True if there is enough stock , False if the stock is 0 

Enter your choice: 1 
Product Details: 
Name: <input> 
Supplier: <input> 
Quantity: <input> 
Price Per Unit: <input>
Stock Capacity: <input> 

Product with ID <id> is added to inventory  
