def verificar_acesso(cargo, dia_semana):
    cargo = cargo.lower()
    dia_semana = dia_semana.lower()

    dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

    if cargo == "gerente":
        return "Acesso permitido."
    elif cargo in ["analista", "estagiário"]:
        if dia_semana in dias_uteis:
            return "Acesso permitido."
        else:
            return "Acesso negado. Permitido apenas em dias úteis."
    else:
        return "Acesso negado. Cargo não autorizado."


# Programa principal
cargo_input = input("Digite o cargo do funcionário: ")
dia_input = input("Digite o dia da semana: ")

resultado = verificar_acesso(cargo_input, dia_input)
print(resultado)
