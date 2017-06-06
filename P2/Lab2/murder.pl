person(albert).
person(bruno).
person(carmen).
person(daniel).
person(elisa).

object(knife).
object(gun).
object(candlestick).
object(leadpipe).

fingerprints(albert,knife).
fingerprints(elisa,knife).
fingerprints(daniel,leadpipe).
fingerprints(bruno,leadpipe).
fingerprints(carmen,gun).
fingerprints(bruno,gun).
fingerprints(albert,candlestick).
fingerprints(daniel,candlestick).




hat(carmen).
hat(elisa).
hat(albert).

nonantique(leadpipe).
nonantique(candlestick).


suspect(X,Y):-fingerprints(X,Y),object(Y).

murder(X,Y):-hat(X),nonantique(Y),suspect(X,Y),person(X).






