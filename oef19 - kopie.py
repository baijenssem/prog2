print("""<svg version="1.1"
    baseProfile="full"
    width="300" height="200"
    xmlns="http://www.w3.org/2000/svg">
    <circle cx="150" cy="100" r="80" fill="green" />
 </svg>""")
for i in range(100):
   for j in range(100):
      cx=i*100
      cy=j*100
      print(f"""<circle cx="{i,j}" cy="{i,j}" r="80" fill="green" />""")