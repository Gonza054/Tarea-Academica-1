# RutaLogix — Backend base (Caso 3, Grupo 3)

Base de software mínima para el Caso 3 del Anexo TA1. Representa **dos de los microservicios** descritos en el caso (`location_service` para GPS y `billing_service` para facturación), cada uno independiente, con su propia app Flask y sus propias pruebas. El grupo no necesita programar los microservicios: su entregable es el diseño del pipeline CI/CD.

## Qué incluye

- `location_service/app.py` + `test_app.py`: microservicio de ubicación en tiempo real.
- `billing_service/app.py` + `test_app.py`: microservicio de facturación por km recorrido.
- `requirements.txt` (compartido): Flask + pytest.

## Cómo correrlo localmente

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cd location_service && python3 -m pytest && cd ..
cd billing_service && python3 -m pytest && cd ..
```

## Qué debe hacer el grupo

Diseñar un pipeline que compile/instale dependencias y pruebe **cada microservicio por separado**, y que permita desplegarlos de forma independiente (por ejemplo, con imágenes de contenedor distintas), incluyendo una estrategia de rollback rápido, según la guía del Caso 3 del Anexo TA1.
