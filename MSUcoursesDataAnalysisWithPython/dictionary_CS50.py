# distances={
#     "Voyager 1": 163,
#     "Voyager 2" : 136,
#     "Pioner 10" : 80,
#     "New Horizons": 58
# }
#
# def main():
#     for distance in distances.values():
#         print(f"{distance} AU is {convert(distance)} m")
#
# def convert(au):
#     return au*149597870700
#
# main()


def main():
    spacecraft = {"name": "Voyager 1"}
    # spacecraft["distance"] = 0.01
    spacecraft.update({"distance" :0.01, "orbit" : "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    =========REPORT============ 
    
    Name: {spacecraft.get("name", "Unknown")}
    Distance:{spacecraft.get("distance", "Unknown")}
    Orbit: {spacecraft.get("orbit")}
    ============================
"""

main()