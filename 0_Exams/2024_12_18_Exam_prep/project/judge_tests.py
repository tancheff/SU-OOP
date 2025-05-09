from project.flower_shop_manager import FlowerShopManager

# Create an instance of FlowerShopManager
manager = FlowerShopManager()

# Add plants
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Tulip", 12.00, 150, "Spring"))
print(manager.add_plant("Flower", "Tulip", 12.00, 150, "Spring"))
print(manager.add_plant("Flower", "Lily", 20.00, 180, "Summer"))
print(manager.add_plant("LeafPlant", "Cactus", 8.00, 50, "M"))
print(manager.add_plant("LeafPlant", "Cactus", 8.00, 50, "M"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Snake Plant", 12.00, 200, "L"))
print(manager.add_plant("LeafPlant", "Snake Plant", 12.00, 200, "L"))
print()

# Add clients
print(manager.add_client("RegularClient", "Alice Johnson", "1234567890"))
print(manager.add_client("RegularClient", "Bob Smith", "0987654321"))
print(manager.add_client("BusinessClient", "Greenhouse Inc.", "5647382910"))
print(manager.add_client("BusinessClient", "CoolGarden Plc.", "9647382910"))
print(manager.add_client("RegularClient", "Peter Johnson", "382910"))
print()

# Perform sales
print(manager.sell_plants("1234567890", "Rose", 3))
print(manager.sell_plants("0987654321", "Tulip", 2))
print(manager.sell_plants("5647382910", "Cactus", 1))
print()

# Get shop report
print(manager.shop_report())
print()

# Perform sales
print(manager.sell_plants("1234567890", "Lily", 2))
print(manager.sell_plants("0987654321", "Fern", 1))
print(manager.sell_plants("5647382910", "Snake Plant", 2))
print()

# Remove a plant
print(manager.remove_plant("Nonexistent"))
print(manager.remove_plant("Cactus"))
print()

# Get shop report
print(manager.shop_report())
print()

# Remove clients who have no orders
print(manager.remove_clients())
print(manager.remove_clients())


"""
------------- Output -------------

Rose is added to the shop as Flower.
Rose is added to the shop as Flower.
Rose is added to the shop as Flower.
Rose is added to the shop as Flower.
Tulip is added to the shop as Flower.
Tulip is added to the shop as Flower.
Lily is added to the shop as Flower.
Cactus is added to the shop as LeafPlant.
Cactus is added to the shop as LeafPlant.
Fern is added to the shop as LeafPlant.
Fern is added to the shop as LeafPlant.
Fern is added to the shop as LeafPlant.
Snake Plant is added to the shop as LeafPlant.
Snake Plant is added to the shop as LeafPlant.

Alice Johnson is successfully added as a RegularClient.
Bob Smith is successfully added as a RegularClient.
Greenhouse Inc. is successfully added as a BusinessClient.
CoolGarden Plc. is successfully added as a BusinessClient.
Peter Johnson is successfully added as a RegularClient.

3pcs. of Rose plant sold for 46.50
2pcs. of Tulip plant sold for 24.00
1pcs. of Cactus plant sold for 8.00

~Flower Shop Report~
Income: 78.50
Count of orders: 3
~~Unsold plants: 8~~
Fern: 3
Snake Plant: 2
Cactus: 1
Lily: 1
Rose: 1
~~Clients number: 5~~
Client: Bob Smith, Phone number: 0987654321, Orders count: 1, Discount: 5%
Client: Alice Johnson, Phone number: 1234567890, Orders count: 1, Discount: 5%
Client: Greenhouse Inc., Phone number: 5647382910, Orders count: 1, Discount: 0%
Client: Peter Johnson, Phone number: 382910, Orders count: 0, Discount: 0%
Client: CoolGarden Plc., Phone number: 9647382910, Orders count: 0, Discount: 0%

Not enough plant quantity.
1pcs. of Fern plant sold for 6.17
2pcs. of Snake Plant plant sold for 24.00

No such plant name.
Removed Leaf Plant: Cactus, Price: 8.00, Watering: 50ml, Size: M

~Flower Shop Report~
Income: 108.67
Count of orders: 5
~~Unsold plants: 4~~
Fern: 2
Lily: 1
Rose: 1
~~Clients number: 5~~
Client: Bob Smith, Phone number: 0987654321, Orders count: 2, Discount: 5%
Client: Greenhouse Inc., Phone number: 5647382910, Orders count: 2, Discount: 10%
Client: Alice Johnson, Phone number: 1234567890, Orders count: 1, Discount: 5%
Client: Peter Johnson, Phone number: 382910, Orders count: 0, Discount: 0%
Client: CoolGarden Plc., Phone number: 9647382910, Orders count: 0, Discount: 0%

2 client/s removed.
0 client/s removed.

"""