STEP = 0.1

STARTBUTTON = (1415, 885)

BACKBUTTON = (1709, 981)

INVENTORY = (1729, 515), (1781, 517), (1835, 515), (1729, 567), (1781, 569), (1837, 569), (1731, 621), (1783, 623), (1835, 621), (1835, 621)

ENRAGESLOT = (74, 81)

GEMKEYS = {}
GEMKEYS['purple'] = 'num1'
GEMKEYS['green'] = 'num2'
GEMKEYS['blue'] = 'num3'
GEMKEYS['yellow'] = 'num4'
GEMKEYS['orange'] = 'num5'
GEMKEYS['red'] = 'num6'

TRAITS = {'Overcrowd': {'field': 'V1 Journey', 'effect': 'Increases the number of monsters by (10% * n) in each wave.', 'pos': (0,0)},
          'Haste': {'field': 'S2 Endurance', 'effect': 'Wave stones move (8% * n) faster.', 'pos': (0,0)},
          'Adaptive Carapace':  {'field': 'R3 Endurance', 'effect': 'Monsters gets (0.5% * n) damage reduction per hit, capped at (5% * n).', 'pos': (0,0)},
          'Swarmling Parasites':  {'field': 'T4 Endurance', 'effect': 'Killed monsters spawns 2 spawnlings, with each spawnling having (30% * n) of monsters max HP.', 'pos': (0,0)},
          'Awakening': {'field': 'I2 Journey', 'effect': 'Monsters have (0.7% * n) wave HP increment', 'pos': (0,0)},
          'Dark Masonry':  {'field': 'K1 Endurance', 'effect': 'Spawns (1+n) beacons every 10 waves, while also makes all hostile structures (beacons, nests, barricades, etc.) having (200% * n) more HP.', 'pos': (0,0)},
          'Swarmling Domination':  {'field': 'Y1 Endurance', 'effect': 'Converts (3*n)% of reaver waves into a wave of swarmlings, and gives swarmlings +(4% * n) speed and -(7% * n) debuff duration reduction (such as slow, bleeding).', 'pos': (0,0)},
          'Giants Domination':  {'field': 'P4 Endurance', 'effect': 'Converts (3*n)% of reaver waves into a wave of giants, and gives giants +(40% * n) armor and +(50% * n) HP.', 'pos': (0,0)},
          'Thick Air':  {'field': 'H3 Journey', 'effect': 'Enemies take maximum (1/(2*n)) max HP of damage.', 'pos': (0,0)},
          'Corrupted Banishment':  {'field': 'O2 Endurance', 'effect': 'Banished enemies gets (30% * n) increased HP, +(30 * n^2) armor, and n shields.', 'pos': (0,0)},
          'Vital Link':  {'field': 'J4 Journey', 'effect': 'Enemies enter battlefield with (10% * n) increased HP based on enemies waiting to enter the battlefield (final value is 10% * n * waiting).', 'pos': (0,0)},
          'Hatred': {'field': 'C3 Endurance', 'effect': 'Increases enemy HP by (100% * 1.5 ^ n)', 'pos': (0,0)},
          'Strength in Numbers': {'field': 'F2 Journey', 'effect': 'Enemies have indestructible armor based on the amount of enemies in the battlefield (+ 4 * n * monsters on field).', 'pos': (0,0)},
          'Ritual' : {'field': 'D1 Endurance', 'effect': 'n+1 flying ones will appear during battle.', 'pos': (0,0)},
          'Insulation' : {'field': 'Z1 Journey', 'effect': 'Enemies spawn with n shields.', 'pos': (0,0)}}
