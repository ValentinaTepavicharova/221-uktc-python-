import random
class221=[22101,22102,22103,22104,22105,22106,22107,22108,22109,22110,22111,22112,22113,22115,22115,22115,22116,22101,22101,22101,22101,22101,22116,22117,22118,22119,22120,22121,22122,22123,22124,22125,22126,22127,22128,22129]
already_selected=[] 
while len(already_selected) != len(class221):
    a=random.choice(class221)
    if a in already_selected:
        continue
    print(a)
    already_selected.append(a)

    input("Tap Enter to continue")
