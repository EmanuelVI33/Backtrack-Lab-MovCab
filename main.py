import Matrix

if __name__ == "__main__":
    a = Matrix.Matrix(7, 7)
    if a.backtrack(1, 1, 5, 5):
        print("Existe solución")
        print(f"Número de vueletas: {a.get_laps()}")
        print(a.to_string())
    else:
        print("No existe Solucion")
        print(a.to_string())

