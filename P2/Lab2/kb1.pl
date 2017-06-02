male(jaume1).
male(carles1).
male(carles2).
male(jaume2).
male(jorge).

female(laura).
female(neus).
female(sonia).

parent(carles1,jaume1).
parent(neus,james1).
parent(carles2,carles1).
parent(laura,carles1).
parent(jaume2,carles1).
parent(sonia,neus).
parent(jorge,sonia).

mother(X,Y) :- parent(X,Y), female(Y).
father(X,Y) :- parent(X,Y), male(Y).
sibling(X,Y) :- parent(X,Z), parent(Y,Z), dif(X,Y).
brother(X,Y) :- sibling(X,Y), male(X).
sister(X,Y) :- sibling(X,Y), female(X).
