class Liquid:
    def __init__(self):
        self.id = "minecraft:water"
        self.hardness = 0
        self.stack = 0
        self.placeability = "all"
        self.light = 0
        self.gravity = False
        self.sound = "water.splash"
        self.blast_resistance = 1
        self.flammable = False
        self.slipperiness = 0.6
        self.solid = false
        self.transparent = true
        self.harvest_tool = "bucket"
        self.harvest_material = "hand"
        self.height = 1
        self.width = 1
        self.length = 1
        self.xp_range = (0,0)
        self.drop = {
            "minecraft:water_bucke": 100
        }
