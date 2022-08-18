#Programa que implementa um AFD e processa cadeias 


class Automato:
    
    def __init__(self, alfabeto, conj_estados, func_transicao, estado_inicial, conj_estados_finais):
            self._alfabeto = alfabeto
            self._conj_estados = conj_estados
            self._func_transicao = func_transicao
            self._estado_inicial = estado_inicial
            self._conj_estados_finais = conj_estados_finais

    def processar_cadeia(self, cadeia):
        cadeia = list(cadeia)

        estado_atual = self._estado_inicial

        while(len(cadeia)>0):
            print cadeia
            print "Estado atual:", estado_atual
            simbolo = cadeia[0]
            estado_atual = self._func_transicao[str(estado_atual)+str(simbolo)]
            cadeia.remove(simbolo)
        
        if(estado_atual in self._conj_estados_finais):
            resultado = "ACEITA!, estado de parada: "+str(estado_atual)
        else:
            resultado = "REJEITA, estado de parada: "+str(estado_atual)


        return resultado

    def processar_cadeias(self, cadeias):
        for cadeia in cadeias:
            print(self.processar_cadeia(cadeia))

#Autômato que aceita cadeias com uma quantidade ímpar de 1's
a = Automato([1,0],[0,1],{'00':0, '01':1, '10':1, '11': 0}, 0, [1])

print(a.processar_cadeias(['0','111','1111','01000','0001']))

