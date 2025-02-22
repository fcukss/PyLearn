def main():
    fruit = input("Item: " )
    res = "Calories: "
    match fruit:
        case 'apple':
           print(f"{res} 130")
        case 'avocado'| 'cantaloupe' | 'honeydew melon' | "pineapple" | 'straberries' | 'tangerine' :
            print (f"{res} 50")
        case 'banana':
            print (f"{res} 110")
        case 'grapefruit'| 'nectarine' | 'peach' :
            print (f"{res} 60")
        case 'grapes' | 'kiwifruit':
            print (f"{res} 90")
        case 'lemon' :
            print (f"{res} 15")
        case 'lime':
            print (f"{res} 20")
        case 'pear' | 'sweet cherries':
            print(f"{res} 100")
        case 'plums':
            print(f"{res} 70")

main()