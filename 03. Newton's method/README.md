# Интерполационна формула на Нютон

## Разделени разлики

## Интерполационна формула на Нютон
## Code snippets

```mathematica
dividedDiff[nodes_,values_] := (
 If[Length[nodes]==1,
Return[ values[[1]]],
Return[( dividedDiff[nodes[[2;;]],values[[2;;]]]-dividedDiff[nodes[[1;;-2]],values[[1;;-2]]])/
                      (nodes[[-1]]-nodes[[1]])]
]
)
```
```mathematica
newtonPoly[nodes_,values_, x_]:=Simplify[ values[[1]] + Sum[dividedDiff[nodes[[1;;k]],values[[1;;k]]]* Product[(x-nodes[[i]]),{i,1,k-1}],{k,2,Length[values]}]]
```

```
rungeX=Range[-1,1,2/10]
f[x_]=1/(1+25x^2)
rungeY=f[rungeX]

error[x_]:=f[x]-newtonPoly[rungeX,rungeY,x]

```


```
ChebishX=Table[Cos[(2k-1)Pi/(2*10)],{k,1,10}]
newtonPoly[ChebishX,f[ChebishX],x]
Plot[Abs[f[x]-newtonPoly[ChebishX,f[ChebishX],x]],{x,-1,1}]

```