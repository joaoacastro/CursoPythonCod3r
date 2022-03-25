nums = [1, 2, 3]
print(type(nums)) #imprime <class 'list'>, ou seja o tipo de nums é list

print(nums)

nums.append(4) #o append adiciona mais um item na lista
nums.append(5)
nums.append(6)

print(len(nums)) #retorna 6, ou seja, os 3 primeiros, mais três que foram adicionados, no caso o 4, o 5 e o 6.

print(nums) #imprime [1, 2, 3, 4, 5, 6]

nums[3] = 100 #o indice 3, passa a receber o valor 100
print(nums) #imprime [1, 2, 3, 100, 4, 5]
nums.insert(0, -10) # ou seja, no indice 0 vai ser inserido o valor de -10
print(nums) #imprime [-10, 1, 2, 3, 1000, 4, 5]
print(len(nums)) #retorna a quantidade de itens da lista, no caso 7

print(nums[6]) #imprime o elemento na posiçao seis, ou seja ultima posiçao neste exemplo, no caso, imprime o valor 6, pois sempre inicia em zero

#outro metodo para pegarmos o ultimo elemento, é se utilizarmos -1 como no exemplo abaixo
print(nums[-1]) #neste exemplo imprime o valor 6

print(nums[-2]) #imprime o penultimo valor, no caso imprime o valor 5

print (1 in nums) #imprime como True