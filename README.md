# validarnif

Módulo Python para la validación de identificadores fiscales españoles: NIF (Número de Identificación Fiscal), 
NIE (Número de Identidad de Extranjero) y CIF (Código de Identificación Fiscal).

## Características

Proporciona funciones de validación conforme a la normativa vigente en 2024, incluyendo el CIF como concepto 
independiente a pesar de que ya no tiene entidad legal propia al haberse integrado en la denominación 
general de NIF.

Por omisión, valida el identificador tal cual aparece en la cadena de texto. Opcionalmente, se puede aplicar un 
preprocesamiento para estandarizar el formato antes de validar: elimina espacios y caracteres extraños, completa 
el número con ceros por la izquierda e iguala mayúsculas/minúsculas.

## Instalación

```bash
# Clonar el repositorio
$ git clone https://github.com/sustoja/validarnif.git

# Acceder al directorio
$ cd validarnif
```

## Uso

Importa el módulo y utiliza las funciones para validar NIF, NIE o CIF:

```python
from src import validar_dni, validar_nie, validar_cif, validar_nif_nie_cif

# Validar un DNI
print(validar_dni("77697094N"))

# Validar un NIE
print(validar_nie("X0631255C"))

# Validar un CIF
print(validar_cif("H27513647"))

# Validar cualquier identificador con preprocesamiento
print(validar_nif_nie_cif("x-631255-c", preprocesar=True))  
```

## Funciones principales

- `validar_dni(dni: str) -> bool`: Valida un DNI.
- `validar_nie(nie: str) -> bool`: Valida un NIE.
- `validar_cif(cif: str) -> bool`: Valida un CIF.
- `validar_nif_nie_cif(identificador: str, preprocesar: bool = True) -> bool`: Estandariza el formato del 
- identificador antes de validar.

## Referencias

- [Ministerio del Interior: Cálculo del dígito de control del NIF/NIE](https://www.interior.gob.es/opencms/es/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/)
- [Wikipedia: Número de Identificación Fiscal](https://es.wikipedia.org/wiki/N%C3%BAmero_de_identificaci%C3%B3n_fiscal)
- [Wikipedia: Código de Identificación Fiscal](https://es.wikipedia.org/wiki/C%C3%B3digo_de_identificaci%C3%B3n_fiscal)
- [GitHub: NIF, DNI, NIE, CIF validation](https://github.com/josegoval/nif-dni-nie-cif-validation/tree/master)
- [fjrodriguezg: Validación de CIF en Java](https://fjrodriguezg.wordpress.com/2015/08/14/validando-cif-en-java-definitivo/)

## Contribuciones

Se agradecen las contribuciones mediante fork del repositorio y solicitudes de pull request.

## Licencia

Este proyecto utiliza la **Licencia MIT**.
