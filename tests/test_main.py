from minha_app.main import saudacao


def test_saudacao() -> None:
    assert saudacao("Mundo") == "Olá, Mundo!"


def test_saudacao_com_nome() -> None:
    assert saudacao("Ana") == "Olá, Ana!"
