def tbls():

            options = print("1 - Celsius\n2 - Kelvin\n3 - Fahrenheit")
            choice = (int(input("Digite a escala base que deseja converter: ")))


            if choice == 1:
                from tabelas.escalas_tabeladas.tbl_celsius import resultados_celsius as cc
                cc()
            elif choice == 2:
                from tabelas.escalas_tabeladas.tbl_kelvin import resultados_kelvin as rk
                rk()
            elif choice == 3:
                from tabelas.escalas_tabeladas.tbl_fahrenheit import resultados_fahrenheit as rf
                rf()
            else:
                print("ERROR!! Tente novamente!")
