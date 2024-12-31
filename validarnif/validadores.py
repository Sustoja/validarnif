# Módulo para la validación del identificador fiscal español de personas físicas y jurídicas: NIF, NIE y CIF

import re

# Constantes

LETRAS_CONTROL = {
    "DNI": "TRWAGMYFPDXBNJZSQVHLCKE",
    "CIF": "JABCDEFGHI",
}
DNI_INVALIDOS = {'', '00000000T', '00000001R', '99999999R', 'X0000000T'}
NIE_CONVERSOR = {'X': '0', 'Y': '1', 'Z': '2'}
CIF_TIPOS_ULTIMO_CARACTER = {
    "LETRA": lambda char: 'A' <= char <= 'Z',
    "NUMERO": lambda char: '0' <= char <= '9',
    "AMBOS": lambda char: ('A' <= char <= 'Z') or ('0' <= char <= '9')
}


# Funciones auxiliares

def _patron_es_invalido(regex: str, valor: str) -> bool:
    return not bool(re.match(regex, valor))

def _preprocesar(cadena: str) -> str:
    cadena = re.sub(r'[^a-zA-Z0-9]', '', cadena).upper()

    if len(cadena) < 9:
        if cadena[0].isdigit():
            cadena = cadena.zfill(9)
        elif cadena[0].isalpha():
            cadena = cadena[0] + cadena[1:].zfill(8)

    return cadena

def _calcular_control_dni(numero: str) -> str:
    idx = int(numero) % 23
    return LETRAS_CONTROL["DNI"][idx]

def _calcular_control_cif(suma: int) -> (str, int):
    idx = (10 - suma % 10) % 10
    return LETRAS_CONTROL["CIF"][idx], idx


# Validadores

def validar_dni(dni: str) -> bool:
    if dni in DNI_INVALIDOS or _patron_es_invalido(r'^([KLM]\d{7}|\d{8})[TRWAGMYFPDXBNJZSQVHLCKE]$', dni):
        return False

    numero, letra_control = dni[:-1], dni[-1]
    return _calcular_control_dni(numero) == letra_control

def validar_nie(nie: str) -> bool:
    if _patron_es_invalido(r'^[XYZ]\d{7}[TRWAGMYFPDXBNJZSQVHLCKE]$', nie):
        return False

    nie_convertido = NIE_CONVERSOR[nie[0]] + nie[1:]
    return validar_dni(nie_convertido)

def validar_cif(cif: str) -> bool:
    if _patron_es_invalido(r'^[ABCDEFGHJKLMNPQRSUVW]\d{7}[A-Z0-9]$', cif):
        return False

    primer_car, digitos, ultimo_car = cif[0], cif[1:-1], cif[-1]
    tipo_ultimo_car = (
        "LETRA" if primer_car in "PQSKW" else
        "NUMERO" if primer_car in "ABEH" else
        "AMBOS"
    )

    suma_pares = sum(int(digitos[i]) for i in range(1, len(digitos), 2))
    suma_impares = sum(sum(int(x) for x in str(int(digitos[i]) * 2)) for i in range(0, len(digitos), 2))
    total = suma_pares + suma_impares

    car_control, idx_control = _calcular_control_cif(total)
    return CIF_TIPOS_ULTIMO_CARACTER[tipo_ultimo_car](ultimo_car) and (
        (ultimo_car.isdigit() and int(ultimo_car) == idx_control) or (ultimo_car == car_control)
    )

def validar_nif_nie_cif(identificador: str, preprocesar: bool = True) -> bool:
    if not isinstance(identificador, str):
        return False

    if preprocesar:
        identificador = _preprocesar(identificador)

    return validar_dni(identificador) or validar_nie(identificador) or validar_cif(identificador)
