class Example:
    def __init__(self):
        self.id = "minecraft:example" # (https://www.digminecraft.com/lists/item_id_list_pe.php)
        self.hardness = 0.5  # Hardness of the block (how long it takes to mine) (https://minecraft.fandom.com/wiki/Module:Hardness_values)
        self.stack = 64  # Maximum stack size for the block (Values from 1-64)
        self.placeability = ""  # Where the block can be placed ("all" means it can be placed anywhere) (wall, up, floor, water, all)
        self.light = 0  # Light level emitted by the block (0 means it doesn't emit light) (https://minecraft.fandom.com/wiki/Light)
        self.gravity = False  # Whether the block is affected by gravity (Boolean)
        self.sound = ""  # Sound produced when the block is placed or broken (https://minecraft.fandom.com/wiki/Sounds.json/Bedrock_Edition_values)
        self.blast_resistance = 0  # Resistance of the block to explosions (https://minecraft.fandom.com/wiki/Explosion)
        self.flammable = False  # Indicates if the block can catch fire (Boolean)
        self.slipperiness = 0.6  # Slipperiness of the block (affects movement speed) (https://www.mcpk.wiki/wiki/Slipperiness)
        self.solid = True  # Whether the block is solid and can be stood upon (Boolean)
        self.transparent = False  # Specifies if the block is transparent (Boolean)
        self.harvest_tool = ""  # Example: None, Shovel, Pickaxe, Axe, Sword
        self.harvest_material = ""  # Needed material to drop item. Example: Hand, Wood, Stone, Iron, Diamond, Netherite
        self.height = 1 # Example: Mostly 1, For Doors 2 and Slabs 0.5
        self.width = 1 # Example: Mostly 1
        self.length = 1 # Example: Mostly 1, For Beds 2
        self.xp_range = (0, 0) # Is a range. https://minecraft.fandom.com/wiki/Experience
        
        self.drop = { # Numbers are %
            "minecraft:example": 20,
            "minecraft:example2": 10
        }