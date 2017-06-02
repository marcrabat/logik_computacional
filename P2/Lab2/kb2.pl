cancer(brenda).

surgeon(bruce).
surgeon(amy).

town(brenda,smalltown).
town(bruce,knoxville).
town(amy,smalltown).

needs_surgery(X) :- cancer(X).

performed_surgery(X,Y) :- needs_surgery(X),surgeon(Y),town(X,Z),town(Y,Z).






