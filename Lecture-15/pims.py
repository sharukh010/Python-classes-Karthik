from tabulate import tabulate 
# constants 
APP_NAME="Product Inventory Management System (P.I.M.S)"
OPTIONS="""Options: 
1. add products
2. check product stock 
3. refill product stock 
4. sell 
5. display single product 
6. display all the available products 
7. Exit"""
ADDING_PRODUCT =1
CHECKING_PRODUCT=2
REFILL_PRODUCT_STOCK=3
SELL = 4
DISPLAY_SINGLE_PRODUCT=5
DISPLAY_ALL_PRODUCTS=6
EXIT=7
#global 
products = [{
    "id": 1,
    "name": "apple",
    "supplier": "farmer",
    "quantity": 10,
    "price_per_unit": 2,
    "stock_capacity": 50,
    "available": True
}] # store where we store all the product details 
pid = 1 
# functions
def add_product(product: dict[str]): 
    products.append(product)

def get_product(id:int): 
    target = None 
    for product in products: 
        if product["id"] == id: 
            target = product 
            break 
    return target 

def display_products(): 
    items = [] 
    for product in products: 
        row = [product["id"],product["name"],product["available"]]
        items.append(row)
    table = tabulate(items,headers=["ID","Name","Available"],tablefmt="grid")
    print(table)

def perform(choice): 
    global pid 
    match choice: 
        case 1: 
            print("Adding Product: ")
            name = input("Name: ")
            supplier = input("Supplier: ")
            quantity = int(input("Quantity: "))
            price_per_unit = float(input("Price Per Unit: "))
            stock_capacity = int(input("Stock Capacity: "))
            is_availabe = True if quantity > 0 else False 
            pid += 1 
            product = {
                "id": pid,
                "name": name,
                "supplier": supplier,
                "quantity": quantity,
                "price_per_unit": price_per_unit,
                "stock_capacity": stock_capacity,
                "available": is_availabe
            }
            add_product(product)
            print(f"Product with ID {pid} is added")
        case 2: # if choice == 2 
            print("Checking Product Stock: ")
            target_id = int(input("ID: "))
            product = get_product(target_id)
            if product == None: 
                print(f"Product with ID {target_id} is not found")
            else: 
                print(f"Stock: {product["quantity"]}/{product["stock_capacity"]}")

        case 3: 
            print("Refilling Product Stock: ")
            target_id = int(input("ID: "))
            product = get_product(target_id)
            if product == None: 
                print(f"Product with ID {target_id} is not found")
            else: 
                product["quantity"] = product["stock_capacity"]
                product["available"] = True 
                print("Product is Restocked")
        case 4: 
            print("Selling Product: ")
            target_id = int(input("ID: "))
            product = get_product(target_id)
            if product == None: 
                print(f"Product with ID {target_id} is not found")
            else: 
                quantity = int(input("Quantity: "))
                if product["quantity"] < quantity: 
                    print(f"Try Again.Exceeding stock quantity")
                else: 
                    product["quantity"] -= quantity 
                    if product["quantity"] == 0: 
                        product["available"] = False 
                    print(f"Cost: {product["price_per_unit"]*quantity}")
                    print("Product Sold Successfully")
        case 5: 
            print("Displaying Single Product: ")
            target_id = int(input("ID: "))
            product = get_product(target_id)
            if product == None: 
                print(f"Product with ID {target_id} is not found")
            else: 
                table = tabulate([product],headers="keys",tablefmt="grid")
                print(table)
        case 6: 
            print("Displaying all the Products: ")
            display_products()
        case 7: 
            print("Exiting..") 
        case _ : 
            print("Invalid choice, Try again.")
while True: 
    print(APP_NAME)
    print(OPTIONS)
    choice = int(input("Enter your choice: "))
    perform(choice)
    response = input("Do you want to coninue(y/n)? ")
    if response == "y": 
        print("#"*15)
        continue 
    else: 
        perform(EXIT)
        break 
    
    
