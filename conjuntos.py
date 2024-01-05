conjunto={"Jhon",1,"Alexander",2,"Aleja"}
conjunto1=frozenset(["dato1","dato2"])
conjunto2={"dato3",conjunto1}
print(conjunto2)


conjunto1={1,3,5,7}
conjunto2={1,3,7}

resultado=conjunto1.issubset(conjunto2)
print(resultado)

