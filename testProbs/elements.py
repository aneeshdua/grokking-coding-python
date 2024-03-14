def findElements(input, periodicElements,index):
    length = len(input)
    if index >= length:
        return []
    res = []
    symbol1 = input[index].lower()
    symbol2 = input[index:index+2].lower() if index !=length-1 else ""
    if symbol1 in periodic_elements:
        if index == length-1:
            res.append(periodic_elements[symbol1])
            return res
        remaining = findElements(input,periodicElements,index+1)
        if remaining!=[]:
            res.append(periodic_elements[symbol1])
            res = res + remaining
        else:
            res=[]
    if symbol2 in periodic_elements:
        if index == length-2:
            res.append(periodic_elements[symbol2])
            return res
        remaining = findElements(input,periodicElements,index+2)
        if remaining!=[]:
            res.append(periodic_elements[symbol2])
            res = res + remaining
        else:
            res=[]
    return res





compound = ["K","HeBe","BaNiNaS","COFFeINe","FUN","SiGeNeSIS","ArTiClEs","BeEr","CaRe","LaDy","AlGeBrA"]
periodic_elements = periodic_elements_lowercase = {
    "h": "hydrogen",
    "he": "helium",
    "li": "lithium",
    "be": "beryllium",
    "b": "boron",
    "c": "carbon",
    "n": "nitrogen",
    "o": "oxygen",
    "f": "fluorine",
    "ne": "neon",
    "na": "sodium",
    "mg": "magnesium",
    "al": "aluminum",
    "si": "silicon",
    "p": "phosphorus",
    "s": "sulfur",
    "cl": "chlorine",
    "ar": "argon",
    "k": "potassium",
    "ca": "calcium",
    "sc": "scandium",
    "ti": "titanium",
    "v": "vanadium",
    "cr": "chromium",
    "mn": "manganese",
    "fe": "iron",
    "co": "cobalt",
    "ni": "nickel",
    "cu": "copper",
    "zn": "zinc",
    "ga": "gallium",
    "ge": "germanium",
    "as": "arsenic",
    "se": "selenium",
    "br": "bromine",
    "kr": "krypton",
    "rb": "rubidium",
    "sr": "strontium",
    "y": "yttrium",
    "zr": "zirconium",
    "nb": "niobium",
    "mo": "molybdenum",
    "tc": "technetium",
    "ru": "ruthenium",
    "rh": "rhodium",
    "pd": "palladium",
    "ag": "silver",
    "cd": "cadmium",
    "in": "indium",
    "sn": "tin",
    "sb": "antimony",
    "te": "tellurium",
    "i": "iodine",
    "xe": "xenon",
    "cs": "cesium",
    "ba": "barium",
    "la": "lanthanum",
    "ce": "cerium",
    "pr": "praseodymium",
    "nd": "neodymium",
    "pm": "promethium",
    "sm": "samarium",
    "eu": "europium",
    "gd": "gadolinium",
    "tb": "terbium",
    "dy": "dysprosium",
    "ho": "holmium",
    "er": "erbium",
    "tm": "thulium",
    "yb": "ytterbium",
    "lu": "lutetium",
    "hf": "hafnium",
    "ta": "tantalum",
    "w": "tungsten",
    "re": "rhenium",
    "os": "osmium",
    "ir": "iridium",
    "pt": "platinum",
    "au": "gold",
    "hg": "mercury",
    "tl": "thallium",
    "pb": "lead",
    "bi": "bismuth",
    "po": "polonium",
    "at": "astatine",
    "rn": "radon",
    "fr": "francium",
    "ra": "radium",
    "ac": "actinium",
    "th": "thorium",
    "pa": "protactinium",
    "u": "uranium",
    "np": "neptunium",
    "pu": "plutonium",
    "am": "americium",
    "cm": "curium",
    "bk": "berkelium",
    "cf": "californium",
    "es": "einsteinium",
    "fm": "fermium",
    "md": "mendelevium",
    "no": "nobelium",
    "lr": "lawrencium",
    "rf": "rutherfordium",
    "db": "dubnium",
    "sg": "seaborgium",
    "bh": "bohrium",
    "hs": "hassium",
    "mt": "meitnerium",
    "ds": "darmstadtium",
    "rg": "roentgenium",
    "cn": "copernicium",
    "nh": "nihonium",
    "fl": "flerovium",
    "mc": "moscovium",
    "lv": "livermorium",
    "ts": "tennessine",
    "og": "oganesson"
}
#len(compound)
for i in range(len(compound)):
    print("PRocessing Item: ", compound[i], end=" ")
    print(findElements(compound[i],periodic_elements,0))