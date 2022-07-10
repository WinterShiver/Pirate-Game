# The Pirate Game

The ultimate solution of the [Pirate Game](https://en.wikipedia.org/wiki/Pirate_game).

海盗分金问题的终极解决方案。

## Usage

```bash
python main.py 
python main.py -m 10 -n 100 --casting --noprint-fail
```

## Arguments

Arguments:

* `-m`, optional

  The number of coins, which should be no less than 1. 

* `-n`, optional

  The number of pirates, which should be greater than 1. 

* `--casting`, optional

  By default, the distribution plan should get the agreement of the majority of pirates. As an example, when there are 2n pirates, a distribution plan is only approved when no less that n+1 pirates agree to the plan. 

  By opening this option, we adopt the rules introduced in Wikipedia, that a distribution plan is approved when up to half pirates agree to the plan. In that case, a distribution plan would be approved when n out of 2n pirates agree to the plan. 

* `--noprint-fail`, optional

  By default, the program would also print some information when a distribution plan is not approved. By opening this option, the program does not print any information when a distribution plan is not approved.

## Sample Running Results

The standard solution of the classical problem setting when there are 100 coins and 5 pirates:

```
> python main.py 
*******************************************************************
Distribution for pirate #2 with 100 coins would fail
*******************************************************************
A sample distribution for pirate #3 when there are 100 coins
[0, 0, 100]
Supporters: [2, 3]
Support rate: 2/3
*******************************************************************
A sample distribution for pirate #4 when there are 100 coins
[1, 1, 0, 98]
Supporters: [1, 2, 4]
Support rate: 3/4
*******************************************************************
A sample distribution for pirate #5 when there are 100 coins
[2, 0, 1, 0, 97]
Supporters: [1, 3, 5]
Support rate: 3/5
```

After the number of pirates exceeds two times of the number of coins, pirates after #20 who can guarantee their survival as captain are:

* #21, 20+2^0
* #22, 20+2^1
* #24, 20+2^2
* #28, 20+2^3
* #36, 20+2^4
* #52, 20+2^5
* #84, 20+2^6
* ...

```
python main.py -m 10 -n 100 --casting --noprint-fail
*******************************************************************
A sample distribution for pirate #2 when there are 10 coins
[0, 10]
Supporters: [2]
Support rate: 1/2
*******************************************************************
A sample distribution for pirate #3 when there are 10 coins
[1, 0, 9]
Supporters: [1, 3]
Support rate: 2/3
*******************************************************************
A sample distribution for pirate #4 when there are 10 coins
[0, 1, 0, 9]
Supporters: [2, 4]
Support rate: 2/4
*******************************************************************
A sample distribution for pirate #5 when there are 10 coins
[1, 0, 1, 0, 8]
Supporters: [1, 3, 5]
Support rate: 3/5
*******************************************************************
A sample distribution for pirate #6 when there are 10 coins
[0, 1, 0, 1, 0, 8]
Supporters: [2, 4, 6]
Support rate: 3/6
*******************************************************************
...
*******************************************************************
A sample distribution for pirate #19 when there are 10 coins
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
Supporters: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Support rate: 10/19
*******************************************************************
A sample distribution for pirate #20 when there are 10 coins
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
Supporters: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Support rate: 10/20
*******************************************************************
A sample distribution for pirate #21 when there are 10 coins
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
Supporters: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
Support rate: 11/21
*******************************************************************
A sample distribution for pirate #22 when there are 10 coins
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0]
Supporters: [2, 4, 6, 8, 10, 12, 16, 18, 20, 21, 22]
Support rate: 11/22
*******************************************************************
A sample distribution for pirate #24 when there are 10 coins
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0]
Supporters: [11, 12, 13, 13, 15, 15, 16, 19, 22, 22, 23, 24]
Support rate: 12/24
*******************************************************************
A sample distribution for pirate #28 when there are 10 coins
[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
Supporters: [3, 3, 5, 7, 9, 9, 15, 17, 17, 21, 25, 26, 27, 28]
Support rate: 14/28
*******************************************************************
A sample distribution for pirate #36 when there are 10 coins
[...]
Supporters: [...]
Support rate: 18/36
*******************************************************************
A sample distribution for pirate #52 when there are 10 coins
[...]
Supporters: [...]
Support rate: 26/52
*******************************************************************
A sample distribution for pirate #84 when there are 10 coins
[...]
Supporters: [...]
Support rate: 42/84
```

## Notes

For the goal *each pirate wants to maximize the number of gold coins he receives*, this program adopts the strategy of: 

* choose to maximize the expectation of the number of coins;
* if the expectation between choices are equal, choose to minimize the variance of the number of coins. 
