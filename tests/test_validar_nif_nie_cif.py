from src.validarnif.validadores import validar_nif_nie_cif


def count_cases(fich: str) -> (int, int):
    ok = 0
    with open(fich, 'r') as ids:
        for count, ident in enumerate(ids):
            if validar_nif_nie_cif(ident.strip()):
                ok += 1
    return ok, count + 1

def test_nif_bien():
    (ok, lines) = count_cases('lista_nifs_bien.txt')
    assert (ok == lines)

def test_nif_mal():
    (ok, _) = count_cases('lista_nifs_mal.txt')
    assert not ok

def test_nie_bien():
    (ok, lines) = count_cases('lista_nies_bien.txt')
    assert (ok == lines)

def test_nie_mal():
    (ok, _) = count_cases('lista_nies_mal.txt')
    assert not ok

def test_cif_bien():
    (ok, lines) = count_cases('lista_cifs_bien.txt')
    assert (ok == lines)

def test_cif_mal():
    (ok, _) = count_cases('lista_cifs_mal.txt')
    assert not ok

