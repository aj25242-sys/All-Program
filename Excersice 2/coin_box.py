# A coin box contain some type of coin, like rs10, rs5, rs2, rs1, paisa50, paisa 25. Now calculate amount in terms.

rs10 = int(input("Enter quantity of 10rs coins = "))
rs5 = int(input("Enter quantity of 5rs coins = "))
rs2 = int(input("Enter quantity of 2rs coins = "))
rs1 = int(input("Enter quantity of 1rs coins = "))
paisa50 = int(input("Enter quantity of 50 paisa coint = "))
paisa25 = int(input("Enter quantity of 25 paisa coins = "))

total_paisa = (rs10 * 1000) + (rs5 * 500) + (rs2 * 200) + (rs1 * 100) + (paisa50 * 50) + (paisa25 * 25)
rupees = total_paisa // 100
paisa = total_paisa * 100

print("Total Rupess ", rupees, "Total paisa", paisa)
