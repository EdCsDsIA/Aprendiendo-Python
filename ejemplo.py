# Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual 
# al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
# Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 
# 2 centavos, más el 32% del excedente sobre 85,528 pesos.


ingreso = float(input("Ingrese el ingreso anual:"))
if (ingreso < 85528.00):
    if ingreso < 0:
        impuesto = 0
    else:
        impuesto = (ingreso * 0.18) - 556.02
else:
    impuesto = ((ingreso - 85528) * 0.32) + 14839.02
impuesto = round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")