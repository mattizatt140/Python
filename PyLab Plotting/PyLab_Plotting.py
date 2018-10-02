import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.plot(mySamples, myLinear, label = 'O(n)')
plt.plot(mySamples, myQuadratic, label = 'O(x^2)')
plt.plot(mySamples, myCubic, label = 'O(x^3)')
plt.plot(mySamples, myExponential, label = 'O(1.5^x)')
plt.title('Big-O Time Complexity')
plt.legend(loc = 'upper left')
plt.ylim(0, 5000)
plt.show()