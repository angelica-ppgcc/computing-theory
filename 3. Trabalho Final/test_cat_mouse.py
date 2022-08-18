from turing_machine import TuringMachine

transition__cat = {("1","1"):("2", "1", "R"),
                   ("1","4"):("4", "4", "R"),
                   ("2","2"):("3", "2", "R"),
                   ("2","7"):("4", "7", "R"),
                   ("3","3"):("1", "3", "R"),
                   ("4","5"):("5", "5", "R"),
                   ("4","8"):("2", "8", "R"),
                   ("5","6"):("1", "6", "R")}

transition__mou = {("1","1"):("3", "1", "R"),
                   ("1","4"):("5", "4", "R"),
                   ("2","3"):("1", "3", "R"),
                   ("3","2"):("2", "2", "R"),
                   ("4","6"):("1", "6", "R"),
                   ("5","5"):("4", "5", "R")}
 

accepting_states = [" "]
final_states = {" "}

MT1 = TuringMachine("3 ", 
                  initial_state = "3",
                  final_states = final_states,
                  transition_function=transition__cat)

MT2 = TuringMachine("56 ", 
                  initial_state = "5",
                  final_states = final_states,
                  transition_function=transition__mou)

flag = 0
while not MT1.final() or  not MT2.final():
    simbolg = MT1.step()
    simbolm = MT2.step()
    if simbolg == simbolm:
        flag = 1
        print "Strings rejeitadas! Ambos os animais se encontram na sala ",simbolg
        break
    else:
        continue

if flag == 0:
    print "Strings aceitas! O gato se encontra na sala "+str(simbolg)+" e o rato na sala "+str(simbolm)


                        