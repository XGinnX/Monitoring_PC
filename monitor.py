import platform as pt, psutil as pu, socket as so

print(pt.system(),pt.release())

print(pt.processor())

# Memória RAM
print(f"{pu.virtual_memory().total / (1024**3):.2f} GB RAM")

# Disco
print(pu.disk_usage('/').percent, "% ocupado")

#Bateria 
print(pu.sensors_battery())

# IP
print(so.gethostbyname(so.gethostname()))