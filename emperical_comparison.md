
I compared three approaches to the coin change problem using the coin denominations [1, 2, 5] and target amounts of 5, 10, 15, 20, 25, and 30. I measured the execution time of each approach using Python's time.perf_counter() function.

Results
Amount    Recursive (s)     Memoized (s)      Bottom-Up (s)
5         0.00001470        0.00000530        0.00000500
10        0.00007010        0.00000810        0.00000670
15        0.00093530        0.00001150        0.00000870
20        0.01374250        0.00001400        0.00001030
25        0.19772600        0.00002440        0.00001710
30        2.70730050        0.00002740        0.00001900

The results show how much slowwer the recursive approach gets each time the amount increases. It repeatedly solves the subproblems.
