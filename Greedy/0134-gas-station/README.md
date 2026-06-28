it is a simple greedy solution, where we start from i, we travel to j, we calc net_gain for every station, when our tank become empty the way we crossed cannot be a starting position

so, we assign start = i+1 , reset the tank and check further

if the total fuel was < total cost it is -1,   we can just check total < 0 here, because that is the total net gain (fuel - cost)

TC = O( n )
SC = O( 1 )
