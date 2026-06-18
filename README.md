# TPI - Gestión de Datos de Países (Programación 1)

## 👥 Integrantes - Grupo 205
* **Gustavo Ramon Parodi**
* **Matheo Santiago Cardozo**

---

## 📝 Descripción del Programa
Este sistema es una aplicación de consola desarrollada en **Python** diseñada para la gestión, análisis y filtrado de información de países. Permite la persistencia de datos mediante un archivo local en formato **CSV** (`paises.csv`), asegurando que las modificaciones (altas y actualizaciones) se guarden automáticamente. 

El programa implementa controles estrictos de validación de datos para evitar desbordamientos de tipos, entradas vacías o inconsistencias matemáticas (como valores negativos o iguales a cero en población y superficie).

### Características Principales:
* **Persistencia Eficiente:** Lectura automatizada al iniciar y escritura inmediata en archivo al realizar cambios.
* **Robustez Frente a Errores:** Control de formatos incorrectos y omisión controlada de registros dañados en el CSV.
* **Filtrado Avanzado:** Consultas dinámicas por continente y por rangos numéricos acotados.
* **Estadísticas en Tiempo Lineal $O(n)$:** Cálculos óptimos de máximos, mínimos, promedios aritméticos y tablas de frecuencias sin alterar el dataset original.

---

## 🔗 Links del Proyecto
* **Repositorio de GitHub:** https://github.com/matheosc/TPI_Programacion1
* **Video Explicativo:** [Ver Video Explicativo en YouTube](https://youtu.be/OnO3xBGW6XA)

---

## 🚀 Instrucciones de Uso

### Prerrequisitos
* Tener instalado **Python 3.x**.
* Contar con el archivo `paises.csv` en la misma carpeta que el código fuente (`main.py`).

### Estructura del Archivo de Datos (`paises.csv`)
El archivo CSV debe contener obligatoriamente la cabecera en la primera línea. Ejemplo:
```csv
nombre,poblacion,superficie,continente
Argentina,46000000,2780400,América
España,47000000,505990,Europa
