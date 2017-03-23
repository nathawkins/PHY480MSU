def oneplanet(t, planet):
    def coorx(xi, h,vxi, axi):
        return xi + h*vxi+h**2*axi/2

    def velx(vxi, h, ax_i_1,ax_i):
        return vxi + (h/2)*(ax_i_1+ax_i)

    def accx(coor, dist):
        return -4*math.pi**2*coor/(dist**3)


    time = t #The number of years we want to loop over
    h = 1/365 #The step size, defined as one day
    n = int(t/h) #The total numbers of iterations

    coordinatesx = np.zeros(n+1)
    velocitiesx = np.zeros(n+1)

    coordinatesx[0] = planet.x
    velocitiesx[0] = planet.vx
    rad = r(planet)

    for i in range(n):
        x_i = coordinatesx[i]
        vx_i = velocitiesx[i]
        ax_i = accx(x_i, rad)
        x_i_1 = coorx(x_i, h,vx_i,ax_i)
        coordinatesx[i+1] = x_i_1
        ax_i_1 = accx(x_i_1, rad)
        vx_i_1 = velx(vx_i,h,ax_i_1,ax_i)
        velocitiesx[i+1] = vx_i_1

    def coory(yi, h,vyi, ayi):
        return yi + h*vyi+h**2*ayi/2

    def vely(vyi, h, ay_i_1,ay_i):
        return vyi + (h/2)*(ay_i_1+ay_i)

    def accy(coor, dist):
        return -4*math.pi**2*coor/(dist**3)


    coordinatesy = np.zeros(n+1)
    velocitiesy = np.zeros(n+1)

    coordinatesy[0] = planet.y
    velocitiesy[0] = planet.vy

    for i in range(n):
        y_i = coordinatesy[i]
        vy_i = velocitiesy[i]
        ay_i = accy(y_i, rad)
        y_i_1 = coory(y_i, h,vy_i,ay_i)
        coordinatesy[i+1] = y_i_1
        ay_i_1 = accy(y_i_1, rad)
        vy_i_1 = vely(vy_i,h,ay_i_1,ay_i)
        velocitiesy[i+1] = vy_i_1

    def coorz(zi, h,vzi, azi):
        return zi + h*vzi+h**2*azi/2

    def velz(vzi, h, az_i_1,az_i):
        return vzi + (h/2)*(az_i_1+az_i)

    def accz(coor, dist):
        return -4*math.pi**2*coor/(dist**3)

    coordinatesz = np.zeros(n+1)
    velocitiesz = np.zeros(n+1)

    coordinatesz[0] = planet.z
    velocitiesz[0] = planet.vz

    for i in range(n):
        z_i = coordinatesz[i]
        vz_i = velocitiesz[i]
        az_i = accz(z_i, rad)
        z_i_1 = coorz(z_i, h,vz_i,az_i)
        coordinatesz[i+1] = z_i_1
        az_i_1 = accz(z_i_1, rad)
        vz_i_1 = velz(vz_i,h,az_i_1,az_i)
        velocitiesz[i+1] = vz_i_1

    return coordinatesx, coordinatesy, coordinatesz
