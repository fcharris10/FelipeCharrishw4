#include <stdio.h>
#include <stdlib.h>
#include <math.h>


//funcion principal 
int main(){
// declarar constantes 
int i;
int j;
int t;
double coeficientev = 0.0001;
double l=1;
double dx=0.1;
double tcaliente= 100;
double tfria= 50;
double posx= 0.2;
double posy= 0.1;
int n = l/dx;
//puntero de posicion 
double *x;
x= malloc((n * n) * sizeof(double));

double *y;
y= malloc((n * n ) * sizeof(double));
//puntero de temperatura
double *temperatura;
temperatura= malloc((n*n) * sizeof(double));
// puntero de temperatura futura o siguiente 
double *tsig;
tsig= malloc((n*n) * sizeof(double));



double *tiempo;
tiempo= malloc((n*n) * sizeof(double));



//en x se guardaran valores de la forma [0,dx,2dx,0,dx,2dx...] en y [0,0,0,dx,dx,dx....]
//siendo n el numero de puntos de la placa en el borde 

for(i=0; i< (n); i++){
	
	for(j=0; j<(n); j++){
	x[i* (n) + j] = j* dx;
	y[i* (n) + j] = i* dx;	
//printf(" %f ---%f  \n ", x[i* (n) + j], y[i* (n) + j]);
}

}

//lo que seguardara en el puntero de la temperatura, se llena todo la lamina y luego se busca el intervalo, ya que si se realiza al revez podemos tener problemas que no se ubique facilmente
 for(i=0; i<n*n; i++){
	temperatura[i]=tfria;
	if(x[i]>= 0.20 && x[i]<= 0.40){

	if(y[i]>= 0.45 && y[i]<= 0.55){
	
	temperatura[i]= tcaliente;
	}
}


//printf("%f %f %f \n ", temperatura[i], x[i],y[i]);
}

// se declararan las condiciones de frontera en primera instancia para el caso de T fija a 50°
for(t =0; t < 2500; t++){
tiempo[t]=t;//contador de tiempo

	for(i=0; i< n*n; i++){
		if(tiempo[t]==0.0 && i<n*n){
		tsig[i]=temperatura[i]; //al inicio si tenemos un tiempo unicial de 0
		}
		if( i<n ){ //si nos encontramos en el extremo inferior
		tsig[i]=tfria;
		}

		if( i<(n*n)-n){//ahora si estamos en el extremo superior
		tsig[i]= tfria;
		}

		if(x[i] <= dx+(dx/10)){ //si estamos en el lado izquiedo de la lamina
		tsig[i]= tfria;
		}
		if(x[i] == 0.9){//si estamos en el lado derecho de la lamina 
		tsig[i]= tfria;
		}
		else
		{
		tsig[i]= temperatura[i] +  (coeficientev * (-4 * temperatura[i]+ tsig[i+1]+temperatura[i-1]+ temperatura[i+n]+ temperatura[i-n]));// para las centrales usare en mi codigo siempre la misma forma que no dependen de las que estan en el extremo 	
		}
		if(tiempo[t]==0.0 || tiempo[t]==100.0 || tiempo[t]==2500.0  ){
		printf(" %f %f %f   \n ",  x[i],y[i],tsig[i]);
		}

}
	
}
//se declaran las condiciones de  Frontera abierta, donde la derivada en ese limite es 0 
for(t =0; t < 2500; t++){
tiempo[t]=t;
	for(i=0; i<n*n; i++){

		if(tiempo[t]==0.0 && i<n*n){
		tsig[i]=temperatura[i]; //al inicio si tenemos un tiempo unicial de 0
		}

		if(i<(n*n)-n){//si nos encontramos en el extremo superior

		tsig[i]=temperatura[i-n];
		}
		if(i<n){                     //-si nos encontramos en el extremo inferior
		tsig[i]=temperatura[i+n];
		}
		if(x[i]==0.0){                     // estamos ahora al lado Izquierdo de la placa
		tsig[i]=temperatura[i+1];
		}
		if(x[i]==0.9){                   // y ahora al lado derecho
		tsig[i]=temperatura[i-n];
		}
		else{      //las que no dependen de su ubicacion en los bordes y estan en el Centro
		tsig[i]= temperatura[i]+ coeficientev*((-4*temperatura[i])+temperatura[i-1]+temperatura[i+1]+temperatura[i+n]+temperatura[i-n]);
		}
		if(tiempo[t]==0.0 || tiempo[t]==100.0 || tiempo[t]==2500.0 ){
		printf(" %f %f %f   \n ",  x[i],y[i],tsig[i]);
		}
	}
}
//se declaran las condiciones de frontera periodica, en este caso se tomo como si uno jugara pacman el de la derecha del nodo del borde derecho seria el del borde izquierdo 

for(t =0; t < 2500; t++){
tiempo[t]=t;
	for(i=0; i<n*n; i++){

		if(tiempo[t]==0.0 && i<n*n){
		tsig[i]=temperatura[i]; //al inicio si tenemos un tiempo unicial de 0
		}
	
		else if(x[i]==0.9){  // si nos encontramos a la derecha 
		
		tsig[i]=temperatura[i]+coeficientev*((-4*temperatura[i])+temperatura[i-n]+temperatura[i+n]+temperatura[i-1]+temperatura[i-n+1]);
		}
		else if(x[i]==0.0){                   //si nos econtramos ahora a la Izquierda
		
		tsig[i]=temperatura[i]+coeficientev*((-4*temperatura[i])+temperatura[i-n]+temperatura[i+n]+temperatura[i+n-1]+temperatura[i+1]);
		}
		else if(i<(n*n)-n){          //ahora extremo superior
		tsig[i]=temperatura[i]+coeficientev*((-4*temperatura[i])+temperatura[i-n]+temperatura[i+n]+temperatura[i-1]+temperatura[i-n+1]);
		}
		else if(i<n){                      // extremo inferior
		tsig[i]=temperatura[i]+coeficientev*((-4*temperatura[i])+temperatura[i+n]+temperatura[n*n-n+i]+temperatura[i+1]+temperatura[i-1]);
		}
		else{                            //las que no dependen de su ubicacion en los bordes y estan en el Centro
		
		tsig[i]=temperatura[i]+coeficientev*((-4*temperatura[i])+temperatura[i-1]+temperatura[i+1]+temperatura[i+n]+temperatura[i-n]);
		}
		if(tiempo[t]==0.0 || tiempo[t]==100.0 || tiempo[t]==2500.0 ){
		printf(" %f %f %f   \n ",  x[i],y[i],tsig[i]);
		}
	}


}


free(x);
free(y);
free(temperatura);
return 0;
}


