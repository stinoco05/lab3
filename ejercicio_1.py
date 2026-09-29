temperaturas = [18, 25, 31, 12, 28, 35, 30]
dias_frios = 0
dias_templados = 0
dias_calurosos = 0

for temperatura in temperaturas:
    if temperatura < 15:
        print(f"La temperatura {temperatura} es fría")
        dias_frios +=  1
    elif 15 <= temperatura <= 25:
        print(f"La temperatura {temperatura} es templada")
        dias_templados += 1
    else: 
        print(f"La temperatura {temperatura} es calurosa")
        dias_calurosos += 1

print(f"Días fríos: {dias_frios}, Días templados: {dias_templados} y Días calurosos: {dias_calurosos}")