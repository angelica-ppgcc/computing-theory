from turing_machine import TuringMachine

initial_state = "q0",
accepting_states = ["q5"],

'''
transition_function = {}
for e1 in range(9):
    for e2 in range(e1+1,10):
        dic = {("q0",str(e1)):("q0", str(e1), "R"),
               ("q0",str(e2)):("q1", str(e2), "R"),
               ("q0"," "):("q2", " ", "L"),
               ("q1",str(e1)):("q3", str(e2), "L"),
               ("q1",str(e2)):("q1", str(e2), "R"),
               ("q1"," "):("q2", " ", "L"),
               ("q2",str(e1)):("q2", str(e1), "L"),
               ("q2",str(e2)):("q2", str(e2), "L"),
               ("q2"," "):("q5", " ", "R"),
               ("q3",str(e2)):("q4", str(e1), "L"),
               ("q4",str(e1)):("q4", str(e1), "L"),
               ("q4",str(e2)):("q4", str(e2), "L"),
               ("q4"," "):("q0", " ", "R"),
               ("q5"," "):("q0", " ", "R"),
               ("q5",str(e1)):("q0", " ", "R"),
               ("q5",str(e2)):("q0", " ", "R"),
             }
        transition_function.update(dic)

print(transition_function)
'''
transition_function = {("q0","0"):("q0", "0", "R"),
                       ("q0","1"):("q1", "1", "R"),
                       ("q0"," "):("q2", " ", "L"),
                       ("q1","0"):("q3", "1", "L"),
                       ("q1","1"):("q1", "1", "R"),
                       ("q1"," "):("q2", " ", "L"),
                       ("q2","0"):("q2", "0", "L"),
                       ("q2","1"):("q2", "1", "L"),
                       ("q2"," "):("q5", " ", "R"),
                       ("q3","1"):("q4", "0", "L"),
                       ("q4","0"):("q4", "0", "L"),
                       ("q4","1"):("q4", "1", "L"),
                       ("q4"," "):("q0", " ", "R"),
                       }
final_states = {"q5"}

t = TuringMachine("00100 ", 
                  initial_state = "q0",
                  final_states = final_states,
                  transition_function=transition_function)

print("Cadeia processada:\n" + t.get_tape())

t.string_process()

print("Saída da Maquina de Turing:")    
print("Fita de saida:", t.get_tape())