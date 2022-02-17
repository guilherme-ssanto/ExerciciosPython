lp = float(input("Largura da parede: "))
ap = float(input("Altura da parede: "))
area = lp*ap
lt = area/2
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m². \nPara pintar essa parede, você precisará de {}l de tinta.".format(lp,ap,area,lt))