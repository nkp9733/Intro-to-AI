import inspect
import sys
from matplotlib import pyplot
import numpy

'''
Raise a "not defined" exception as a reminder 
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)

'''
Kalman 2D
'''
def kalman2d(data):
    estimated = []
    x_init = numpy.array([[2], [1]])
    p_init = numpy.array([[0.05,0],[0,0.05]])
    Q = numpy.array([[0.0001, 0.00002],[0.00002, 0.0001]])
    R = numpy.array([[0.01, 0.005],[0.005, 0.02]])
    I = numpy.array([[1,0],[0,1]])
    x_pred = numpy.zeros([2,1])
    p_pred = numpy.zeros([2,2])
    x_prev = numpy.zeros([2,1])
    p_prev = numpy.zeros([2,2])
    for i in range(0, len(data)):
        u = numpy.array([[data[i][0]], [data[i][1]]])
        z_obs = numpy.array([[data[i][2]],[data[i][3]]])
        if i == 0:
            x_pred = numpy.add(x_init,u)
            p_pred = numpy.add(p_init,Q)
        else:
            x_pred = numpy.add(x_prev,u)
            p_pred = numpy.add(p_prev,Q)
        #print x_pred
        denom = numpy.add(p_pred,R)
        kg = numpy.divide(p_pred,denom)
        temp = numpy.subtract(z_obs,x_pred)
        temp2 = numpy.dot(kg,temp)
        x_prev = numpy.add(x_pred,temp2)
        temp3 = numpy.subtract(I,kg)
        p_prev = numpy.dot(temp3,p_pred)
        print x_prev
        estimated.append([x_prev[0][0],x_prev[1][0]])
        
    print estimated
    print len(estimated)
    #_raise_not_defined()
    return estimated

'''
Plotting
'''
def plot(data, output):
    z1 = []
    z2 = []
    x1 = []
    x2 = []
    for i in range(0,len(data)):
        z1.append(data[i][2])
        z2.append(data[i][3])
    for j in output:
        x1.append(j[0])
        x2.append(j[1])
    z = pyplot.plot(z1,z2,'-bo')
    x = pyplot.plot(x1,x2,'-ro')
    pyplot.title('Observed vs. Estimated')
    pyplot.ylabel('z2, x2')
    pyplot.xlabel('z1, x1')
    #pyplot.plot(x,output)

    pyplot.show()
    #_raise_not_defined()
    return

'''
Kalman 2D 
'''
def kalman2d_shoot(ux, uy, ox, oy, reset=False):
    decision = (0, 0, False)
    # Your code starts here 
    # Your code ends here 
    _raise_not_defined()
    return decision

'''
Kalman 2D 
'''
def kalman2d_adv_shoot(ux, uy, ox, oy, reset=False):
    decision = (0, 0, False)
    # Your code starts here 
    # Your code ends here 
    _raise_not_defined()
    return decision


