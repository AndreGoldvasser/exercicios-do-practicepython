# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this
# opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers
# in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
# sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def gera_fibonacci(numeros_sequencia=7):
    lista_fibonacci = []
    for x in range(1, numeros_sequencia):
        if x == 1 or x == 2:
            lista_fibonacci.append(1)
        else:
            lista_fibonacci.append(lista_fibonacci[-1]+lista_fibonacci[-2])
    return lista_fibonacci

print((gera_fibonacci(int(input("Quantos números para a sequência Fibonacci: \n")))))




