
f = open ("tekst")
print(f)

f.close()


#kodowanie ASCII
#a-zA-Z
# 7 bitt -128
# 1111111 = 1+2+4+8+16+32+64
# Unicode
#kodowanie UTF - 8  (początkowe bity zakodowane jak w ASCII)

f = open ("tekst")
for line in f:
    print(line)
f.close()

f = open ("tekst")
print(f.read())
f.close()

try:
    f = open('tekst')
    #cos tu robimy
except Exception:
    f.close()
    print("Wyjątek")
finally:
    f.close()   #duzo kodu trochę

#menager kontekstu
with open ("tekst", encoding= 'utf -8') as f:
    print(f.read())