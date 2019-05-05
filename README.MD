# Solid Principles...in Python

Es un [acrónimo](https://es.wikipedia.org/wiki/Acr%C3%B3nimo "Acrónimo") [mnemónico](https://es.wikipedia.org/wiki/Mnem%C3%B3nico "Mnemónico") introducido por [Robert C. Martin](https://es.wikipedia.org/wiki/Robert_C._Martin "Robert C. Martin")[1](https://es.wikipedia.org/wiki/SOLID#cite_note-ub-old-web-solid-1)​[2](https://es.wikipedia.org/wiki/SOLID#cite_note-ub-solid-2)​ a comienzos de la década del 2000[3](https://es.wikipedia.org/wiki/SOLID#cite_note-metz-presentation-2009-3)​ que representa cinco principios básicos de la [programación orientada a objetos](https://es.wikipedia.org/wiki/Programaci%C3%B3n_orientada_a_objetos "Programación orientada a objetos") y el [diseño](https://es.wikipedia.org/wiki/Dise%C3%B1o_orientado_a_objetos "Diseño orientado a objetos"). Cuando estos principios se aplican en conjunto es más probable que un [desarrollador](https://es.wikipedia.org/wiki/Programador "Programador") cree un sistema que sea fácil de [mantener](https://es.wikipedia.org/wiki/Mantenimiento_de_Software "Mantenimiento de Software") y ampliar con el tiempo
Fuente: [https://es.wikipedia.org/wiki/SOLID](https://es.wikipedia.org/wiki/SOLID)

## SRP (Single Responsible Principle)

- Una clase = Un concepto y responsabilidad
- Una clase debería tener sólo 1 razón para cambiar
- Cómo:
  - Clases pequeñas con objetivos acotados
- Si es que tienes más de un método público puede ser señal de más de una responsabilidad
- Nombres de servicios muy abstractos EmailService vs EmailSender (solo enviará emails)
- Finalidad: - Alta cohesión y robustez - Permitir composición de clases (inyección) - Reducir duplicidad

**Niveles de granularidad**
Ejemplo:

- Order | User: Son modelos de dominio, no servicios
- OrderAnalyzer | OrderProcessor: términos genéricos lleva a más de 1 responsabilidad
- OrderTrustabilityChecker | OrderMarginCalculator: son más específicos

## OCP (Open Close Principle)

- El software debería estar abierto a extensión y cerrado a modificación
- Cómo:
  - No dependiendo de implementaciones especificas
- Finalidad:
  - Fácil de añadir nuevos caso de uso

**Beneficios de interfaces:**

- No modifica árbol jerarquía.
- Permite implementar N.

**Beneficios abstract class:**

- Permite patrón template method empujando lógica al modelo.
- Problema: Dificultad de trazar.
- Getter privados (tell don’t ask).

## LSP (Liskov Substitution Principle)

- Si S es un subtipo de T, instancia de T deberían poderse sustituir por instancias de S sin alterar las propiedades del programa.
- Cómo:
  - El comportamiento de subclases debe respetar el contrato de las superclases.
- Finalidad:
  - Mantener correctitude para poder aplicar OCP.

## ISP (Interface Segregation Principle)

- Ningún cliente debería verse forzado a depender de métodos que no usa.
- Como: Definir contratos de interfaces basándonos en los clientes que las usan y no en las implementaciones que pudiéramos tener.
- Evitar Header Interface promoviendo Role Interface.
- LAS INTERFACES PERTENECEN A LOS CLIENTES
- Finalidad:
  - Alta cohesión y bajo acoplamiento estructural.

## DIP (Dependency Inversion Principle)

- Módulos de alto nivel no deberían depender de los de bajo nivel. Ambos deberían depender de abstracciones.
- Como:

  - Inyectar dependencias (parámetros recibidos idealmente en constructor).
  - Depender de las interfaces (contratos) de estas dependencias y no de las implementaciones concretas.
  - LSP como premisa.

- Finalidad:
  - Facilitar la modificación y substitución de implementaciones.
  - Mejor testabilidad de clases.
