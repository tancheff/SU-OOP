from project.auction_house_manager_app import AuctionHouseManagerApp

# Create an instance of AuctionHouseManagerApp
manager = AuctionHouseManagerApp()
# Register artifacts
print(manager.register_artifact("RenaissanceArtifact", "Kohinoor", 5000.0, 10))
print(manager.register_artifact("RenaissanceArtifact", "Zelda", 5000.0, 10))
print(manager.register_artifact("RenaissanceArtifact", "Mona Lisa", 10000.0, 100))
print(manager.register_artifact("ContemporaryArtifact", "The Scream", 2000.0, 1000))
print(manager.register_artifact("ContemporaryArtifact", "Untitled", 32000.0, 90))
print()
# Register collectors
print(manager.register_collector("PrivateCollector", "Josh Smith"))
print(manager.register_collector("Museum", "Louvre"))
print(manager.register_collector("Museum", "Hermitage"))
print()
# Perform purchases
print(manager.perform_purchase("Josh Smith", "Mona Lisa"))
print(manager.perform_purchase("Louvre", "Kohinoor"))
print(manager.perform_purchase("Josh Smith", "Zelda"))
print(manager.perform_purchase("Josh Smith", "The Scream"))
print(manager.perform_purchase("Josh Smith", "Untitled"))
print()
# Remove artifact
print(manager.remove_artifact("The Scream"))
print(manager.remove_artifact("Nonexistent"))
print()
# Start fund-raising campaigns
print(manager.fundraising_campaigns(10000.0))
print()
# Get auction report
print(manager.get_auction_report())
print()

# Remove artifact
print(manager.remove_artifact("Untitled"))


"""
    ------------- EXPECTED OUTPUT -------------
    
Kohinoor is successfully added to the auction as RenaissanceArtifact.
Zelda is successfully added to the auction as RenaissanceArtifact.
Mona Lisa is successfully added to the auction as RenaissanceArtifact.
The Scream is successfully added to the auction as ContemporaryArtifact.
Untitled is successfully added to the auction as ContemporaryArtifact.

Josh Smith is successfully registered as a PrivateCollector.
Louvre is successfully registered as a Museum.
Hermitage is successfully registered as a Museum.

Josh Smith purchased Mona Lisa for a price of 10000.00.
Louvre purchased Kohinoor for a price of 5000.00.
Josh Smith purchased Zelda for a price of 5000.00.
Josh Smith purchased The Scream for a price of 2000.00.
Purchase is impossible.

No such artifact.
No such artifact.

2 collector/s increased their available money.

**Auction statistics**
Total number of sold artifacts: 4
Available artifacts for sale: 1
***
Collector name: Josh Smith; Money available: 13000.00; Space available: 1890; Artifacts: Zelda, The Scream, Mona Lisa
Collector name: Louvre; Money available: 11000.00; Space available: 1990; Artifacts: Kohinoor
Collector name: Hermitage; Money available: 15000.00; Space available: 2000; Artifacts: none

Removed Contemporary Artifact: Untitled; Price: 32000.00; Required space: 90
"""