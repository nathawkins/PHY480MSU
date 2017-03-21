def twoplanet(t, planet1, planet2):
    def coorx(xi, h,vxi, axi):
        return xi + h*vxi+h**2*axi/2

    def velx(vxi, h, ax_i_1,ax_i):
        return vxi + (h/2)*(ax_i_1+ax_i)

    def accx(coor1,coor2, dist, sepdist):
        return -4*math.pi**2*coor1/(dist**3)-4*math.pi**2*(coor1-coor2)/(sepdist**3)

    def coory(yi, h,vyi, ayi):
        return yi + h*vyi+h**2*ayi/2

    def vely(vyi, h, ay_i_1,ay_i):
        return vyi + (h/2)*(ay_i_1+ay_i)

    def accy(coor1,coor2, dist, sepdist):
        return -4*math.pi**2*coor1/(dist**3)-4*math.pi**2*(coor1-coor2)/(sepdist**3)

    def coorz(zi, h,vzi, azi):
        return zi + h*vzi+h**2*azi/2

    def velz(vzi, h, az_i_1,az_i):
        return vzi + (h/2)*(az_i_1+az_i)

    def accz(coor1,coor2, dist, sepdist):
        return -4*math.pi**2*coor1/(dist**3)-4*math.pi**2*(coor1-coor2)/(sepdist**3)


    time = t #The number of years we want to loop over
    h = 1/365 #The step size, defined as one day
    n = int(t/h) #The total numbers of iterations


    coordinatesx1 = np.zeros(n+1)
    velocitiesx1 = np.zeros(n+1)
    coordinatesy1 = np.zeros(n+1)
    velocitiesy1 = np.zeros(n+1)
    coordinatesz1 = np.zeros(n+1)
    velocitiesz1 = np.zeros(n+1)

    coordinatesx2 = np.zeros(n+1)
    velocitiesx2 = np.zeros(n+1)
    coordinatesy2 = np.zeros(n+1)
    velocitiesy2 = np.zeros(n+1)
    coordinatesz2 = np.zeros(n+1)
    velocitiesz2 = np.zeros(n+1)

    coordinatesx1[0] = planet1.x
    velocitiesx1[0] = planet1.vx
    coordinatesy1[0] = planet1.y
    velocitiesy1[0] = planet1.vy
    coordinatesz1[0] = planet1.z
    velocitiesz1[0] = planet1.vz

    coordinatesx2[0] = planet2.x
    velocitiesx2[0] = planet2.vx
    coordinatesy2[0] = planet2.y
    velocitiesy2[0] = planet2.vy
    coordinatesz2[0] = planet2.z
    velocitiesz2[0] = planet2.vz

    rad1 = r(planet1)
    rad2 = r(planet2)

    for i in range(n):
        #Define x coordinates for both planets
        x1_i = coordinatesx1[i]
        vx1_i = velocitiesx1[i]
        x2_i = coordinatesx2[i]
        vx2_i = velocitiesx2[i]

        #Define y coordinates for both planets
        y1_i = coordinatesy1[i]
        vy1_i = velocitiesy1[i]
        y2_i = coordinatesy2[i]
        vy2_i = velocitiesy2[i]

        #Define z coordinates for both planets
        z1_i = coordinatesz1[i]
        vz1_i = velocitiesz1[i]
        z2_i = coordinatesz2[i]
        vz2_i = velocitiesz2[i]

        #Distance between them, should be the same for both planets
        rsep1 = ((x1_i-x2_i)**2+(y1_i-y2_i)**2+(z1_i-z2_i)**2)**(1/2)
        rsep2 = ((x2_i-x1_i)**2+(y2_i-y1_i)**2+(z2_i-z1_i)**2)**(1/2)

        ax1_i = accx(x1_i,x2_i, rad1, rsep1)
        ax2_i = accx(x1_i,x2_i, rad2, rsep2)
        ay1_i = accy(y1_i,y2_i, rad1, rsep1)
        ay2_i = accy(y1_i,y2_i, rad2, rsep2)
        az1_i = accz(z1_i,z2_i, rad1, rsep1)
        az2_i = accz(z1_i,z2_i, rad2, rsep2)

        x1_i_1 = coorx(x1_i, h,vx1_i,ax1_i)
        x2_i_1 = coorx(x2_i, h,vx2_i,ax2_i)
        y1_i_1 = coory(y1_i, h,vy1_i,ay1_i)
        y2_i_1 = coory(y2_i, h,vy2_i,ay2_i)
        z1_i_1 = coorz(z1_i, h,vz1_i,az1_i)
        z2_i_1 = coorz(z2_i, h,vz2_i,az2_i)

        coordinatesx1[i+1] = x1_i_1
        coordinatesx2[i+1] = x2_i_1
        coordinatesy1[i+1] = y1_i_1
        coordinatesy2[i+1] = y2_i_1
        coordinatesz1[i+1] = z1_i_1
        coordinatesz2[i+1] = z2_i_1

        ax1_i_1 = accx(x1_i_1, x2_i_1, rad1, rsep1)
        ax2_i_1 = accx(x2_i_1, x1_i_1, rad2, rsep2)
        ay1_i_1 = accy(y1_i_1, y2_i_1, rad1, rsep1)
        ay2_i_1 = accy(y2_i_1, y1_i_1, rad2, rsep2)
        az1_i_1 = accz(z1_i_1, z2_i_1, rad1, rsep1)
        az2_i_1 = accz(z2_i_1, z1_i_1, rad2, rsep2)

        vx1_i_1 = velx(vx1_i,h,ax1_i_1,ax1_i)
        velocitiesx1[i+1] = vx1_i_1
        vx2_i_1 = velx(vx2_i,h,ax2_i_1,ax2_i)
        velocitiesx2[i+1] = vx2_i_1
        vy1_i_1 = vely(vy1_i,h,ay1_i_1,ay1_i)
        velocitiesy1[i+1] = vy1_i_1
        vy2_i_1 = vely(vy2_i,h,ay2_i_1,ay2_i)
        velocitiesy2[i+1] = vy2_i_1
        vz1_i_1 = velz(vz1_i,h,az1_i_1,az1_i)
        velocitiesz1[i+1] = vz1_i_1
        vz2_i_1 = velz(vz2_i,h,az2_i_1,az2_i)
        velocitiesz2[i+1] = vz2_i_1

    return (coordinatesx1, coordinatesx2), (coordinatesy1, coordinatesy2), (coordinatesz1, coordinatesz2)
