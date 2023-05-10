# Cycle (Intervalo: 1min)
1. Lee la api de USA, JAPON, CHILE y obtiene el ultimo sismo registrado para cada uno
2. Verifica que no se encuentra en el DB
3. Guarda el nuevo sismo

+ Build:

```bash
docker build -t sismology .
```

+ Run:

```bash
docker run --name sismic-logger sismology
```
