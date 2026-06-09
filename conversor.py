
def conversion():

        qtd = input("Converter Tabela (S/n): ").lower()
        if qtd == "s":
            from tabelas.tabela import tbls
            tbls()
            return 
        elif qtd == "n":

            options = print("1 - Celsius\n2 - Kelvin\n3 - Fahrenheit")
            choice = (int(input("Digite a escala base que deseja converter: ")))


            if choice == 1:
                from escalas.celsius import resultado_celsius as resultado_c
                resultado_c()
            elif choice == 2:
                from escalas.kelvin import resultado_kelvin as resultado_k
                resultado_k()
            elif choice == 3:
                from escalas.fahrenheit import resultado_fahrenheit as resultado_f
                resultado_f()
            else:
                print("ERROR!! Tente novamente!")

        else:
            print("ERROR!! Tente novamente!")

conversion()
