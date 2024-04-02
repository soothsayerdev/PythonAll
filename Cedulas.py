def calculoDeCedulas():
    value_buy = float(input("Digite o valor da compra: "))
    value_money = float(input("Digite o valor dado: "))
    
    notes = [100.00, 50.00, 20.00, 10.00,
             5.00, 2.00, 1.00, 0.50,
             0.25, 0.10, 0.05, 0.01]
    
    rest = value_money - value_buy
    change = rest
    
    for note in notes:
        if change >= note:
            count = int(change // note)
            print(f"{count} de R$ {note:.2f}")
            change -= count * note
            
    print(f"Troco: R$ {rest:.2f}")

calculoDeCedulas()
    