from math import sin, cos, sqrt, atan2, radians

class City_dist:

    def __init__(self, lat1, lat2, lon1, lon2):  
        self.lat1 = lat1
        self.lat2 = lat2
        self.lon1 = lon1
        self.lon2 = lon2

    # Methode to calculate distance
    def findDistance(self):
        R = 6373.0
        lat1 = radians(self.lat1)
        lon1 = radians(self.lon1)
        lat2 = radians(self.lat2)
        lon2 = radians(self.lon2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1        
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c


if __name__ == "__main__":
    # Taking Inputs from User
    [ilat1, ilon1] = input("City 1: ").split(", ")
    [ilat2, ilon2] = input("City 2: ").split(", ") 

    # formatting from dms to decimal
    def formatDMS(dms):
        [num, direction] = dms.split(" ")
        num = float(num)
        if direction == "S" or direction == "W":
            num *= -1
        return float(num)

    lat1 = formatDMS(ilat1)
    lat2 = formatDMS(ilat2)
    lon1 = formatDMS(ilon1)
    lon2 = formatDMS(ilon2)
    
    dis=City_dist(lat1,lat2,lon1,lon2)

    print("City 1 and City 2 are", round(dis.findDistance(),2), "km apart")
