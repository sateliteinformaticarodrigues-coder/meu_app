"""Ponto de entrada da aplicação."""


def saudacao(nome: str) -> str:
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}!"


def main() -> None:
    print(saudacao("Mundo"))


if __name__ == "__main__":
    main()
