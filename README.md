# ISB Library (`isb-lib`)

**ISB** (*Ingeniería de Señales y Búsqueda de Sistemas*) es una librería de Python diseñada para automatizar el análisis simbólico y gráfico de señales y sistemas de forma equivalente a las herramientas de MATLAB (como `pzmap`).

Permite analizar expresiones simbólicas tanto en el dominio del tiempo $x(t)$ como en el dominio de la frecuencia/Laplace $X(s)$, calculando automáticamente la Transformada o Transformada Inversa de Laplace, así como los polos y ceros del sistema.

---

## 🚀 Instalación

Puedes instalar la librería directamente desde el repositorio de GitHub:

```bash
pip install git+https://github.com/MSMRo/ISB_LIB.git
```

Si estás trabajando en **Google Colab** o en un **Jupyter Notebook**, ejecuta:

```python
!pip install git+https://github.com/MSMRo/ISB_LIB.git
```

Para desarrollo local en editable mode:

```bash
git clone https://github.com/MSMRo/ISB_LIB.git
cd ISB_LIB
pip install -e .
```

---

## 💡 Uso Rápido

### 1. Graficar desde una Función en Laplace $X(s)$

```python
import sympy as sp
from isb_lib import ISB

# Definir variables simbólicas
t, s = sp.symbols('t s')

# Definir función de transferencia o señal en el dominio s
X_s = 1 / (s**2 + 2*s + 5)

# Graficar respuesta en el tiempo x(t) y plano s (Polos y Ceros)
X_s, x_t, polos, ceros = ISB.plot_pz(X_s, t_range=(0, 10))

print("Polos:", polos)
print("Ceros:", ceros)
```

### 2. Graficar desde una Función en el Tiempo $x(t)$

```python
import sympy as sp
from isb_lib import ISB

t, s = sp.symbols('t s')

# Función en el tiempo
x_t = sp.E**(-2*t) * sp.cos(2*t)

# Generar gráficos automáticamente
ISB.pzmap(x_t, t_range=(0, 6))
```

---

## 🛠️ API Reference

### `ISB.plot_pz(expr, t_range=(0, 10), num_pts=500, var_t='t', var_s='s', show_unit_circle=True, figsize=(12, 5))`

**Parámetros:**
- `expr` (*sympy.Expr*): Expresión simbólica en tiempo ($t$) o Laplace ($s$).
- `t_range` (*tuple*): Rango $(t_{min}, t_{max})$ para graficar en tiempo. Por defecto `(0, 10)`.
- `num_pts` (*int*): Número de puntos para evaluación numérica de la gráfica. Por defecto `500`.
- `var_t` (*str*): Nombre de la variable simbólica del tiempo (`'t'`).
- `var_s` (*str*): Nombre de la variable simbólica de Laplace (`'s'`).
- `show_unit_circle` (*bool*): Muestra el círculo unitario $|s| = 1$ como referencia. Por defecto `True`.
- `figsize` (*tuple*): Tamaño de la figura `(ancho, alto)`. Por defecto `(12, 5)`.

**Retorna:**
- `(X_s, x_t, polos, ceros)`: Tupla con las expresiones en Laplace y tiempo, junto con las listas de polos y ceros numéricos.

---

## 📄 Licencia

MIT License.
