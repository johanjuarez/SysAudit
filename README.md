# SysAudit

Herramienta de auditoría e inventario de equipos desarrollada en Python.

## Descripción

SysAudit es una aplicación diseñada para recopilar información técnica de equipos Windows y generar reportes de inventario orientados a soporte TI.

El objetivo principal es facilitar la documentación de activos tecnológicos, permitiendo obtener información del hardware, sistema operativo, red y software instalado.

---

## Características actuales

### Sistema
- Nombre del equipo
- Usuario actual
- Fabricante
- Modelo del equipo
- Número de serie
- Sistema operativo
- Versión y Build
- Arquitectura
- Tiempo de actividad

### Hardware
- Procesador
- Núcleos e hilos
- BIOS
- Memoria RAM
- Módulos instalados
- Placa madre
- Tarjeta gráfica
- Batería
- Discos físicos
- Particiones

### Red
- Adaptadores de red
- Dirección MAC
- Dirección IPv4
- Máscara de red
- Estado de conexión
- Velocidad
- Tipo de conexión

### Reportes
- Generación de reportes en formato TXT

---

## Tecnologías utilizadas

- Python 3
- WMI
- Psutil
- Git

---
## Instalación

### 1. Clonar repositorio

git clone https://github.com/johanjuarez/SysAudit.git

### 2. Crear entorno virtual

python -m venv .venv

### 3. Activar entorno virtual

.venv\Scripts\activate

### 4. Instalar dependencias

pip install -r requirements.txt

### 5. Ejecutar aplicación

python main.py
