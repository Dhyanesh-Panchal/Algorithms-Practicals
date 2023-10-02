import matplotlib.pyplot as plt

def loopSum(n):
    sum=0
    iterations = 0


    for i in range(1,n+1):
        sum+=i
        iterations+=1

    return {"sum":sum,"iterations":iterations}


def eqSum(n):
    iterations = 0

    sum = n*(n+1)/2
    iterations+=1
    return {"sum":sum,"iterations":iterations}


def recursive_sum(n,depth=0):
    depth+=1
    if(n==1):
        return {"sum":1,"depth":depth}
    else:
        prev_data = recursive_sum(n-1,depth = depth)
        return {"sum":(n + prev_data["sum"]) ,"depth":prev_data["depth"] }

# Main exection
n = [100,200,300,400,500]
loop_data = []
equation_data = []
recursive_data = []
for i in n:
    loop_data.append(loopSum(i))
    equation_data.append(eqSum(i))
    recursive_data.append(recursive_sum(i))

print(loop_data)
print(equation_data)
print(recursive_data)

# Generating the plots
fig , (ax1,ax2,ax3) = plt.subplots(nrows=1,ncols=3,figsize=(15,5))

ax1.plot(n,list(map(lambda data:data["iterations"],loop_data)))
ax1.set(title="Sum by Loop",xlabel="Inupt Length" , ylabel="Iterations")

ax2.plot(n,list(map(lambda data:data["iterations"],equation_data)))
ax2.set(title="Sum by Equation",xlabel="Inupt Length" , ylabel="Iterations")

ax3.plot(n,list(map(lambda data:data["depth"],recursive_data)))
ax3.set(title="Sum by Recursion",xlabel="Inupt Length" , ylabel="Depth of recursion")

fig.show()