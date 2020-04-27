# DD1327 Övning 3
2020-04-08 Kl 10.00

## Induktionsbevis - Uppgift 3.1 
Vi vill med hjälp av induktion, bevisa att den rekursiva fakultetsfunktionen i uppgift 3.1 är korrekt. <br>
Det vill säga: *n! = n(n - 1)!*.
- (1) Basfall: *n = 1.*
   >  1! = 1(1 - 1)! = 1 · 0! = 1
- (2) Antag att satsen *n! = n(n - 1)!* gäller för det positiva heltalet *n*.

- (3) Bevisa att satsen även gäller för nästkommande heltal *n+1*, dvs: *(n + 1)! = (n + 1)n!.*

  > HL = (n + 1)! = (n + 1)·n·(n - 1)·(n - 2)...·1·0! = (n + 1)·n·(n - 1)! = (n + 1)·n! = VL 

Satsen gäller för alla *n=1*, positiva heltalet *n* och som följd även *n+1*. Principen för matematisk induktion medför därmed att satsen gäller för alla positiva heltal. <br>
Q.E.D.
