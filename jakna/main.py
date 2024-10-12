from procenat import izracunaj_novu_cenu_jakne
jakna=1200
lopta=3000
nova_cena_jakne = izracunaj_novu_cenu_jakne(jakna)
nova_cena_lopte = izracunaj_novu_cenu_jakne(lopta)
if(nova_cena_jakne>nova_cena_lopte):
    print("jakna je skuplja")
elif(nova_cena_lopte>nova_cena_jakne):
    print("lopta je skuplja")
else:
    print("jednake su cene")
