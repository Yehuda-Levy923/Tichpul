%Yehuda Levy 332300433


married(avr,sara).                
married(yit,rivka).
married(yaak,lea).
married(yaak,rachel).
parent(avr,yit).
parent(sara,yit).
parent(rivka,yaak).
parent(yit,yaak).
parent(yaak,reuven). 
parent(yaak,shimon).
parent(yaak,levi).
parent(yaak,yehuda).
parent(yaak,dina).
parent(yaak,yoseph).
parent(yaak,binyamin).
parent(yehuda,zerach).
parent(yehuda,peretz).
parent(levi,kehat).
parent(levi,gershon).
parent(levi,merari).
parent(lea,reuven).  
parent(lea,shimon).
parent(lea,levi).
parent(lea,yehuda).
parent(lea,dina).
parent(rachel,yoseph).
parent(rachel,binyamin).
male(avr).
male(yit).
male(yaak).
male(reuven).
male(shimon).
male(levi).
male(yehuda).
male(yoseph).
male(binyamin).
male(zerach).
male(peretz).
male(kehat).
male(gershon).
male(merari).
female(sara).
female(rivka).
female(lea).
female(rachel).
female(dina).

% 1. Father
father(X, Y) :- 
    parent(X, Y),
    male(X).

% 2. Mother
mother(X, Y) :- 
    parent(X, Y),
    female(X).

% 3. Son
son(X, Y) :- 
    parent(Y, X),
    male(X).

% 4. Daughter
daughter(X, Y) :- 
    parent(Y, X),
    female(X).

% 5. Grandfather
grandfather(X, Y) :- 
    parent(X, Z),
    parent(Z, Y),
    male(X).

% 6. Grandmother
grandmother(X, Y) :- 
    parent(X, Z),
    parent(Z, Y),
    female(X).

% 7. Grandson
grandson(X, Y) :- 
    parent(Y, Z),
    parent(Z, X),
    male(X).

% 8. Granddaughter
granddaughter(X, Y) :- 
    parent(Y, Z),
    parent(Z, X),
    female(X).

% 9. Sibling
sibling(X, Y) :- 
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% 10. Uncle by marriage
uncle_by_marriage(X, Y) :- 
    parent(Z, Y),
    parent(W, Z1),
    parent(W, Z),
    female(Z1),
    married(X, Z1),
    male(X).

% 11. Male cousin from female aunt
male_cousin_from_aunt(X, Y) :- 
    parent(Z, Y),
    parent(W, Z),
    parent(W, Z1),
    female(Z1),
    parent(Z1, X),
    male(X).

% 12. Brother-in-law (3 cases)
% Case 1: Husband of sibling
brother_in_law(X, Y) :- 
    parent(Z, Y),
    parent(Z, W),
    Y \= W,
    married(X, W),
    male(X).

% Case 2: Brother of spouse
brother_in_law(X, Y) :- 
    (married(Y, Z) ; married(Z, Y)),
    parent(W, Z),
    parent(W, X),
    Z \= X,
    male(X).

% Case 3: Husband of spouse's sibling
brother_in_law(X, Y) :- 
    (married(Y, W) ; married(W, Y)),
    parent(Z, W),
    parent(Z, V),
    W \= V,
    married(X, V),
    male(X).

% 13. Niece
niece(X, Y) :- 
    parent(Z, X),
    parent(Z, W),
    W \= Y,
    parent(Y1, Y),
    parent(Y1, W),
    female(X).

% 14. Second cousins
second_cousins(X, Y) :- 
    parent(PX, X),
    parent(PY, Y),
    parent(GX, PX),
    parent(GX, PY),
    PX \= PY,
    X \= Y.

% 15. Y is niece of X's grandmother
niece_of_grandmother(X, Y) :- 
    parent(G, Z),
    parent(Z, X),
    female(G),
    parent(W, Y),
    parent(W, G1),
    G \= G1,
    parent(W, G),
    female(Y).
