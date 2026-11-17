import random
import os

# Blackjack de consola: sin dependencias externas.

VALORES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
}
PALOS = ["♠", "♥", "♦", "♣"]
RANGOS = list(VALORES.keys())


def crear_baraja():
    baraja = [(rango, palo) for palo in PALOS for rango in RANGOS]
    random.shuffle(baraja)
    return baraja


def valor_mano(mano):
    total = sum(VALORES[carta[0]] for carta in mano)
    ases = sum(1 for carta in mano if carta[0] == "A")
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total


def mostrar_mano(nombre, mano, ocultar_primera=False):
    if ocultar_primera:
        cartas = ["[??]"] + [f"[{r} {p}]" for r, p in mano[1:]]
        print(f"{nombre}: {' '.join(cartas)}")
    else:
        cartas = [f"[{r} {p}]" for r, p in mano]
        print(f"{nombre}: {' '.join(cartas)}  => {valor_mano(mano)}")


def pedir_apuesta(saldo):
    while True:
        entrada = input(f"Tu saldo: {saldo} fichas | Apuesta (0 para salir): ").strip()
        try:
            apuesta = int(entrada)
            if apuesta == 0:
                return 0
            if 1 <= apuesta <= saldo:
                return apuesta
            print(f"Apuesta entre 1 y {saldo}.")
        except ValueError:
            print("Escribe una cantidad entera.")


def jugar_ronda(saldo, baraja, apuesta):
    jugador = [baraja.pop(), baraja.pop()]
    crupier = [baraja.pop(), baraja.pop()]

    print("\\n--- REPARTO ---")
    mostrar_mano("Tú", jugador)
    mostrar_mano("Crupier", crupier, ocultar_primera=True)

    # Blackjack natural (21 con las dos primeras cartas)
    blackjack_jugador = valor_mano(jugador) == 21
    blackjack_crupier = valor_mano(crupier) == 21

    if blackjack_jugador or blackjack_crupier:
        print("\\n--- MANOS ---")
        mostrar_mano("Tú", jugador)
        mostrar_mano("Crupier", crupier)
        if blackjack_jugador and blackjack_crupier:
            print("¡Empate! Se devuelve tu apuesta.")
            return saldo
        if blackjack_jugador:
            premio = int(apuesta * 1.5)  # beneficio 3:2, más la apuesta
            print(f"¡BLACKJACK! Ganas {premio} fichas de beneficio.")
            return saldo + apuesta + premio
        print("El crupier tiene Blackjack. Pierdes la apuesta.")
        return saldo - apuesta

    # Turno del jugador
    while True:
        total = valor_mano(jugador)
        if total >= 21:
            break
        accion = input("\\n¿Quieres (P)edir carta o (Q)uedarte? ").strip().lower()
        if accion in ("p", "pedir"):
            carta = baraja.pop()
            jugador.append(carta)
            print(f"Robas: [{carta[0]} {carta[1]}]")
            mostrar_mano("Tú", jugador)
            if valor_mano(jugador) > 21:
                print("¡Te has pasado de 21! Pierdes.")
                return saldo - apuesta
        elif accion in ("q", "quedar", "quedarse"):
            break
        else:
            print("Opción no válida. Escribe P o Q.")

    # Turno del crupier: roba hasta 17
    print("\\n--- TURNO DEL CRUPIER ---")
    mostrar_mano("Crupier", crupier)
    while valor_mano(crupier) < 17:
        carta = baraja.pop()
        crupier.append(carta)
        print(f"El crupier roba: [{carta[0]} {carta[1]}]")
        mostrar_mano("Crupier", crupier)

    total_j = valor_mano(jugador)
    total_c = valor_mano(crupier)
    print("\\n--- RESULTADO ---")
    mostrar_mano("Tú", jugador)
    mostrar_mano("Crupier", crupier)

    if total_c > 21 or total_j > total_c:
        print(f"¡GANAS! +{apuesta} fichas.")
        return saldo + apuesta
    if total_j == total_c:
        print("Empate. Se devuelve tu apuesta.")
        return saldo
    print(f"Pierdes {apuesta} fichas.")
    return saldo - apuesta


def main():
    saldo = 1000
    print("=" * 42)
    print("          ♠ BLACKJACK DE CONSOLA ♥")
    print("=" * 42)
    print("Objetivo: acercarte a 21 sin pasarte.")
    print("El crupier roba hasta alcanzar 17.")
    print("A, J, Q y K: 11 (A puede valer 1); figuras: 10.")
    print("Empiezas con 1000 fichas. ¡Suerte!\\n")

    while saldo > 0:
        apuesta = pedir_apuesta(saldo)
        if apuesta == 0:
            break

        # Se usa una baraja nueva si quedan menos de 15 cartas
        if "baraja" not in locals() or len(baraja) < 15:
            baraja = crear_baraja()
            print("\\nSe mezcla una nueva baraja.")

        saldo -= apuesta  # la apuesta se descuenta antes de jugar
        saldo = jugar_ronda(saldo, baraja, apuesta)

        print(f"\\n💰 Saldo actual: {saldo} fichas")
        if saldo <= 0:
            print("Te has quedado sin fichas. Fin de la partida.")
            break

        seguir = input("\\n¿Otra partida? (S/N): ").strip().lower()
        if seguir not in ("s", "si", "sí"):
            break

    print(f"\\nGracias por jugar. Te vas con {saldo} fichas. ¡Hasta pronto!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\\nPartida interrumpida. ¡Hasta la próxima!")
