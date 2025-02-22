import calculator


if __name__ == '__main__':
    calc = calculator.Calculator(years=3)
    calc.add_car(
        calculator.Car("Volkswagen Golf", 38500 , 7,1000,1000)
    )
    calc.add_car(
        calculator.ElectricCar("Tesla Model 3", 50000 , 1000,150)
    )


    calc.print_cars()