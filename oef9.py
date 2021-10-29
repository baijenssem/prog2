naam = input("wat is je naam")
aantaltickets = input("hoeveel tickets wil je")
prijstickets = input("en prijs per ticket")
aantaltickets = int(aantaltickets)
prijstickets = int(prijstickets)


print(f"""geachte{naam})
bedankt voor u bestelling van {aantaltickets} tickets ze  kosten {aantaltickets*prijstickets} euro.
MVG
het ticketshopteeam""")
