temperatura.png: Plots_Temperatura.py Resultados.txt
	python Plots_Temperatura.py
Resultados.txt: a.out
	./a.out> Resultados.txt	

a.out: DifusionTemperatura.c
	gcc DifusionTemperatura.c
	
