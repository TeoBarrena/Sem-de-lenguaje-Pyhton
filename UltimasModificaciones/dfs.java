public ListaGenerica<String> caminoSinCargarCombustible(String ciudad1,String ciudad2,int tanqueAuto){
    ListaGenerica<String> camino = new ListaEnlazadaGenerica<String>();
    if(!this.mapa.esVacio()) {
        boolean [] marca = new boolean [mapa.listaDeVertices().tamanio()+1];
        //para encontrar ciudad 1
        ListaGenerica<Vertice<String>> aux = mapa.listaDeVertices();
        aux.comenzar();
        Vertice<String> vertice;
        boolean ok = false;
        int i = -1;
        while((!aux.fin()) && (!ok)) {
            vertice = aux.proximo();
            if(vertice.dato().equals(ciudad1)) {
                ok = true;
                i = vertice.getPosicion();
            }
        }
        if(i != 1)
            dfsSinCargar(i,camino,marca,ciudad2,tanqueAuto);
    }
    return camino;
}
private boolean dfsSinCargar(int pos,ListaGenerica<String> camino,boolean [] marca,String ciudad2,int tanque) {
    boolean ok = false;
    marca[pos] = true;
    Vertice<String> v1 = mapa.vetice(pos);//la 1ra vez toma el valor de ciudad 1, las prox toma el valor de las adyacentes
    camino.agregarFinal(v1.dato());
    if(v1.dato().equals(ciudad2)) 
        ok = true;
    else {
        ListaGenerica<Arista<String>> ady = mapa.listaDeAdyacentes(v1);//obtiene los adyacentes
        ady.comenzar();
        while(!ok && !ady.fin()) {
            Arista<String> a = ady.proximo();//va recorriendo en profundidad
            int pesoA = a.peso();
            int posAdy = a.verticeDestino().getPosicion();
            if(!marca[posAdy] && pesoA <= tanque)
                ok = dfsSinCargar(posAdy,camino,marca,ciudad2,tanque - pesoA);
        }
    }
    if(!ok) {
        marca[pos] = false;
        camino.eliminarEn(camino.tamanio());  
    }
    return ok;
}

private int dfs(int pos, Vertice<String> v2,ListaGenerica<String> camMinimo,ListaGenerica<String> cam,boolean [] marca, int tanque,int tanqueActual,int cargaMin,int cargaActual) {
		marca[pos] = true;
		Vertice<String> v1 = this.mapa.vetice(pos);//toma el valor del vertice actual que se procesa 
		cam.agregarFinal(v1.dato());
		if(v1 == v2) {
			camMinimo.eliminarTodos();
			cargaMin = cargaActual;
			cam.comenzar();
			while(!cam.fin()) {
				camMinimo.agregarFinal(cam.proximo());
			}
		}
		else {
			ListaGenerica<Arista<String>> ady = this.mapa.listaDeAdyacentes(v1);//obtenes una lista con los adyacentes del vertice que estas procesando(dfs)
			ady.comenzar();
			while(cargaMin!= 0 && !ady.fin()) {
				Arista<String> a = ady.proximo();//vas recorriendo la lista de adyacentes y tomando sus adyacentes
				int j = a.verticeDestino().getPosicion();
				int peso = a.peso();
				if(!marca[j]) {
					if(peso <= tanqueActual)
						cargaMin = dfs(j,v2,camMinimo,cam,marca,tanque,tanqueActual - peso,cargaMin,cargaActual);
				}
				else if(peso <= tanque && cargaActual + 1 < cargaMin)
					cargaMin = dfs(j,v2,camMinimo,cam,marca,tanque,tanqueActual - peso,cargaMin,cargaActual + 1);
			}
		}
		marca[pos] = false;
		cam.eliminarEn(cam.tamanio());
		return cargaMin;
	}